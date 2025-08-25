#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n, m, s):
    """
    Determines which prisoner receives the last sweet.

    Args:
        n (int): Number of prisoners (numbered 1 to n).
        m (int): Number of sweets to distribute.
        s (int): Starting prisoner position.

    Returns:
        int: The prisoner number who gets the last sweet.
    """
    # Write your code here
    chair = (s + m - 1) % n
    if chair != 0:
        return chair
    else:
        return n


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
