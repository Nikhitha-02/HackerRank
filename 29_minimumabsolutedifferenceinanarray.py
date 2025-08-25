#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    """
     Finds the minimum absolute difference between any two elements in the array.

     Approach:
     - Sort the array.
     - The smallest absolute difference must occur between two adjacent elements.
     - Compute differences for adjacent pairs and return the minimum.

     Args:
         arr (List[int]): List of integers.

     Returns:
         int: The minimum absolute difference between any two elements.
     """
    # Write your code here
    arr.sort()
    min_diff = None
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if min_diff is None or diff < min_diff:
            min_diff = diff
    return min_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
