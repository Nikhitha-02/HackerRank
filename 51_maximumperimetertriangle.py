#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    """
    Finds the non-degenerate triangle with the maximum possible perimeter
    from the given list of stick lengths.

    The triangle must satisfy the triangle inequality:
        a + b > c  (for sorted sides a <= b <= c)

    Selection rules if multiple triangles have the same perimeter:
    1. Choose the one with the longest maximum side.
    2. If tied, choose the one with the longest minimum side.
    3. If still tied, return any of them.

    Args:
        sticks (List[int]): A list of integers representing stick lengths.

    Returns:
        List[int]: A list of 3 integers representing the sides of the chosen
                   triangle in non-decreasing order.
                   If no valid triangle can be formed, returns [-1].

    Example:
        >>> maximumPerimeterTriangle([1, 1, 1, 3, 3])
        [1, 3, 3]
        >>> maximumPerimeterTriangle([1, 2, 3])
        [-1]
    """
    # Write your code here
    sticks.sort()
    n = len(sticks)
    for i in range(n - 3, -1, -1):
        a, b, c = sticks[i], sticks[i + 1], sticks[i + 2]
        if a + b > c:
            return [a, b, c]
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
