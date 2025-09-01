#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    """
        Find the minimum distance between two equal elements in the list.

        Args:
            a (List[int]): A list of integers.

        Returns:
            int: The minimum distance between two equal elements.
                 If no such elements exist, returns -1.

        Example:
            >>> minimumDistances([7, 1, 3, 4, 1, 7])
            3
            >>> minimumDistances([1, 2, 3, 4])
            -1
    """
    # Write your code here
    min_diff = None
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                diff = abs(j - i)
                if min_diff is None or diff < min_diff:
                    min_diff = diff
    return min_diff if min_diff is not None else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
