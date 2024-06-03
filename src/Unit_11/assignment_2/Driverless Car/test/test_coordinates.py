# Coordinate tests

import unittest

import util
import constants

from system.geometry import Point


def is_within_range(lat, lon):
    """
    Check if the latitude and longitude are within the valid range.
    Latitude must be between -90 and 90 degrees.
    Longitude must be between -180 and 180 degrees.
    """
    return constants.VALID_LATITUDE_RANGE[1] <= lat <= constants.VALID_LATITUDE_RANGE[0] and \
        constants.VALID_LONGITUDE_RANGE[1] <= lon <= constants.VALID_LONGITUDE_RANGE[0]


class TestCoordinateGeneration(unittest.TestCase):
    def test_generate_start_coordinates(self):
        point = util.generate_random_coordinates(task="start")
        self.assertTrue(is_within_range(point.lat, point.lon), f"Coordinates ({point.lat}, {point.lon}) are out of range")

    def test_valid_end_coordinates(self):
        start_lat = 52.2296756
        start_lon = 21.0122287
        point = Point(start_lat, start_lon)

        point = util.generate_random_coordinates(task="object_detection", current_position=point)

        # Check if the end coordinates are within valid ranges
        self.assertTrue(is_within_range(point.lat, point.lon), f"Coordinates ({point.lat}, {point.lon}) are out of range")


class TestPointObject(unittest.TestCase):
    def test_valid_latitude_range(self):
        # Valid latitude range: -90 to 90
        valid_point = Point(45.5, -122.7)
        self.assertTrue(constants.VALID_LATITUDE_RANGE[1] <= valid_point.lat <= constants.VALID_LATITUDE_RANGE[0])

        invalid_point_1 = Point(91.0, -122.7)
        self.assertFalse(constants.VALID_LATITUDE_RANGE[1] <= invalid_point_1.lat <= constants.VALID_LATITUDE_RANGE[0])

        invalid_point_2 = Point(-91.0, -122.7)
        self.assertFalse(constants.VALID_LATITUDE_RANGE[1] <= invalid_point_2.lat <= constants.VALID_LATITUDE_RANGE[0])

    def test_valid_longitude_range(self):
        # Valid longitude range: -180 to 180
        valid_point = Point(45.5, -122.7)
        self.assertTrue(constants.VALID_LONGITUDE_RANGE[1] <= valid_point.lon <= constants.VALID_LONGITUDE_RANGE[0])

        invalid_point_1 = Point(45.5, 181.0)
        self.assertFalse(constants.VALID_LONGITUDE_RANGE[1] <= invalid_point_1.lon <= constants.VALID_LONGITUDE_RANGE[0])

        invalid_point_2 = Point(45.5, -181.0)
        self.assertFalse(constants.VALID_LONGITUDE_RANGE[1] <= invalid_point_2.lon <= constants.VALID_LONGITUDE_RANGE[0])