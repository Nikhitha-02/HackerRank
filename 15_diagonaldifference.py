#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    """
    Computes the absolute difference between the sums of the matrix's
    primary diagonal and secondary diagonal.

    Args:
        arr (List[List[int]]): A square 2D list of integers.

    Returns:
        int: The absolute difference between the two diagonal sums.
    """
    # Write your code here
    n = len(arr)
    diagonal = [arr[i][i] for i in range(n)]
    anti_diagonal = [arr[i][n - 1 - i] for i in range(n)]
    return abs(sum(diagonal) - sum(anti_diagonal))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
