import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# =============================================================================
# SIMULATION CONFIG — Edit all parameters here
# =============================================================================
class Config:
    # --- MODE SELECTOR ---
    # "rod"  → tumbling rigid rod:  RK4 (quadratic drag + torque)  vs  perturbation (linear drag)
    # "ball" → point-mass sphere:   RK4 (quadratic drag)           vs  perturbation (linear drag)
    # In both modes the two curves use the SAME object's parameters, so the only
    # difference shown is the numerical method vs the analytic approximation.
    MODE = "rod"   # <-- change this: "rod" | "ball"

    # --- Launch parameters (shared) ---
    LAUNCH_SPEED    = 35.0   # initial speed [m/s]
    LAUNCH_ANGLE    = 45.0   # launch angle above horizontal [degrees]

    # --- Wind (affects RK4 only; perturbation assumes no wind) ---
    WIND_X          = 0.0    # horizontal wind [m/s]  (set to 0 for a clean RK4 vs pert. comparison)
    WIND_Y          = 0.0    # vertical wind [m/s]

    # -------------------------------------------------------------------------
    # ROD parameters  (used when MODE = "rod")
    # -------------------------------------------------------------------------
    ROD_MASS        = 20.0    # mass [kg]   — heavier → smaller ε → perturbation more valid
    ROD_LENGTH      = 1.0    # length [m]  (longer → more visible tumbling)
    ROD_CD          = 0.4    # drag coefficient
    ROD_AREA        = 0.05   # reference area = width × length [m²]
                             # effective width for torque: d = ROD_AREA / ROD_LENGTH
    ROD_THETA_0_DEG = 30.0   # initial tilt from horizontal [degrees]
    ROD_OMEGA_0     = 0.0    # initial angular velocity [rad/s]

    # Perturbation for the rod uses the rod's own mass/drag to derive ε:
    #   ε = 0.5·ρ·Cd·A / m   [1/m]
    # This linearises the rod's quadratic drag at the launch speed.
    # For the approx. to hold: ε·v₀·T << 1.
    # If the warning fires, increase ROD_MASS or decrease ROD_CD / ROD_AREA.

    # -------------------------------------------------------------------------
    # BALL parameters  (used when MODE = "ball")
    # -------------------------------------------------------------------------
    BALL_MASS       = 7.26   # mass [kg]   — shot put ≈ 7.26 kg  (heavier → perturbation more valid)
    BALL_RADIUS     = 0.06   # radius [m]  — shot put ≈ 0.06 m
    BALL_CD         = 0.47   # drag coefficient for a smooth sphere

    # -------------------------------------------------------------------------
    # Fluid / environment (shared)
    # -------------------------------------------------------------------------
    G               = 9.81   # gravitational acceleration [m/s²]
    RHO             = 1.225  # air density [kg/m³]

    # -------------------------------------------------------------------------
    # Integrator
    # -------------------------------------------------------------------------
    DT              = 0.01   # RK4 time step [s]
    MAX_STEPS       = 5000   # safety cap

    # -------------------------------------------------------------------------
    # Animation / display
    # -------------------------------------------------------------------------
    INTERVAL_MS     = 15     # ms between frames
    FIG_WIDTH       = 12
    FIG_HEIGHT      = 6
    ROD_LINEWIDTH   = 4
# =============================================================================


assert Config.MODE in ("rod", "ball"), \
    f"Config.MODE must be 'rod' or 'ball' — got '{Config.MODE}'"


# =============================================================================
# SHARED HELPERS
# =============================================================================
def _flight_time_array(cfg):
    """Time array covering a generous upper bound of the flight duration."""
    angle_rad = np.radians(cfg.LAUNCH_ANGLE)
    t_max     = 2.0 * cfg.LAUNCH_SPEED * np.sin(angle_rad) / cfg.G * 1.3
    return np.linspace(0.0, t_max, int(t_max / cfg.DT) + 1)


def _mask_underground(x, y):
    """Replace positions below ground with NaN."""
    valid = y >= 0
    return np.where(valid, x, np.nan), np.where(valid, y, np.nan)


# =============================================================================
# PERTURBATION SOLUTION  (shared formula, object-specific ε)
# =============================================================================
def perturbation_solution(times, v0, angle_deg, epsilon, g):
    """
    First-order perturbation expansion for a projectile with weak linear drag:
        F_drag = -ε · m · v    (linear in v)

    ε [1/m] is matched to quadratic drag at launch speed v₀:
        ε = 0.5·ρ·Cd·A / m

    Expansion to O(ε):
        x(t) = v₀x·t  −  ½·ε·v₀·v₀x·t²
        y(t) = v₀y·t  −  ½·g·t²  −  ε·v₀·(½·v₀y·t²  −  g·t³/6)

    Returns x, y with NaN underground.
    """
    angle_rad = np.radians(angle_deg)
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)

    x = v0x * times - 0.5 * epsilon * v0 * v0x * times**2
    y = ( v0y * times
        - 0.5 * g * times**2
        - epsilon * v0 * (0.5 * v0y * times**2 - (g / 6.0) * times**3) )

    return _mask_underground(x, y)


def _check_perturbation_validity(epsilon, v0, angle_deg, g, label):
    """Print a warning if the weak-drag assumption ε·v₀·T << 1 is violated."""
    T = 2.0 * v0 * np.sin(np.radians(angle_deg)) / g
    smallness = epsilon * v0 * T
    status = "OK" if smallness < 0.3 else "WARNING — perturbation may be inaccurate"
    print(f"[{label}] ε·v₀·T = {smallness:.3f}  ({status})")


# =============================================================================
# ROD PHYSICS — RK4
# =============================================================================
def rod_derivatives(t, state, cfg, wind_v):
    """
    d/dt [x, y, vx, vy, theta, omega] for a tumbling rod.
    Quadratic aerodynamic drag on CM + aerodynamic torque.
    """
    x, y, vx, vy, theta, omega = state
    m, L, Cd, A = cfg.ROD_MASS, cfg.ROD_LENGTH, cfg.ROD_CD, cfg.ROD_AREA

    v_rel     = np.array([vx - wind_v[0], vy - wind_v[1]])
    v_rel_mag = np.linalg.norm(v_rel)

    F_g    = np.array([0.0, -m * cfg.G])
    F_d    = np.array([0.0,  0.0])
    torque = 0.0

    if v_rel_mag > 0:
        F_d = -0.5 * cfg.RHO * Cd * A * v_rel_mag * v_rel

        v_angle = np.arctan2(v_rel[1], v_rel[0])
        phi     = theta - v_angle
        d       = A / L                   # effective rod width [m]
        torque  = -0.5 * cfg.RHO * Cd * d * L**2 * v_rel_mag**2 * np.sin(2.0 * phi)

    ax_cm = (F_g[0] + F_d[0]) / m
    ay_cm = (F_g[1] + F_d[1]) / m
    I     = (1.0 / 12.0) * m * L**2      # thin uniform rod about CM
    alpha = torque / I

    return np.array([vx, vy, ax_cm, ay_cm, omega, alpha])


def simulate_rod_rk4(cfg):
    """RK4 integration for the rod. Returns trajectory (N,6) and times (N,)."""
    wind_v    = np.array([cfg.WIND_X, cfg.WIND_Y])
    angle_rad = np.radians(cfg.LAUNCH_ANGLE)
    state     = np.array([
        0.0, 0.0,
        cfg.LAUNCH_SPEED * np.cos(angle_rad),
        cfg.LAUNCH_SPEED * np.sin(angle_rad),
        np.radians(cfg.ROD_THETA_0_DEG),
        cfg.ROD_OMEGA_0,
    ], dtype=float)

    traj, times, t, dt = [state.copy()], [0.0], 0.0, cfg.DT

    while state[1] >= 0 and len(traj) < cfg.MAX_STEPS:
        k1 = rod_derivatives(t,        state,             cfg, wind_v)
        k2 = rod_derivatives(t + dt/2, state + k1*(dt/2), cfg, wind_v)
        k3 = rod_derivatives(t + dt/2, state + k2*(dt/2), cfg, wind_v)
        k4 = rod_derivatives(t + dt,   state + k3*dt,     cfg, wind_v)
        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        t    += dt
        traj.append(state.copy())
        times.append(t)

    return np.array(traj), np.array(times)


def rod_epsilon(cfg):
    """ε for the rod: linearise its own quadratic drag at v₀."""
    return 0.5 * cfg.RHO * cfg.ROD_CD * cfg.ROD_AREA / cfg.ROD_MASS


# =============================================================================
# BALL PHYSICS — RK4
# =============================================================================
def ball_derivatives(t, state, cfg, wind_v):
    """
    d/dt [x, y, vx, vy] for a point-mass sphere with quadratic drag.
    No torque (symmetric body).
    """
    x, y, vx, vy = state
    m  = cfg.BALL_MASS
    A  = np.pi * cfg.BALL_RADIUS**2      # frontal area

    v_rel     = np.array([vx - wind_v[0], vy - wind_v[1]])
    v_rel_mag = np.linalg.norm(v_rel)

    F_g = np.array([0.0, -m * cfg.G])
    F_d = np.array([0.0,  0.0])

    if v_rel_mag > 0:
        F_d = -0.5 * cfg.RHO * cfg.BALL_CD * A * v_rel_mag * v_rel

    ax = (F_g[0] + F_d[0]) / m
    ay = (F_g[1] + F_d[1]) / m

    return np.array([vx, vy, ax, ay])


def simulate_ball_rk4(cfg):
    """RK4 integration for the ball. Returns trajectory (N,4) and times (N,)."""
    wind_v    = np.array([cfg.WIND_X, cfg.WIND_Y])
    angle_rad = np.radians(cfg.LAUNCH_ANGLE)
    state     = np.array([
        0.0, 0.0,
        cfg.LAUNCH_SPEED * np.cos(angle_rad),
        cfg.LAUNCH_SPEED * np.sin(angle_rad),
    ], dtype=float)

    traj, times, t, dt = [state.copy()], [0.0], 0.0, cfg.DT

    while state[1] >= 0 and len(traj) < cfg.MAX_STEPS:
        k1 = ball_derivatives(t,        state,             cfg, wind_v)
        k2 = ball_derivatives(t + dt/2, state + k1*(dt/2), cfg, wind_v)
        k3 = ball_derivatives(t + dt/2, state + k2*(dt/2), cfg, wind_v)
        k4 = ball_derivatives(t + dt,   state + k3*dt,     cfg, wind_v)
        state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        t    += dt
        traj.append(state.copy())
        times.append(t)

    return np.array(traj), np.array(times)


def ball_epsilon(cfg):
    """ε for the ball: linearise its own quadratic drag at v₀."""
    A = np.pi * cfg.BALL_RADIUS**2
    return 0.5 * cfg.RHO * cfg.BALL_CD * A / cfg.BALL_MASS


# =============================================================================
# RUN
# =============================================================================
cfg  = Config()
mode = cfg.MODE

if mode == "rod":
    eps   = rod_epsilon(cfg)

    rk4_traj, rk4_times = simulate_rod_rk4(cfg)

    # Perturbation on a common time grid (use RK4 flight time as reference)
    t_grid          = _flight_time_array(cfg)
    pert_x, pert_y  = perturbation_solution(t_grid, cfg.LAUNCH_SPEED, cfg.LAUNCH_ANGLE, eps, cfg.G)

    rk4_x  = rk4_traj[:, 0]
    rk4_y  = rk4_traj[:, 1]
    rk4_theta = rk4_traj[:, 4]

else:  # "ball"
    eps   = ball_epsilon(cfg)

    rk4_traj, rk4_times = simulate_ball_rk4(cfg)

    t_grid          = _flight_time_array(cfg)
    pert_x, pert_y  = perturbation_solution(t_grid, cfg.LAUNCH_SPEED, cfg.LAUNCH_ANGLE, eps, cfg.G)

    rk4_x     = rk4_traj[:, 0]
    rk4_y     = rk4_traj[:, 1]
    rk4_theta = None   # ball has no angle

n_frames = max(len(rk4_times), len(t_grid))

# Last frame index where each trajectory is still above ground.
rk4_landed_at  = int(np.searchsorted(-rk4_y, 0))
rk4_landed_at  = min(rk4_landed_at, len(rk4_y) - 1)

pert_valid      = ~np.isnan(pert_y)
pert_landed_at  = int(np.where(pert_valid)[0][-1]) if pert_valid.any() else 0

# =============================================================================
# TERMINAL REPORT  —  Table I Metrics
# =============================================================================
def _print_report(cfg, mode, eps,
                  rk4_x, rk4_y, rk4_times, rk4_theta,
                  pert_x, pert_y, t_grid,
                  rk4_landed_at, pert_landed_at):

    v0  = cfg.LAUNCH_SPEED
    ang = cfg.LAUNCH_ANGLE
    g   = cfg.G
    rad = np.radians(ang)

    W  = 72   # total table width
    sep  = "+" + "-" * (W - 2) + "+"
    sep2 = "+" + "=" * (W - 2) + "+"

    def row(label, value, unit="", note=""):
        cell = f"{value}  {unit}  {note}".strip()
        inner = f"  {label:<34s}  {cell}"
        inner = inner.ljust(W - 2)
        return "|" + inner + "|"

    def header(title):
        inner = f"  {title}".ljust(W - 2)
        return "|" + inner + "|"

    print()
    print(sep2)
    print(header("TABLE I — SIMULATION METRICS"))
    print(sep2)

    # ------------------------------------------------------------------
    # 1. Vacuum (frictionless) analytic reference
    # ------------------------------------------------------------------
    vac_tf   = 2.0 * v0 * np.sin(rad) / g
    vac_xmax = v0**2 * np.sin(2 * rad) / g
    vac_ymax = (v0 * np.sin(rad))**2 / (2 * g)

    print(header("1. VACUUM (FRICTIONLESS) LIMIT  —  analytic"))
    print(sep)
    print(row("Max Range  x_max",        f"{vac_xmax:>10.4f}", "m"))
    print(row("Flight Time  t_f",         f"{vac_tf:>10.4f}",  "s"))
    print(row("Peak Height  y_max",       f"{vac_ymax:>10.4f}", "m"))
    print(sep)

    # ------------------------------------------------------------------
    # 2. Active-mode epsilon & smallness
    # ------------------------------------------------------------------
    T_flight_vac = vac_tf
    smallness    = eps * v0 * T_flight_vac
    warn         = "  [WARNING - PERTURBATION INVALID]" if smallness >= 0.3 else ""
    obj_label    = "ROD" if mode == "rod" else "BALL"

    print(header(f"2. ACTIVE MODE: {obj_label}"))
    print(sep)
    print(row("epsilon  (ε = 0.5·ρ·Cd·A / m)",  f"{eps:>10.6f}", "m⁻¹"))
    print(row("Smallness  ε·v₀·T_vac",            f"{smallness:>10.4f}", f"{warn}"))
    print(sep)

    # ------------------------------------------------------------------
    # 3. RK4 results
    # ------------------------------------------------------------------
    rk4_xmax = float(rk4_x[rk4_landed_at])
    rk4_ymax = float(np.max(rk4_y))
    rk4_tf   = float(rk4_times[rk4_landed_at])

    print(header("  RK4  (quadratic drag, numerical)"))
    print(sep)
    print(row("Max Range  x_max",  f"{rk4_xmax:>10.4f}", "m"))
    print(row("Flight Time  t_f",  f"{rk4_tf:>10.4f}",   "s"))
    print(row("Peak Height  y_max",f"{rk4_ymax:>10.4f}", "m"))
    print(sep)

    # ------------------------------------------------------------------
    # 4. Perturbation results
    # ------------------------------------------------------------------
    pert_xmax = float(pert_x[pert_landed_at])
    pert_ymax = float(np.nanmax(pert_y))
    pert_tf   = float(t_grid[pert_landed_at])

    print(header("  Perturbation  (linear drag, analytic O(ε))"))
    print(sep)
    print(row("Max Range  x_max",  f"{pert_xmax:>10.4f}", "m"))
    print(row("Flight Time  t_f",  f"{pert_tf:>10.4f}",   "s"))
    print(row("Peak Height  y_max",f"{pert_ymax:>10.4f}", "m"))
    print(sep)

    # ------------------------------------------------------------------
    # 5. Rod-only: rotation analysis
    # ------------------------------------------------------------------
    if mode == "rod" and rk4_theta is not None:
        theta_start = float(rk4_theta[0])
        theta_end   = float(rk4_theta[rk4_landed_at])
        total_rad   = abs(theta_end - theta_start)

        # Accumulate total rotation including direction reversals
        dtheta      = np.diff(rk4_theta[:rk4_landed_at + 1])
        total_rad_acc = float(np.sum(np.abs(dtheta)))   # absolute arc
        rotations   = total_rad_acc / (2 * np.pi)

        print(header("3. ROTATION ANALYSIS  (rod only)"))
        print(sep)
        print(row("Net angle change  Δθ",    f"{np.degrees(total_rad):>10.4f}", "deg"))
        print(row("Total arc  |∫ω dt|",      f"{total_rad_acc:>10.4f}",         "rad"))
        print(row("Total Takla (rotations)", f"{rotations:>10.4f}",             "rev"))
        print(sep)

    # ------------------------------------------------------------------
    # 6. Error matrix: RK4 vs Perturbation
    # ------------------------------------------------------------------
    dx_abs = abs(rk4_xmax - pert_xmax)
    dx_pct = dx_abs / rk4_xmax * 100.0 if rk4_xmax != 0 else float('nan')

    dt_abs = abs(rk4_tf - pert_tf)
    dt_pct = dt_abs / rk4_tf * 100.0   if rk4_tf   != 0 else float('nan')

    dy_abs = abs(rk4_ymax - pert_ymax)
    dy_pct = dy_abs / rk4_ymax * 100.0 if rk4_ymax != 0 else float('nan')

    n_label = "4." if mode == "ball" else "4."
    print(header(f"{n_label} ERROR MATRIX  |RK4 − Perturbation|"))
    print(sep)
    print(row("Range  |Δx|",        f"{dx_abs:>10.4f}", "m",  f"({dx_pct:.2f} %)"))
    print(row("Flight time  |Δt|",  f"{dt_abs:>10.4f}", "s",  f"({dt_pct:.2f} %)"))
    print(row("Peak height  |Δy|",  f"{dy_abs:>10.4f}", "m",  f"({dy_pct:.2f} %)"))
    print(sep2)
    print()


_print_report(cfg, mode, eps,
              rk4_x, rk4_y, rk4_times, rk4_theta,
              pert_x, pert_y, t_grid,
              rk4_landed_at, pert_landed_at)


# =============================================================================
# ANIMATION
# =============================================================================
fig, ax = plt.subplots(figsize=(cfg.FIG_WIDTH, cfg.FIG_HEIGHT))

all_x = [rk4_x, pert_x[~np.isnan(pert_x)]]
all_y = [rk4_y, pert_y[~np.isnan(pert_y)]]

x_min = min(0.0, float(np.nanmin(np.concatenate(all_x)))) - 1.0
x_max = float(np.nanmax(np.concatenate(all_x))) * 1.1
y_max = float(np.nanmax(np.concatenate(all_y))) * 1.2

ax.set_xlim(x_min, x_max)
ax.set_ylim(-1.0, y_max)
ax.axhline(0, color='saddlebrown', linewidth=1.5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlabel("Range (m)")
ax.set_ylabel("Height (m)")

if mode == "rod":
    title = (f"Rod  (m={cfg.ROD_MASS} kg, L={cfg.ROD_LENGTH} m, Cd={cfg.ROD_CD}) — "
             f"RK4 quadratic drag  vs  perturbation linear drag")
else:
    title = (f"Ball  (m={cfg.BALL_MASS} kg, r={cfg.BALL_RADIUS} m, Cd={cfg.BALL_CD}) — "
             f"RK4 quadratic drag  vs  perturbation linear drag")
ax.set_title(title, fontsize=10, fontweight='bold')

# RK4 trail
line_rk4_trail, = ax.plot([], [], 'b-', alpha=0.5, linewidth=1.5,
    label='RK4 — quadratic drag (numerical, exact)')

# Perturbation trail
line_pert_trail, = ax.plot([], [], 'r--', alpha=0.85, linewidth=1.5,
    label='Perturbation — linear drag (analytic, O(ε) approx.)')

# Moving object marker(s)
if mode == "rod":
    rod_body, = ax.plot([], [], 'k-', linewidth=cfg.ROD_LINEWIDTH,
        marker='o', mec='steelblue', mfc='steelblue', markersize=5, label='Rod body (RK4 quadratic drag)')
    ball_dot  = None
else:
    ball_dot, = ax.plot([], [], 'o', color='steelblue', markersize=10, label='Ball (RK4 quadratic drag)')
    rod_body  = None

# Perturbation moving marker
_pert_label = 'Rod CM (perturbation)' if mode == 'rod' else 'Ball (perturbation)'
pert_dot, = ax.plot([], [], 's', color='firebrick', markersize=8, label=_pert_label)

ax.legend(loc='upper right', fontsize=8)


def init():
    line_rk4_trail.set_data([], [])
    line_pert_trail.set_data([], [])
    pert_dot.set_data([], [])
    artists = [line_rk4_trail, line_pert_trail, pert_dot]
    if rod_body is not None:
        rod_body.set_data([], [])
        artists.append(rod_body)
    if ball_dot is not None:
        ball_dot.set_data([], [])
        artists.append(ball_dot)
    return artists


def update(frame):
    # --- RK4 trail + marker ---
    # Clamp to rk4_landed_at so the marker freezes at y≈0, not underground.
    f_rk4 = min(frame, rk4_landed_at)
    line_rk4_trail.set_data(rk4_x[:f_rk4 + 1], rk4_y[:f_rk4 + 1])

    if rod_body is not None:
        cx, cy = rk4_x[f_rk4], rk4_y[f_rk4]
        theta  = rk4_theta[f_rk4]
        half_L = cfg.ROD_LENGTH / 2.0
        rod_body.set_data(
            [cx - half_L * np.cos(theta), cx + half_L * np.cos(theta)],
            [cy - half_L * np.sin(theta), cy + half_L * np.sin(theta)],
        )

    if ball_dot is not None:
        ball_dot.set_data([rk4_x[f_rk4]], [rk4_y[f_rk4]])

    # --- Perturbation trail + marker ---
    # Clamp to pert_landed_at so the curve freezes at landing, not underground.
    f_pert = min(frame, pert_landed_at)
    line_pert_trail.set_data(pert_x[:f_pert + 1], pert_y[:f_pert + 1])
    pert_dot.set_data([pert_x[f_pert]], [pert_y[f_pert]])

    artists = [line_rk4_trail, line_pert_trail, pert_dot]
    if rod_body  is not None: artists.append(rod_body)
    if ball_dot  is not None: artists.append(ball_dot)
    return artists


ani = animation.FuncAnimation(
    fig, update,
    frames=n_frames,
    init_func=init,
    blit=True,
    interval=cfg.INTERVAL_MS,
)

plt.tight_layout()
plt.show()