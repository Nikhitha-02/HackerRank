# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    """
    Determines the total number of matching pairs of socks from a pile.

    Each sock is represented by an integer indicating its color.
    The function counts how many pairs of socks with the same color
    can be formed from the given list.

    :param n: int - The number of socks in the pile.
    :param ar: list[int] - A list of integers where each integer represents
                           the color of a sock.
    :return: int - The total number of matching pairs of socks.

    Example:
        >>> sockMerchant(7, [1, 2, 1, 2, 1, 3, 2])
        2
    """
    # Write your code here
    l = {}
    for i in ar:
        if i in l:
            l[i] += 1
        else:
            l[i] = 1

    pairs = 0
    for element in l.values():
        pairs += element // 2

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
