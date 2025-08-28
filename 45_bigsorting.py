#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    """
    Sort an array of numeric strings in ascending numerical order.

    Since the numbers can be very large (up to 10^6 digits), they are given as strings.
    The sorting strategy:
      - First compare by string length (shorter numbers are smaller).
      - If lengths are equal, compare lexicographically (works because both numbers have same length).

    Args:
        unsorted (List[str]): A list of numbers represented as strings.

    Returns:
        List[str]: The list sorted in ascending numerical order.

    Example:
        >>> bigSorting(["31415926535897932384626433832795", "1", "3", "10", "3", "5"])
        ['1', '3', '3', '5', '10', '31415926535897932384626433832795']

        >>> bigSorting(["1", "2", "100", "111", "200"])
        ['1', '2', '100', '111', '200']
    """
    # Write your code here
    unsorted.sort(key = lambda x:(len(x) , x))
    return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
