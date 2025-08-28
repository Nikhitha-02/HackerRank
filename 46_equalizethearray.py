#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    """
    Determine the minimum number of deletions required so that all elements
    in the array are equal.

    Strategy:
    - Count the frequency of each element.
    - Find the maximum frequency (most common element).
    - To equalize, keep all occurrences of that element and delete the rest.

    Args:
        arr (List[int]): The input array of integers.

    Returns:
        int: The minimum number of deletions needed.

    Example:
        >>> equalizeArray([3, 3, 2, 1, 3])
        2
        # Explanation: Keep all 3's (frequency = 3), delete 2 and 1 → 2 deletions.
    """
    # Write your code here
    c = {}
    for i in arr:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    m = max(c.values())
    return len(arr) - m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
