from car import Car


class DRSCar(Car):
    def __init__(self, model: str, top_speed: float, acceleration: float, handling: int) -> None:
        """
        Initializes a DRSCar object.

        Parameters:
            model (str): Car model.
            top_speed (float): Maximum speed in km/h.
            acceleration (float): Time to reach 100 km/h in seconds.
            handling (int): Handling quality, 1-10.
        """
        # TODO: Call the parent class constructor with the given arguments.
        super().__init__(model, top_speed, acceleration, handling)
        self.model = model
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.handling = handling

        # TODO: Initialize a new instance variable called drs_active and set it to False.
        self.drs_active = False

    def activate_drs(self) -> None:
        """
        Activates DRS system.
        """
        # TODO: Set drs_active to True.
        self.drs_active = True

    def deactivate_drs(self) -> None:
        """
        Deactivates DRS system.
        """
        # TODO: Set drs_active to False.
        self.drs_active = False

    def calculate_lap_time(self, track_length: float) -> float:
        """
        Calculates lap time considering if DRS is active. DRS will improve the car's speed.

        Parameters:
            track_length (float): Length of the track in km.

        Returns:
            float: Calculated lap time.
        """
        # TODO: Implement the formula considering the DRS system.
        speed_factor = self.top_speed/300
        acceleration_factor = 10/self.acceleration
        handling_factor = self.handling/10
        
        if self.drs_active:
            return track_length/(1.07 * speed_factor*acceleration_factor*handling_factor)
        else:
            return track_length/(speed_factor*acceleration_factor*handling_factor)
        
