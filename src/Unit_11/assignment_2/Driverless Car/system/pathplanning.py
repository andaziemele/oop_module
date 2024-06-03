import random
from collections import deque

import constants
import util  # import utility class to fulfill required system functions
from system.geometry import Point

from system.objectdetection import ObjectDetector

random.seed(15)


class Planner:
    """Planner class as part of the Path Planning system."""

    def __init__(self):
        self.current_route = deque()  # current route, to support a Queue structure and operations (FiFo)
        self.completed_route = deque(maxlen=10)  # route history, to support a Stack structure and operations (LiFo)
        self.full_route = []  # full route including directions (N, E, S, W), stored as a list of dicts

    @staticmethod
    def search_address(starting_position: Point):
        """Function that simulates an address search."""
        end_position = util.generate_random_distance_point(starting_position)

        return end_position

    def generate_route(self, starting_position: Point, end_position: Point, turns: int = None):
        """Function that simulates directions for the vehicle by creating a list of N random turning points
        and respective waypoint coordinates for each point. Additionally, it simulates "wrong turns" for backtracking, i.e.,
        for a North-facing route, if a vehicle routes W and then back E, that is a back-tracking activity and requires
        accessing the history of the route.

        Params:
            starting_position: Point object of start
            end_position: Point object of end

        Returns:
            route: dictionary of waypoints
        """
        # get direction (N, E, S, W) of the end position.
        direction = util.get_direction(starting_position, end_position)
        print(direction)

        # if else statements based on direction to ensure vehicle does not route backwards, i.e., opposite direction
        # if end point is North-facing, vehicle will not generate S directions

        if turns:  # if rerouting
            k = turns
        else:  # usual generation of 100 waypoints
            k = 100

        # use random choices with weights to generate turns
        if direction == 'N':
            turning_points = random.choices(['W', 'E', 'N'], [5, 5, 15],
                                            k=k)  # higher weight placed on vehicle moving towards needed direction
        elif direction == 'S':
            turning_points = random.choices(['W', 'E', 'S'], [5, 5, 15], k=k)  # same as above
        elif direction == 'W':
            turning_points = random.choices(['N', 'S', 'W'], [5, 5, 15], k=k)  # same as above
        elif direction == 'E':
            turning_points = random.choices(['N', 'S', 'E'], [5, 5, 15], k=k)  # same as above
        else:
            raise Exception("Invalid direction!")

        # print(turning_points)
        # coordinate mapper to adjust lat/long based on turning point list
        modifiers = constants.COORD_MODIFIERS_10CM  # import constants

        # initialise starting waypoint latitude and longitude
        waypoint_lat = starting_position.lat
        waypoint_lon = starting_position.lon

        # append starting position/first waypoint to current route
        self.current_route.append(Point(waypoint_lat, waypoint_lon))

        # loop through each turning point and start generating waypoints based on modifier dict
        for turn in turning_points:
            turn_distance = modifiers.get(turn, None)  # get respective lat lon modifier based on direction
            waypoint_lat, waypoint_lon = waypoint_lat + turn_distance[0] * 100, \
                                         waypoint_lon + turn_distance[
                                             1] * 100  # modify lat lon, increase modifier 100 times to convert to 10m
            self.current_route.append(Point(waypoint_lat,
                                            waypoint_lon))  # append Point objects to current route
            self.full_route.append({"direction": turn,
                                    "waypoint": Point(waypoint_lat, waypoint_lon),
                                    "distance": 0.01})  # in km

        print("Distance to final destination:", round(starting_position.distance(self.current_route[-1]), 2), "kms")
        # return waypoints
        return self.current_route

    def follow_route(self):
        """Function that simulates the vehicle following the route. Function updates the current_route queue structure by
        removing items using popleft() as it loops through the waypoints. Where it faces opposing directions, i.e.,
        West (W) and East (E), it fetches the latest history from saved history points. Additionally, per each movement
        a set of objects are detected.
        """
        print("Starting route...")
        detector = ObjectDetector()
        counter = 0
        for waypoint in self.full_route:
            print("Routing...")
            detected_objects = detector.detect_objects(waypoint["waypoint"])
            for obj in detected_objects:  # sequential search
                if obj["threat_level"] == "high":
                    print("Avoiding collision...")  # in a future development/real life scenario, move vehicle by cms
            self.completed_route.append(self.current_route.popleft())
            try:  # this catches scenarios where the route generated caused the vehicle to take the wrong turn
                if (self.current_route[0].lat, self.current_route[0].lon) == (  # using current live position
                        self.completed_route[-2].lat,
                        self.completed_route[-2].lon):  # using the stack structure as history to catch wrong turn
                    print("Vehicle took the wrong turn, backtracking...")
            except:
                pass
            # simulate route recalculation at turn 50
            if counter == 50:
                print("Re-routing......")
                print(len(self.current_route), "turns remaining.")
                # recalculates route using the same logic, but for remaining turns, which is the length of
                # the up-to-date current_route queue data structure
                self.current_route = self.recalculate_route(waypoint["waypoint"], self.current_route[-1], len(self.current_route))
            counter += 1

    def backtrack_route(self, previous_position):
        """Function that would simulate backtracking when opposing directions faced (W, E) or (N, S).
        In a future development/real world scenario, the vehicle would use its history to trace back steps and
        continue its journey. CURRENTLY EMPTY.
        """
        pass

    def recalculate_route(self, current_position: Point, end_position: Point, turns: int):
        """Function that simulates recalculation of the route.
        """
        new_route = self.generate_route(current_position, end_position, turns)
        self.current_route = new_route

        return self.current_route
