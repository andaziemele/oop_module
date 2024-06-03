# storing of utility and helper functions to support the simulation of an autonomous vehicle
# existing research:
# https://www.sciencedirect.com/science/article/pii/S2665963822001129#:~:text=RanCoord%20is%20an%20open%2Dsource,name%2Faddress%20through%20its%20geocoding.
# 10cm position: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8433815/#:~:text=While%20a%20high%2Dquality%20localization,at%20the%20same%20confidence%20level.
import random
from math import radians, cos, sin, asin, atan2, pi, degrees

from system.geometry import Point

import constants

random.seed(15)


def generate_random_coordinates(task: str, current_position: Point = None, full_route: dict = None):
    """Helper function that generates random Latitude, Longitude values to precision of 10 cm.
    start Boolean param defines whether it is the vehicle starting position or next position.

    Args:
        task: type of task for which to generate random coordinates ("start" or "object_detection")
        current_position: current latitude longitude as Point (optional, default None)
        full_route: full route with directions from the Planner class

    Returns:
        random_point: Point object with random values
    """
    # depending on the task, different coordinate generating strategies exist
    if task == "start":  # if vehicle starting position required, can be any point, anywhere
        random_latitude = round(random.uniform(constants.VALID_LATITUDE_RANGE[1],
                                               constants.VALID_LATITUDE_RANGE[0]), 8)
        random_longitude = round(random.uniform(constants.VALID_LONGITUDE_RANGE[1],
                                                constants.VALID_LONGITUDE_RANGE[0]), 8)
        random_point = Point(random_latitude, random_longitude)
    elif task == "object_detection":  # get a random object distance from current reference point
        random_radius = round(random.uniform(0, 0.005), 8)  # generate random radius between 0 and 5 metres (0.005 km)
        random_point = generate_random_distance_point(reference_point=current_position, max_radius=random_radius)
    else:
        raise Exception("Invalid coordinate generation task. Must be 'start', 'navigate' or 'object_detection'.")

    return random_point


def generate_random_distance_point(reference_point: Point, max_radius: float = 1.0):
    """Helper function that generates a random coordinate position based on distance input.
    For purposes of this exercise, the random start and end positions are exactly 1km away from each other.
    Code adapted based on following source: http://www.movable-type.co.uk/scripts/latlong.html

    Args:
        reference_point: Point object of reference (either start or current vehicle position)
        max_radius: float of 1.0 (equalling 1000 metres/1 kilometre)

    Returns:
        Point objects of start and end position within 1km of each other.
    """
    # convert lat lon to radians
    lat1 = radians(reference_point.lat)
    lon1 = radians(reference_point.lon)

    # convert bearing to radians
    random_bearing = radians(random.randint(constants.VALID_BEARING_RANGE[0],
                                            constants.VALID_BEARING_RANGE[1]))  # generate a random bearing (0, 360)

    # get angle distance of radius and earth's distance (in kms)
    ang_distance = max_radius / constants.EARTH_RADIUS_KM  # max radius in KM

    # calculate new latitude
    lat2 = asin((sin(lat1) * cos(ang_distance)) + (cos(lat1) * sin(ang_distance) * cos(random_bearing)))

    # calculate new longitude
    lon2 = lon1 + atan2(sin(random_bearing) * sin(ang_distance) * cos(lat1),
                        cos(ang_distance) - sin(lat1) * sin(lat2))

    # convert lat lon to degrees
    end_lat = degrees(lat2)
    end_lon = degrees(lon2)

    # create Point object of new coords
    end_point = Point(end_lat, end_lon)

    return end_point


def get_direction(start_point: Point, end_point: Point):
    """Function for getting the direction of the end coordinate.
    For sake of reducing complexity, SW, NE, NW and SE directions have been removed.
    
    Args:
        start_point: start coordinate
        end_point: end coordinate
        
    Returns:
        direction: direction of end destination (N, E, S or W)
    
    """
    # separate lat and lon attributes of start and end points
    end_lat = end_point.lat
    end_lon = end_point.lon
    start_lat = start_point.lat
    start_lon = start_point.lon

    # get distance in radians
    d_radians = atan2((end_lon - start_lon), (end_lat - start_lat))

    # get angle of direction
    compass_measure = d_radians * (180 / pi)

    # list of directions, with an additional N direction to account for both 0 and 360 degrees
    coords = ["N", "E", "S", "W", "N"]

    # get index of direction from list, 90 degrees clockwise starting from N and ending with N
    coord_index = round(compass_measure / 90)

    # additional account for N
    if coord_index < 0:
        coord_index = coord_index + 4

    # get final direction based on index
    direction = coords[coord_index]

    return direction


def generate_random_objects(num_objects: int):
    """Simulates random objects and their attributes for object detection system, assuming within one frame.
    Returns:
        object_class: one of the following IDs [0, 1, 2, 3] that will then get mapped to respective object labels
        box: random set of four numbers representing a bounding box
        confidence: 0 to 100, with 0 being perfect match
    """
    object_ids = [0, 1, 2, 3]  # assuming vehicle is 0, road object 1, pedestrian 2 and cyclist 3
    detected_ids = random.choices(object_ids, weights=[8, 10, 4, 6],
                                  k=num_objects)  # generate n objects, and more weight assigned to vehicles, road objects

    # a list of dicts, storing individual object information
    detected_objects = []
    for obj_id in detected_ids:
        obj_dict = {"id": obj_id,
                    "box": generate_random_bounding_box(),
                    "confidence": generate_random_confidence_score()}
        detected_objects.append(obj_dict)

    return detected_objects


def generate_random_bounding_box():
    """Generates random coordinates of a bounding box for detected objects.
    Returns:
        box: a list of four values, each representing a box
    """
    bounds = [100, 100, 1000, 1000]  # x0, y0, x1, y1, randomly chosen

    # generate list of four random integers and fetch corner values of each
    b = [random.randint(0, b) for b in bounds]
    left = min(b[0], b[2])
    upper = min(b[1], b[3])
    right = max(b[0], b[2])
    lower = max(b[1], b[3])

    return [left, upper, right, lower]


def generate_random_confidence_score():
    """Generates random confidence score based on a normal distribution.
    Returns:
        confidence: 0 to 100, with 0 being perfect match
    """
    confidence = random.normalvariate(5, 3)  # mean of 5, standard deviation of 3
    # negative values not permitted, turn into a positive number and closer to 0
    if confidence < 0:
        confidence = confidence * -0.1

    return confidence
