from math import radians, cos, sin, asin, sqrt
import constants

class Point:
    """Point object for storing x and y (Latitude and Longitude) coordinates."""

    def __init__(self, lat, lon):
        """Initialise Point object.
        Args:
            lat: latitude
            lon: longitude
        """
        self.lat = lat
        self.lon = lon

    def distance(self, end_point):
        """Function that generates haversine distance in millimetres (mms) between two Points.
        This assumes the Earth is a sphere, rather than an Ellipsoid, which is not representative of the
        real world, but is applicable for the purposes of this exercise.
        Source:
        Raspberry Pi Foundation (n.d.) Finding the distance between two points on the Earth. Raspberry Pi Foundation.
        Available from: https://projects.raspberrypi.org/en/projects/fetching-the-weather/6 [Accessed 19 May 2024]

        Args:
            end_point: second coordinate between which to measure distance

        Returns:
            Distance in kms
        """
        start_lon = radians(self.lon)  # longitude value of start coordinate
        start_lat = radians(self.lat)  # latitude value of start coordinate
        end_lon = radians(end_point.lon)  # longitude value of end coordinate
        end_lat = radians(end_point.lat)  # latitude value of end coordinate

        d_lon = end_lon - start_lon  # get difference between end and start longitude value
        d_lat = end_lat - start_lat  # get difference between end and start latitude values

        # calculate distance between Point A to Point B
        a = sin(d_lat / 2) ** 2 + cos(start_lat) * cos(end_lat) * sin(d_lon / 2) ** 2
        distance = 2 * asin(sqrt(a)) * constants.EARTH_RADIUS_KM  # 6371 is the radius of the Earth

        return distance
