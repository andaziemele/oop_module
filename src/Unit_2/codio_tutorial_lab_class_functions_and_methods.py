#
# Codio Tutorial Lab exercises
#

class Person:
    count = 0

    """Represents a generic Person."""

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):

        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

    @classmethod
    def print_count(cls):
        return cls.count

    def print_self(self):
        """Return details."""
        return (self.first_name, self.last_name,
                self.weight_in_lbs, self.height_in_inches, self.calc_bmi())

    def evaluate_weight(self):
        """Healthy weight indicator based on BMI."""
        bmi = self.calc_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi > 24.9:
            return "Overweight"
        else:
            return "Healthy Weight"


if __name__ == '__main__':
    p = Person('Tom', 'Thumb', 150, 62)
    p2 = Person('Fred', 'Flint', 225, 57)

    print(p.calc_bmi())
    print(p2.calc_bmi())
    print(Person.count)
    print(Person.print_count())
    print(p.print_self())
    print(p2.print_self())
    print(p.evaluate_weight())
    print(p2.evaluate_weight())