from drone import Drone


class DroneHub:
    """
    A drone hub.

    Attributes:
        name (str): The name of the drone hub.
        drones (list): A list of drones in the hub.

    Methods:
        __init__(self, name: str): Initializes the drone hub with the given name.
        add_drone(self, drone: Drone): Adds a drone to the hub.
        list_drones(self): Prints the list of drones in the hub.
        relocate_all_drones(self, new_location: tuple[float, float]): Relocates all drones to the new location.
    """

    def __init__(self, name: str):
        """
        Initializes the drone hub with the given name.

        Args:
            name (str): The name of the drone hub.
        """
        self.name = name
        self.drones = []


    def add_drone(self, drone: Drone) -> None:
        """
        Adds a drone to the hub.

        Args:
            drone (Drone): The drone to add.
        """
        self.drones.append(drone)


    def list_drones(self) -> None:
        """
        Prints the list of drones in the hub.
        """
        for d in self.drones:
            print(f"Drone ID: {d.id}, Type: {d.get_type()}")


    def relocate_all_drones(self, new_location: tuple[float, float]) -> None:
        """
        Relocates all drones to the new location.

        Args:
            new_location (tuple[float, float]): The new location to move the drones to (latitude, longitude).
        """
        for d in self.drones:
            d.move_to(new_location)
