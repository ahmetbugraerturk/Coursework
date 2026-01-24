class Car:
    def __init__(self, model: str, top_speed: float, acceleration: float, handling: int) -> None:
        """
        Initializes a Car object.

        Parameters:
            model (str): Car model.
            top_speed (float): Maximum speed in km/h.
            acceleration (float): Time to reach 100 km/h in seconds.
            handling (int): Handling quality, 1-10.

        Raises:
            TypeError: If model is not a string.
            TypeError: If top_speed is not a float.
            TypeError: If acceleration is not a float.
            TypeError: If handling is not an integer.
            ValueError: If top_speed is not in range 318-360.
            ValueError: If acceleration is not in range [2.4, 2.6].
            ValueError: If handling is not in range 1-10.
        """
        # TODO: Check for type errors
        if not isinstance(model, str):
            raise TypeError("If model is not a string.")
        if not isinstance(top_speed, float):
            raise TypeError("If top_speed is not a float.")
        if not isinstance(acceleration, float):
            raise TypeError("If acceleration is not a float.")
        if not isinstance(handling, int):
            raise TypeError("If handling is not an int.")

        # TODO: Check for value errors
        if top_speed<318 or top_speed>360:
            raise ValueError("If top_speed is not in range 318-360.")
        if acceleration<2.4 or acceleration>2.6:
            raise ValueError("If acceleration is not in range [2.4, 2.6].")
        if handling<1 or handling>10:
            raise ValueError("If handling is not in range 1-10.")


        # TODO: Set instance variables
        self.model = model
        self.top_speed = top_speed
        self.acceleration = acceleration
        self.handling = handling
        

    def add_component(self, component) -> None:
        """
        Adds a component to the car.

        Parameters:
            component (Component): The component to be added.
        """
        # TODO: Apply the component to the car
        component.apply(self)


    def calculate_lap_time(self, track_length: float) -> float:
        """
        Calculates lap time based on car specs and track length.

        Parameters:
            track_length (float): Length of the track in km.

        Returns:
            float: Calculated lap time.
        """
        # TODO: Calculate lap time
        speed_factor = self.top_speed/300
        acceleration_factor = 10/self.acceleration
        handling_factor = self.handling/10
        return track_length/(speed_factor*acceleration_factor*handling_factor)
        
        
        
        
        
        

