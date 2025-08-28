#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    """
    Count the number of perfect squares between two integers a and b (inclusive).

    A perfect square is an integer that is the square of another integer.
    For example, 1, 4, 9, and 16 are perfect squares.

    The idea:
    - The smallest possible square root is ceil(sqrt(a)).
    - The largest possible square root is floor(sqrt(b)).
    - The count of integers in this range = difference + 1.

    Args:
        a (int): Lower bound of the range (inclusive).
        b (int): Upper bound of the range (inclusive).

    Returns:
        int: The number of perfect squares between a and b (inclusive).

    Example:
        >>> squares(3, 9)
        2   # (squares are 4, 9)

        >>> squares(17, 24)
        0   # (no perfect squares in this range)
    """
    # Write your code here
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1 if b >= a else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
