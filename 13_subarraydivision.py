#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    """
    Determines how many ways the chocolate bar can be divided such that
    the sum of 'm' consecutive pieces is equal to 'd'.

    Args:
        s (List[int]): The list of integers representing the chocolate squares.
        d (int): The target sum (Ron's birth day).
        m (int): The length of the segment (Ron's birth month).

    Returns:
        int: The number of valid ways the bar can be divided.
    """
    # Write your code here
    count = 0
    for i in range(len(s) - m + 1):
        l = s[i:i + m]
        if sum(l) == d:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
