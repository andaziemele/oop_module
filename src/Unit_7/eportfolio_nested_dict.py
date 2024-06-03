#
# example nested dictionary for autnomous vehicle
#

class DetectedCars:
    def __init__(self):
        # Initialize a nested dictionary to store car data
        self.cars = dict() # initialise empty dict

    def detect_car(self, car_object):
        """Adds car to cars dict."""
        # Use the model as the key and the car dictionary as the value
        self.cars[car_object.car['car_id']] = car_object.car # add car dicts, creating a nested dict

    def get_items(self):
        # Return the items of the nested dictionary
        return self.cars.items()

    def get_keys(self):
        # Return the keys of the nested dictionary
        return self.cars.keys()

    def get_values(self):
        # Return the values of the nested dictionary
        return self.cars.values()


class Car:
    def __init__(self, car_id: int, model: str, distance: int, speed: int):
        """Initialising the car object"""
        self.car = {"car_id": car_id, "model": model, "distance": distance, "speed": speed}


if __name__ == '__main__':
    # Create an instance of the Car class
    detected_cars = DetectedCars()
    car1 = Car(1, "Audi", 300, 20)
    car2 = Car(2, "Toyota", 500, 50)
    car3 = Car(3, "BMW", 20, 100)

    cars = [car1, car2, car3]

    for car in cars:
        detected_cars.detect_car(car)

    print(detected_cars.cars)
    # Call the methods and print their outputs
    print("Items:")
    for item in detected_cars.get_items():
        print(item)

    print("\nKeys:")
    for key in detected_cars.get_keys():
        print(key)

    print("\nValues:")
    for value in detected_cars.get_values():
        print(value)