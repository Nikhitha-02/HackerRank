#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    """
        Computes the sum of all integers in the given array.

        :param ar: list[int] - A list of integers to be summed.
        :return: int - The total sum of all elements in the array.

        Example:
            >>> simpleArraySum([1, 2, 3, 4, 10, 11])
            31
    """
    # Write your code here
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
