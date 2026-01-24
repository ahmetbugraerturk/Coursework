class Drone:
    """
    A base class for all drones.

    Attributes:
        id (str): The unique identifier for the drone.
        max_speed (int): The maximum speed of the drone (km/h).
        current_location (tuple[float, float]): The current location of the drone (latitude, longitude).

    Methods:
        __init__(self, id: str, max_speed: int, current_location: tuple[float, float]):
            Initializes a drone with the given attributes.
        move_to(self, new_location: tuple[float, float]) -> None:
            Moves the drone to the new location.
        get_type(self) -> str:
            Returns the type of the drone.
    """

    def __init__(self, id: str, max_speed: int, current_location: tuple[float, float]):
        """
        Initializes a drone with the given attributes.

        Args:
            id (str): The unique identifier for the drone.
            max_speed (int): The maximum speed of the drone (km/h).
            current_location (tuple[float, float]): The current location of the drone (latitude, longitude).
        """
        self.id = id
        self.max_speed = max_speed
        self.current_location = current_location


    def move_to(self, new_location: tuple[float, float]) -> None:
        """
        Moves the drone to the new location.

        Args:
            new_location (tuple[float, float]): The new location to move the drone to (latitude, longitude).

        Returns:
            None
        """
        self.current_location = new_location


    def get_type(self) -> str:
        """
        Returns the type of the drone.

        Returns:
            str: The type of the drone.
        """
        return "Generic Drone"
