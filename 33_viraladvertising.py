#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    """
    Simulates the viral advertising campaign and calculates total likes.

    Rules:
    - Day 1 starts with 5 people receiving the ad.
    - Each day, floor(shared/2) people like the ad.
    - Each person who likes the ad shares it with 3 new friends.
    - Process repeats for 'n' days.

    Args:
        n (int): Number of days.

    Returns:
        int: Total cumulative likes after n days.
    """
    # Write your code here
    shared = 5
    cummulative = 0
    for i in range(1, n + 1):
        likes = shared // 2
        cummulative += likes
        shared = likes * 3
    return cummulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
