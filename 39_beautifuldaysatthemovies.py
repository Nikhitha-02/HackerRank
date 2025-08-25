#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    """
    Counts the number of 'beautiful days' between days i and j inclusive.

    A day is beautiful if:
    abs(day - reverse(day)) is divisible by k.

    Args:
        i (int): Starting day.
        j (int): Ending day.
        k (int): Divisor.

    Returns:
        int: Number of beautiful days.
    """
    # Write your code here
    c = 0
    for i in range(i, j + 1):
        reverse = int(str(i)[::-1])
        if abs(i - reverse) % k == 0:
            c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
