
# Exercises on Codio
import math
import copy


class Point:
    x = int
    y = int


class Circle:
    center = Point
    radius = int


class Rectangle:
    width = int
    height = int
    corner = Point


def point_in_circle(point, circle):
    # formula = (x - h)**2 + (y - k)**2 = r**2
    # formula = (point.x - circle.center.x)**2 + (point.y - circle.center.y)**2 = circle.radius**2
    expected_radius = (point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2
    value_on_circle = eval("expected_radius == circle.radius**2")

    distance = math.sqrt((point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2)
    value_in_circle = eval("distance <= circle.radius")
    return value_on_circle or value_in_circle


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    if point_in_circle(p, circle):
        return True

    return False


if __name__ == '__main__':
    p = Point()
    p.x = 150
    p.y = 100

    # Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.
    new_circle = Circle()
    new_circle.center = p
    new_circle.radius = 75

    new_point = Point()
    new_point.x = 50
    new_point.y = 50

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(point_in_circle(new_point, new_circle))

    print(rect_in_circle(box, new_circle))

    print(rect_circle_overlap(box, new_circle))