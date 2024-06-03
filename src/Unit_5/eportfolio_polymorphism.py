#
# Polymorphism implementation.
#

class Sensor:
    """Main sensor class for defining sensors in the system."""
    def detect_objects(self):
        """Abstract sensor class does not do anything, child classes implement the methods."""
        raise NotImplementedError("This method should be overridden by subclasses.")


class Radar(Sensor):
    """Class for Radar sensor system."""
    def detect_objects(self):
        """Detection method."""
        print("Detecting objects using Radar...")


class LiDAR(Sensor):
    """Class for LiDAR sensor system."""
    def detect_objects(self):
        """Detection method."""
        print("Detecting objects using LiDAR...")


class Camera(Sensor):
    """Class for Camera sensor system."""
    def detect_objects(self):
        """Detection method."""
        print("Detecting objects using Camera...")


# Create vehicle instances
if __name__ == '__main__':
    # create instances of each sensor object
    radar = Radar()
    lidar = LiDAR()
    camera = Camera()

    # create list of sensors
    sensors = [radar, lidar, camera]

    # loop through the sensors and call the detect_objects method
    for sensor in sensors:
        sensor.detect_objects()
