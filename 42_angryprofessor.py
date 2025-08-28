#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    """
    Determine the minimum number of deletions required so that all elements
    in the array are equal.

    The strategy:
    - Count the frequency of each unique element.
    - Find the element with the maximum frequency.
    - The minimum deletions required = total elements - maximum frequency.

    Args:
        arr (List[int]): A list of integers representing the array.

    Returns:
        int: The minimum number of deletions needed to equalize the array.
    """
    # Write your code here
    c = 0
    for i in a:
        if i <= 0:
            c += 1
    if c >= k:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
