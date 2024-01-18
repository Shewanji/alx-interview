#!/usr/bin/python3
"""
This script defines a function minOperations to calculate the minimum number
of operations needed to reach a given number of characters in a file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to reach n characters.

    Args:
    - n: An integer representing the desired number of characters.

    Returns:
    - An integer representing the minimum number of operations.
    """
    if n <= 1:
        return 0

    result = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            result += divisor
            n //= divisor
        divisor += 1

    return result
