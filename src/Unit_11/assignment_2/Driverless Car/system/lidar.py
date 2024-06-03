import util
from system.geometry import Point


class LiDAR:
    """Class that simulates inputs from a LiDAR sensor for getting distance of an object."""

    def __init__(self):
        """Initialise status attribute.
        """
        self.status = None

    @staticmethod
    def get_object_position(current_position: Point):
        """Function for fetching distance of detected objects.
        Args:
            current_position: current vehicle position

        Returns:
            object_position: detected latitude and longitude of object
        """
        object_position = util.generate_random_coordinates(task="object_detection", current_position=current_position)
        return object_position

    @staticmethod
    def get_object_distance(vehicle_position: Point, object_position: Point):
        """Function for fetching distance of detected objects.
        Args:
            vehicle_position: current vehicle position
            object_position:

        Returns:
            distance: distance between two points (in km)
        """
        distance = vehicle_position.distance(object_position)

        return distance
