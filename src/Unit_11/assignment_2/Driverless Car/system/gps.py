import util
from system.geometry import Point


class GPS:
    """GPS class that simulates fetching of current coordinates."""
    def __init__(self):
        """Initialise current position and other GPS-related attributes. Set to None."""
        self.current_position = None
        self.altitude = None
        self.speed = None
        self.accuracy = None

    def get_current_coordinates(self, task: str):
        """Function for getting current Latitude, Longitude position of the vehicle.
        Tasks associated with GPS are getting the start of the vehicle, and the navigation positions.
        Args:
            task: task indicating coordinate generation strategy ("start")
        """
        current_coordinates = util.generate_random_coordinates(task)
        self.current_position = current_coordinates

        return self.current_position




