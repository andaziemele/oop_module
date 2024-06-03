#
# Codio tutorial lab exercises for recursion
#

def recursive_power(base: int, exponent: int):
    """Write a recursive function called recursive_power that takes two integers as parameters.
    The first parameter is the base and the second parameter is the exponent.
    Return the base parameter to the power of the exponent."""
    # base case: if exponent is 0, return 1
    if exponent == 0:
        return 1
    # recursive case: base * (base to the power of (exponent - 1))
    else:
        return base * recursive_power(base, exponent - 1)


if __name__ == '__main__':
    assert recursive_power(5, 3) == 125
    assert recursive_power(4, 5) == 1024
