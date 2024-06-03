# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import abc
from abc import ABC

from system.locator import Locator
from system.pathplanning import Planner


# define abstract class for Vehicle Interface
class VehicleInterface(object):
    _instance = None

    @abc.abstractmethod
    def __init__(self):
        """Message to direct user to create an instance of the vehicle."""
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance

    @abc.abstractmethod
    def start(self):
        """Starting a vehicle assigns bool True (ON) for engine, and bool False (OFF) for moving state."""
        pass

    @abc.abstractmethod
    def stop(self):
        """Stopping a vehicle assigns bool False (OFF) for engine, and bool False (OFF) for moving state."""
        pass

    @abc.abstractmethod
    def drive(self):
        """Vehicle in a driving state assigns bool True (ON) for engine, and bool True (ON) for moving state."""
        pass


class Vehicle(VehicleInterface, ABC):
    """Vehicle class. Captures and enables updating of engine and moving state."""
    engine_state = False
    moving_state = False

    @classmethod
    def start(cls):
        """Starting a vehicle assigns bool True (ON) for engine, and bool False (OFF) for moving state."""
        cls.engine_state = True
        cls.moving_state = False
        print(f"Engine started: {cls.engine_state}, Moving: {cls.moving_state}")

    @classmethod
    def stop(cls):
        """Stopping a vehicle assigns bool False (OFF) for engine, and bool False (OFF) for moving state."""
        cls.engine_state = False
        cls.moving_state = False
        print(f"Engine started: {cls.engine_state}, Moving: {cls.moving_state}")

    @classmethod
    def drive(cls):
        """Vehicle in a driving state assigns bool True (ON) for engine, and bool True (ON) for moving state."""
        cls.engine_state = True
        cls.moving_state = True
        print(f"Engine started: {cls.engine_state}, Moving: {cls.moving_state}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # test/run flow of the vehicle
    # set random seed as 15
    random.seed(15)
    print("Welcome to your autonomous vehicle.")
    # instantiating required classes, vehicle, planner and locator
    vehicle = Vehicle.instance()
    planner = Planner()
    locator = Locator()
    # update vehicle status and get starting position
    vehicle.start()
    starting_position = locator.get_starting_position()
    print("Starting latitude, longitude:", starting_position.lat, starting_position.lon)
    # request user to input address, this doesn't do anything apart from requesting a user input
    address = int(input("Please select one of the following destination addresses.\n \
                        [1] The University, 123 Palm Drive \n \
                        [2] The Shop, 45 Bridge Avenue \n \
                        [3] The Library, 77 Teak Street \n \
                        Enter the number of the address, so either 1, 2 or 3.\n"))
    assert address in [1, 2, 3]
    end_position = planner.search_address(starting_position)
    print(end_position.lat)
    print(end_position.lon)
    route = planner.generate_route(starting_position, end_position)
    vehicle.drive()
    planner.follow_route()
    print("Destination reached!")
    vehicle.stop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
