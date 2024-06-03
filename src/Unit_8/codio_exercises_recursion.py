#
# Codio exercises for recursion
#

def recursive_sum(n: int):
    """Recursively calculate sum from 0 to the parameter."""
    # base case: if n is 0, return 0
    if n == 0:
        return 0
    # recursive case: return n plus the sum of integers from 0 to n-1
    else:
        return n + recursive_sum(n - 1)


def list_sum(numbers: list):
    """Recursively calculate the sum of a list of numbers."""
    # base case: if the list is empty, return 0
    if not numbers:
        return 0
    # recursive case: return the first element plus the sum of the rest of the list
    else:
        return numbers[0] + list_sum(numbers[1:])


def bunny_ears(bunnies: int):
    """Recursively determine the number of bunny ears (2 per bunny)."""
    # base case: if there are no bunnies, return 0
    if bunnies == 0:
        return 0
    # recursive case: 2 ears for the current bunny plus the ears of the remaining bunnies
    else:
        return 2 + bunny_ears(bunnies - 1)


def reverse_string(string: str):
    """Recursively reverse the given string."""
    # base case: if the string is empty or has only one character, return it
    if len(string) <= 1:
        return string
    # recursive case: return the last character plus the reverse of the remaining string
    else:
        return string[-1] + reverse_string(string[:-1])


def get_max(numbers):
    """Recursively find the maximum number in the list."""
    # base case: if the list has only one element, return that element
    if len(numbers) == 1:
        return numbers[0]
    # recursive case: compare the first element with the maximum of the rest of the list
    else:
        max_in_list = get_max(numbers[1:])
        return numbers[0] if numbers[0] > max_in_list else max_in_list


if __name__ == '__main__':
    # assertions for recursive sum based on Codio reqs
    assert recursive_sum(5) == 15
    assert recursive_sum(10) == 55

    # assertions for list sum based on Codio reqs
    assert list_sum([1, 2, 3, 4, 5]) == 15
    assert list_sum([10, 12.5, 10, 7]) == 39.5

    # assertions for bunny ears
    assert bunny_ears(8) == 16
    assert bunny_ears(0) == 0

    # assertions for reverse string recursion
    assert reverse_string("cat") == "tac"
    assert reverse_string("house") == "esuoh"

    # assertions for getting max in list
    assert get_max([1, 2, 3, 4, 5]) == 5
    assert get_max([11, 22, 3, 41, 15]) == 41



