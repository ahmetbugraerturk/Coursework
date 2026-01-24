from drone import Drone


class SurveyDrone(Drone):
    """
    A survey drone.

    Attributes:
        camera_quality (str): The quality of the camera.
        survey_data (list): The data collected by the drone.

    Methods:
        __init__(self, id: str, max_speed: int, current_location: tuple[float, float], camera_quality: str):
            Initializes a survey drone with the given attributes.
        scan_area(self, area_coordinates: list) -> None:
            Scans the given area and appends the data to `survey_data`.
    """

    def __init__(self, id: str, max_speed: int, current_location: tuple[float, float], camera_quality: str):
        """
        Initializes a survey drone with the given attributes.

        Args:
            id (str): The unique identifier for the drone.
            max_speed (int): The maximum speed of the drone (km/h).
            current_location (tuple[float, float]): The current location of the drone (latitude, longitude).
            camera_quality (str): The quality of the camera.
        """
        super().__init__(id, max_speed, current_location)
        self.camera_quality = camera_quality
        self.survey_data = []


    def scan_area(self, area_coordinates: list) -> None:
        """
        Scans the given area and appends the data to `survey_data`.

        Args:
            area_coordinates (list): The coordinates of the area to scan.

        Returns:
            None
        """
        self.survey_data += area_coordinates
        print("Survey completed!")


    def get_type(self) -> str:
        """
        Returns the type of the drone.

        Returns:
            str: The type of the drone.
        """
        return "Survey Drone"
