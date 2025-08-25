#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    """
    Determines how many candles are the tallest.

    Args:
        candles (List[int]): A list of integers representing candle heights.

    Returns:
        int: The number of candles that have the maximum height.
    """
    # Write your code here
    c = {}
    for i in candles:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    return max(c.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
