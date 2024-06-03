# locator system will contain Point object
# GPS object
# IMU object
from system.gps import GPS
from system.imu import IMU


class Locator:
    """
    Set of functions of the Locator system of the Autonomous vehicle.
    It uses GPS and IMU systems to get current vehicle position.
    """

    def __init__(self):
        """Initialise position. Default set to None."""
        self.position = None
        self.altitude = None
        self.accuracy = None
        self.rotation = None
        self.acceleration = None
        self.velocity = None

    def get_starting_position(self):
        """Get starting position of vehicle using GPU class and assign to position attribute of the Locator."""
        gps = GPS()
        starting_position = gps.get_current_coordinates(task="start")
        self.position = starting_position

        return self.position

    def get_current_position(self):
        """Get current position of vehicle using GPU class and assign to position attribute of the Locator."""
        gps = GPS()
        current_position = gps.get_current_coordinates(task="navigate")
        self.position = current_position

        return self.position

    def get_imu_readings(self):
        """Get readings from IMU."""
        imu = IMU()
        self.acceleration = imu.acceleration
        self.rotation = imu.rotation
        self.velocity = imu.velocity
        return self.acceleration, self.rotation, self.velocity
