
# retrieved exercises from Codio on Classes and Objects

class Person:
    """Represents a generic Person."""

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height


if __name__ == '__main__':
    p1 = Person("Tom", "B", "58", "161")
    p2 = Person("Fred", "C", "87", "198")
    p3 = Person("George", "F", "74", "187")
    p4 = Person("Tanya", "G", "60", "172")
    p5 = Person("Mary", "T", "65", "178")

    people = [p1, p2, p3, p4, p5]

    for person in people:
        print(person.first_name)
