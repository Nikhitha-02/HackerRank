#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    """
    Prints the ratios of positive, negative, and zero elements in the array.

    Each ratio is printed on a new line with 6 decimal places.

    Args:
        arr (List[int]): A list of integers.
    """
    # Write your code here
    n = len(arr)
    cp = cn = cz = 0
    for i in arr:
        if i > 0:
            cp += 1
        elif i < 0:
            cn += 1
        else:
            cz += 1
    print(cp / n)
    print(cn / n)
    print(cz / n)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
