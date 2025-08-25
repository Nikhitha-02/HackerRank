#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    """
        Determines the most frequently sighted bird type.
        If multiple types are most common, the smallest ID is returned.

        Args:
            arr (List[int]): A list of integers representing bird type IDs.

        Returns:
            int: The ID of the most frequently sighted bird.
    """
    # Write your code here
    c = {}
    for i in arr:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    max_value = max(c.values())
    return min(k for k, v in c.items() if v == max_value)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
