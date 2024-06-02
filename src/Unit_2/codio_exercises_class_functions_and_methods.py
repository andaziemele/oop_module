#
# Codio exercises on Class functions and methods
#

"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division
from datetime import date, datetime


class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """
    hour = int
    minute = int
    second = int


def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(time1, time2):
    """Write a boolean function called is_after that takes two Time objects,
    t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise."""
    t1 = time1.hour + time1.minute + time1.second
    t2 = time2.hour + time2.minute + time2.second

    return t1 > t2


def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_times(t1, t2):
    """Adds two time objects.

    t1, t2: Time

    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False

    return True

# Write a function called mul_time that takes a Time object and a number and returns a new Time object
# that contains the product of the original Time and the number.

# Then use mul_time to write a function that takes a Time object that represents the finishing time
# in a race, and a number that represents the distance, and returns a Time object that represents the
# average pace (time per mile).


def mul_time(time, mult):
    product = time_to_int(time) * mult
    product = int_to_time(product)
    return product


def distance_time(time, dist):
    product = time_to_int(time) / dist
    product = int_to_time(product)
    return product


def calculate_age_and_time_to_next_birthday(birthday_str):
    """Write a program that takes a birthday as input and
    prints the user’s age and the number of days, hours, minutes and
    seconds until their next birthday."""
    # parse birthday date string
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

    # get the current date and time
    now = datetime.now()

    # calculate the age
    age = now.year - birthday.year
    if (now.month, now.day) < (birthday.month, birthday.day):
        age -= 1

    # calculate the next birthday
    next_birthday_year = now.year if (now.month, now.day) < (birthday.month, birthday.day) else now.year + 1
    next_birthday = datetime(next_birthday_year, birthday.month, birthday.day)

    # calculate the time difference until the next birthday
    time_until_next_birthday = next_birthday - now

    # extract days, hours, minutes, and seconds from the time difference
    days = time_until_next_birthday.days
    seconds = time_until_next_birthday.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # print the results
    print(f"Age: {age} years")
    print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")


if __name__ == '__main__':
    time = Time()
    time.hour = 1
    time.minute = 59
    time.second = 30

    time2 = Time()
    time2.hour = 2
    time2.minute = 59
    time2.second = 30

    print(is_after(time, time2))

    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print_time(mul_time(noon_time, 1.1237))

    race_time = Time()
    race_time.hour = 3
    race_time.minute = 34
    race_time.second = 5

    print_time(distance_time(race_time, 26.2))

    print(date.today())

    print(date.today().weekday())

    print(date.today().strftime('%A'))

    birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
    calculate_age_and_time_to_next_birthday(birthday_input)







