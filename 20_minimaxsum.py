#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """
    Prints the minimum and maximum sum of 4 out of 5 integers.

    The function computes:
    - Minimum sum: sum of all elements except the maximum.
    - Maximum sum: sum of all elements except the minimum.

    Args:
        arr (List[int]): A list of exactly 5 integers.
    """
    # Write your code here
    total = sum(arr)
    min_sum = total - max(arr)
    max_sum = total - min(arr)
    print(min_sum,max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
