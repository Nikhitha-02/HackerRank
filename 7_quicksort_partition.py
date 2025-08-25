#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    """
        Sorts a list of integers using the QuickSort algorithm.

        This implementation chooses the first element as the pivot,
        partitions the remaining elements into two sublists
        (less than or equal to pivot, and greater than pivot),
        and recursively sorts the sublists.

        :param arr: List[int] - A list of integers to be sorted.
        :return: List[int] - A new sorted list of integers.

        Example:
            >>> quickSort([3, 6, 8, 10, 1, 2, 1])
            [1, 1, 2, 3, 6, 8, 10]

            >>> quickSort([])
            []

            >>> quickSort([5])
            [5]
    """
    # Write your code here
    if len(arr) <= 1:
        return arr
    p = arr[0]
    left_array = [i for i in arr[1:] if i <= p]
    right_array = [i for i in arr[1:] if i > p]
    return quickSort(left_array) + [p] + quickSort(right_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
