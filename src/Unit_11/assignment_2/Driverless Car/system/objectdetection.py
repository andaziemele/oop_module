from system.geometry import Point
from system.lidar import LiDAR

import util


class ObjectDetector:
    """Object Detector class, that simulates the output of a Computer Vision model."""

    def __init__(self):
        """Initialising Object detector path with an empty model path attribute and a list of detected objects."""
        self.model_path = None
        self.objects = []

    def detect_objects(self, current_position):
        """Function that simulates object detection and location.
        Detection outputs are aligned closely to the OpenCV toolkit. Location provides randomly generated coordinates.
        Source: https://docs.opencv.org/4.x/index.html

        Returns:
            self.objects: dict with object attributes
        """
        lidar = LiDAR()
        objects = util.generate_random_objects(20)
        # update object dictionary with new attributes - position, distance and threat level
        for obj in objects:
            obj_position = lidar.get_object_position(current_position)
            obj_distance = lidar.get_object_distance(current_position, obj_position)
            obj.update({"position": obj_position,
                        "distance": obj_distance})
            obj.update({"threat_level": "high" if (obj["id"] == 2) | (obj["distance"] < 0.0005) else "low"})  # if object a pedestrian, or any object closer than 50cms, high

        self.objects = objects

        return self.objects


class DetectedObject:
    """Object class for storing and retrieving detected object attributes."""

    def __init__(self):
        self.position = Point()
        self.confidence = None
        self.object_class = None
        self.box = None
        self.distance = None
        self.threat_level = None

    def get_position(self):
        """Function to simulate latitude longitude position of a detected object."""


class VehicleObject(DetectedObject):
    """Class for storing child Vehicle object of DetectedObject class."""
    pass


class BicycleObject(DetectedObject):
    """Class for storing child Bicycle object of DetectedObject class."""
    pass


class PedestrianObject(DetectedObject):
    """Class for storing child Pedestrian object of DetectedObject class."""
    pass


class RoadObject(DetectedObject):
    """Class for storing child Road object of DetectedObject class."""
    pass
