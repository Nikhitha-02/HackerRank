#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    """
    Calculates the minimum miles Marc must walk to burn calories
    from eating cupcakes, given the calorie counts.

    Rules:
    - Marc must eat the cupcakes in some order.
    - The miles walked for the i-th cupcake eaten is:
      calorie[i] * (2^i), where i starts from 0.
    - To minimize miles, eat the highest-calorie cupcakes first.

    Args:
        calorie (List[int]): List of calorie values for cupcakes.

    Returns:
        int: The minimum miles Marc must walk.
    """
    # Write your code here
    calorie.sort(reverse=True)
    sum = 0
    for i in range(len(calorie)):
        sum += calorie[i] * (2 ** i)
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
