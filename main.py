import math
from typing import Union


def power(x: int, y: int) -> Union[float, int]:
    res = pow(x, y)
    return res


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n cannot be a negative number")
    res = math.factorial(n)
    return res


def permutation(n: int, r: int) -> float:
    if n < r:
        raise ValueError("r should not be greater than n")
    res = factorial(n) / factorial(n - r)
    return res


def combination(n: int, r: int) -> float:
    res = permutation(n, r) * (1 / factorial(r))
    return res
