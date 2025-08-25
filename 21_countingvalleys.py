#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    """
    Counts the number of valleys traversed during a hike.

    A valley is defined as a sequence of steps below sea level,
    starting with a step down ('D') and ending with a step up ('U')
    back to sea level.

    Args:
        steps (int): The total number of steps taken (length of path).
        path (str): A string consisting of 'U' (up) and 'D' (down).

    Returns:
        int: The number of valleys traversed.
    """
    # Write your code here
    steps = [-1 if x == "D" else 1 for x in list(path)]
    count = 0
    step_count = steps[0]
    for i in steps[1:]:
        step_count += i
        if step_count == 0:
            if i == 1:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
