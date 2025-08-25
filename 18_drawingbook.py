#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    """
    Determines the minimum number of page turns needed
    to reach page 'p' in a book of 'n' pages.

    Args:
        n (int): Total number of pages in the book.
        p (int): Target page number.

    Returns:
        int: Minimum number of page turns required.
    """
    # Write your code here
    return min(p//2,(n // 2) - (p // 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
