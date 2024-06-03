# Module for storing constant values

VALID_LATITUDE_RANGE = (90, -90)  # in degrees
VALID_LONGITUDE_RANGE = (180, -180)  # in degrees
VALID_BEARING_RANGE = (0, 359)  # in degrees
EARTH_RADIUS_KM = 6371.0  # in kilometres
COORD_MODIFIERS_10CM = {"W": (0, -0.000000899),  # change in longitude for 10cm, bearing of 270 degrees
                        "E": (0, 0.0000008991),  # change in longitude for 10cm, bearing of 90 degrees
                        "S": (-0.0000008991, 0),  # change in latitude for 10cm, bearing of 180 degrees
                        "N": (0.0000008991, 0)}  # change in latitude for 10cm, bearing of 0 degrees
