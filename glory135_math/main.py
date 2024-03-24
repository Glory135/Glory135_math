from typing import Union


def power(x: int, y: int) -> Union[float, int]:
    """
    Calculate the result of raising x to the power of y.

    :param x: The base number (int).
    :param y: The exponent.
    :return: The result of x^y as a float if both x and y are floats, otherwise an int.
    """
    res = x**y
    return res


def factorial(n: int) -> int:
    """
    Calculate the factorial of n.

    :param n: A non-negative integer.
    :return: The factorial of n
    """
    if n < 0:
        raise ValueError("n cannot be a negative number")
    accumulator = 1
    while n > 1:
        accumulator *= n
        n -= 1
    return accumulator


def permutation(n: int, r: int) -> float:
    """
    Calculate the number of ways to choose r items from a set of n items without repetition.

    :param n: The total number of items.
    :param r: The number of items to choose.
    :return: The number of possible combinations.
    """
    if n < r:
        raise ValueError("r should not be greater than n")
    res = factorial(n) / factorial(n - r)
    return res


def combination(n: int, r: int) -> float:
    """
    Calculate the number of ways to choose r items from a set of n items with replacement allowed.

    :param n: The total number of items.
    :param r: Number of items chosen each time.
    :return: The number of possible combinations
    """
    res = permutation(n, r) * (1 / factorial(r))
    return res
