// Ahmet Buğra Ertürk, 0086877
#include <stdio.h>
#include <stdlib.h>

// --- SETTINGS ---
#define MAX_FUEL 3
#define MAX_TURNS 10

// DIRECTIONS
int DRONE_DIRS[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
int PIRATE_DIRS[4][2] = { {-1, 1}, {1, 1}, {1, -1}, {-1, -1} };

// --- STRUCTS ---
typedef enum { EMPT, WALL_FARM, WALL_HIDEOUT } TerrainType;
typedef enum { NONE, DRONE, PIRATE } UnitType;

typedef struct {
    UnitType type;
    int dy, dx;         
    int fuel;
    int has_moved;      // Flag for turn processing
} Ship;

typedef struct {
    TerrainType terrain;
    int has_crystal;
    Ship* ship;
} Cell;

// GLOBALS
int HEIGHT = 0;
int WIDTH = 0;

// --- PROTOTYPES ---

Cell** create_grid();
void free_grid(Cell** grid);
Cell** load_map(const char* filename);
void print_grid(Cell** grid, int turn);

// Simulation Functions

void run_turn(Cell** current_grid, int turn_counter);
void spawn_drones(Cell** current_grid, int turn_counter);
void spawn_pirates(Cell** current_grid, int turn_counter);
void move_drones_phase(Cell** current_grid, Cell** next_grid);
void move_pirates_phase(Cell** current_grid, Cell** next_grid);
void update_grid(Cell** current_grid, Cell** next_grid);

void handle_entity_move(Ship* s, int r, int c, int new_r, int new_c, Cell** current_grid, Cell** next_grid);

// --- MAIN ---
int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <map_file>\n", argv[0]);
        return 1;
    }

    Cell** grid = load_map(argv[1]);
    if (!grid) {
        printf("Error loading map.\n");
        return 1;
    }

    print_grid(grid, 0);

    for (int t = 1; t <= MAX_TURNS; t++) {
        run_turn(grid, t);
        print_grid(grid, t);
    }

    free_grid(grid);
    return 0;
}

// --- CORE SIMULATION ---

void run_turn(Cell** current_grid, int turn_counter) {
    // 1. Prepare Next Grid
    Cell** next_grid = create_grid();

    // 2. Spawn Phase
    spawn_drones(current_grid, turn_counter);
    spawn_pirates(current_grid, turn_counter);
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            next_grid[i][j]=current_grid[i][j];
        }
    }

    // 3. Drone Movement Phase 
    move_drones_phase(current_grid, next_grid);

    // 4. Pirate Movement Phase 
    move_pirates_phase(current_grid, next_grid);

    // 5. Update Phase
    update_grid(current_grid, next_grid);

    // Clean up temporary structure
    free_grid(next_grid);
}

// --- MOVEMENT PHASES ---

void move_drones_phase(Cell** current_grid, Cell** next_grid) {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (current_grid[i][j].ship == NULL) continue;
            else if (current_grid[i][j].ship->type == DRONE && current_grid[i][j].ship->has_moved == 0){   
                int new_i = i-current_grid[i][j].ship->dy;
                int new_j = j+current_grid[i][j].ship->dx;
                if((new_i>=HEIGHT || new_i<0 || new_j>=WIDTH || new_j<0) || current_grid[new_i][new_j].terrain == WALL_FARM || (next_grid[new_i][new_j].ship)){
                    next_grid[i][j].ship->dx = -next_grid[i][j].ship->dx;
                    next_grid[i][j].ship->dy = -next_grid[i][j].ship->dy;
                    new_i = i-next_grid[i][j].ship->dy;
                    new_j = j+next_grid[i][j].ship->dx;
                }
                if((new_i>=HEIGHT || new_i<0 || new_j>=WIDTH || new_j<0) || current_grid[new_i][new_j].terrain == WALL_FARM || (next_grid[new_i][new_j].ship)){
                    next_grid[i][j].ship->dx = -next_grid[i][j].ship->dx;
                    next_grid[i][j].ship->dy = -next_grid[i][j].ship->dy;
                    next_grid[i][j].ship->fuel--;
                    if (next_grid[i][j].ship->fuel==0){
                        next_grid[i][j].ship=NULL;
                    }
                    if (current_grid[i][j].has_crystal == 1){
                        next_grid[i][j].ship->fuel = MAX_FUEL;
                        next_grid[i][j].has_crystal = 0;
                    }
                    continue;
                }
                else if (current_grid[new_i][new_j].terrain == WALL_HIDEOUT){
                    next_grid[i][j].ship = NULL;
                }
                else if (current_grid[new_i][new_j].has_crystal == 1){
                    handle_entity_move(next_grid[i][j].ship, i, j, new_i, new_j, current_grid, next_grid);
                    next_grid[new_i][new_j].ship->fuel = MAX_FUEL;
                    next_grid[new_i][new_j].has_crystal = 0;
                }
                else {
                    handle_entity_move(next_grid[i][j].ship, i, j, new_i, new_j, current_grid, next_grid);
                    if (next_grid[new_i][new_j].ship->fuel==0){
                        next_grid[new_i][new_j].ship=NULL;
                    }
                }
            }
            else if (current_grid[i][j].ship->type == DRONE && current_grid[i][j].ship->has_moved == 1) {
                next_grid[i][j].ship = current_grid[i][j].ship;
                next_grid[i][j].ship->has_moved = 0;
            }
        }
    }
}

void move_pirates_phase(Cell** current_grid, Cell** next_grid) {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (current_grid[i][j].ship == NULL) continue;
            else if (current_grid[i][j].ship->type == PIRATE && current_grid[i][j].ship->has_moved == 0){   
                int new_i = i-current_grid[i][j].ship->dy;
                int new_j = j+current_grid[i][j].ship->dx;
                int isT = 0;
                if(new_i>=HEIGHT || new_i<0 || new_j>=WIDTH || new_j<0){
                    if (new_i>=HEIGHT || new_i<0) {next_grid[i][j].ship->dy = -next_grid[i][j].ship->dy; isT = 1;}
                    if (new_j>=WIDTH || new_j<0) {next_grid[i][j].ship->dx = -next_grid[i][j].ship->dx; isT = -1;}
                    new_i = i-next_grid[i][j].ship->dy;
                    new_j = j+next_grid[i][j].ship->dx;
                }
                else if(current_grid[new_i][new_j].terrain == WALL_HIDEOUT || (next_grid[new_i][new_j].ship && next_grid[new_i][new_j].ship->type == PIRATE)){
                    next_grid[i][j].ship->dx = -next_grid[i][j].ship->dx;
                    next_grid[i][j].ship->dy = -next_grid[i][j].ship->dy;
                    new_i = i-next_grid[i][j].ship->dy;
                    new_j = j+next_grid[i][j].ship->dx;
                }
                if((new_i>=HEIGHT || new_i<0 || new_j>=WIDTH || new_j<0) || current_grid[new_i][new_j].terrain == WALL_HIDEOUT || (next_grid[new_i][new_j].ship && next_grid[new_i][new_j].ship->type == PIRATE)){
                    if (isT == 1) next_grid[i][j].ship->dy = -next_grid[i][j].ship->dy;
                    else if (isT == -1) next_grid[i][j].ship->dx = -next_grid[i][j].ship->dx;
                    else if (isT == 0) {
                        next_grid[i][j].ship->dx = -next_grid[i][j].ship->dx;
                        next_grid[i][j].ship->dy = -next_grid[i][j].ship->dy;
                    }
                    next_grid[i][j].ship->fuel--;
                    if (next_grid[i][j].ship->fuel==0){
                        next_grid[i][j].ship=NULL;
                    }
                    if (current_grid[i][j].has_crystal == 1){
                        next_grid[i][j].ship->fuel = MAX_FUEL;
                        next_grid[i][j].has_crystal = 0;
                    }
                    continue;
                }
                else if (current_grid[new_i][new_j].terrain == WALL_FARM){
                    next_grid[i][j].ship = NULL;
                }
                else if (current_grid[new_i][new_j].has_crystal == 1 || (next_grid[new_i][new_j].ship && next_grid[new_i][new_j].ship->type == DRONE)){
                    handle_entity_move(next_grid[i][j].ship, i, j, new_i, new_j, current_grid, next_grid);
                    next_grid[new_i][new_j].ship->fuel = MAX_FUEL;
                    next_grid[new_i][new_j].has_crystal = 0;
                }
                else {
                    handle_entity_move(next_grid[i][j].ship, i, j, new_i, new_j, current_grid, next_grid);
                    if (next_grid[new_i][new_j].ship->fuel==0){
                        next_grid[new_i][new_j].ship=NULL;
                    }
                }
            }
            else if (current_grid[i][j].ship->type == PIRATE && current_grid[i][j].ship->has_moved == 1) {
                next_grid[i][j].ship = current_grid[i][j].ship;
                next_grid[i][j].ship->has_moved = 0;
            }
        }
    }
}

// --- HELPER FUNCTION: THE LOGIC CORE ---

void handle_entity_move(Ship* s, int r, int c, int new_r, int new_c, Cell** current_grid, Cell** next_grid) {
    next_grid[r][c].ship=NULL;
    next_grid[new_r][new_c].ship=current_grid[r][c].ship;
    next_grid[new_r][new_c].ship->fuel--;
}

// --- SPAWN FUNCTIONS ---

void spawn_drones(Cell** current_grid, int turn_counter) {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (current_grid[i][j].terrain == WALL_FARM){
                if (i-DRONE_DIRS[turn_counter%4][1]<HEIGHT && i-DRONE_DIRS[turn_counter%4][1]>=0 && j+DRONE_DIRS[turn_counter%4][0]<WIDTH && j+DRONE_DIRS[turn_counter%4][0]>=0){
                    if (current_grid[i-DRONE_DIRS[turn_counter%4][1]][j+DRONE_DIRS[turn_counter%4][0]].ship!=NULL) continue;
                    Ship* ship = malloc(sizeof(Ship));
                    ship->fuel=MAX_FUEL;
                    ship->has_moved = 1;
                    ship->type = DRONE;
                    ship->dx = DRONE_DIRS[turn_counter%4][0];
                    ship->dy = DRONE_DIRS[turn_counter%4][1];
                    current_grid[i-DRONE_DIRS[turn_counter%4][1]][j+DRONE_DIRS[turn_counter%4][0]].ship = ship;
                }
            }
        }
    }
}

void spawn_pirates(Cell** current_grid, int turn_counter) {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (current_grid[i][j].terrain == WALL_HIDEOUT){
                if (i-PIRATE_DIRS[turn_counter%4][1]<HEIGHT && i-PIRATE_DIRS[turn_counter%4][1]>=0 && j+PIRATE_DIRS[turn_counter%4][0]<WIDTH && j+PIRATE_DIRS[turn_counter%4][0]>=0){
                    if (current_grid[i-PIRATE_DIRS[turn_counter%4][1]][j+PIRATE_DIRS[turn_counter%4][0]].ship!=NULL) continue;
                    Ship* ship = malloc(sizeof(Ship));
                    ship->fuel=MAX_FUEL;
                    ship->has_moved = 1;
                    ship->type = PIRATE;
                    ship->dx = PIRATE_DIRS[turn_counter%4][0];
                    ship->dy = PIRATE_DIRS[turn_counter%4][1];
                    current_grid[i-PIRATE_DIRS[turn_counter%4][1]][j+PIRATE_DIRS[turn_counter%4][0]].ship = ship;
                }
            }
        }
    }
}

// --- UPDATE & UTILS ---

void update_grid(Cell** current_grid, Cell** next_grid) {
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            current_grid[i][j]=next_grid[i][j];
        }
    }
}

Cell** create_grid() {
    Cell** grid = malloc(sizeof(Cell*)*HEIGHT);
    if (grid == NULL) {
        return NULL;
    }
    for (int i = 0; i < HEIGHT; i++) {
        grid[i] = malloc(sizeof(Cell)*WIDTH);
        if (grid[i] == NULL) {
            return NULL; 
        }
    }
    return grid;
}

void free_grid(Cell** grid) {
    for (int i = 0; i < HEIGHT; i++) {
        free(grid[i]);
    }
    free(grid);
}

Cell** load_map(const char* filename) {
    FILE* f = fopen(filename, "r");
    if (!f) return NULL;
    if (fscanf(f, "%d %d", &HEIGHT, &WIDTH) != 2) return NULL;
    Cell** grid = create_grid();
    char buf[1024];
    for (int i = 0; i < HEIGHT; i++) {
        fscanf(f, "%s", buf);
        for (int j = 0; j < WIDTH; j++) {
            if (buf[j] == 'F') grid[i][j].terrain = WALL_FARM;
            else if (buf[j] == 'H' || buf[j] == 'B') grid[i][j].terrain = WALL_HIDEOUT;
            else if (buf[j] == 'C') grid[i][j].has_crystal = 1;
        }
    }
    fclose(f);
    return grid;
}

void print_grid(Cell** grid, int turn) {
    printf("--- STEP %d ---\n", turn);
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            if (grid[i][j].ship) printf(grid[i][j].ship->type == DRONE ? "D" : "P");
            else if (grid[i][j].terrain == WALL_FARM) printf("F");
            else if (grid[i][j].terrain == WALL_HIDEOUT) printf("H");
            else if (grid[i][j].has_crystal) printf("C");
            else printf("-");
        }
        printf("\n");
    }
    printf("\n");
}