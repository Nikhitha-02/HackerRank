#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    """
    Determines if, after sorting each row alphabetically,
    all columns in the grid are also sorted in ascending order.

    Args:
        grid (List[str]): A list of equal-length strings representing the grid.

    Returns:
        str: "YES" if columns are sorted, "NO" otherwise.
    """
    # Write your code here
    sort_list = ["".join(sorted(i)) for i in grid]
    row = len(sort_list)
    column = len(sort_list[0])

    for j in range(column):
        for k in range(1, row):
            if sort_list[k][j] < sort_list[k - 1][j]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
