#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    """
    Perform right circular rotations on an array and return the values at specific query indices.

    A right circular rotation moves the last element of the array to the front.
    After k such rotations, the array is modified, and the function must return
    the values at the given query indices.

    Args:
        a (List[int]): The original array of integers.
        k (int): The number of right circular rotations to perform.
        queries (List[int]): List of indices to retrieve from the rotated array.

    Returns:
        List[int]: Values from the rotated array corresponding to the queried indices.

    Example:
        >>> circularArrayRotation([1, 2, 3], 2, [0, 1, 2])
        [2, 3, 1]

    Explanation:
        Original array: [1, 2, 3]
        After 1 rotation: [3, 1, 2]
        After 2 rotations: [2, 3, 1]
        Query results: index 0 -> 2, index 1 -> 3, index 2 -> 1
    """
    # Write your code here
    n = len(a)
    k = k % n
    rotation = a[-k:] + a[:-k]
    r = []
    for i in queries:
        r.append(rotation[i])
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
