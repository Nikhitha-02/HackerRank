#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    """
        Finds the number of integers that are 'between' two sets.

        An integer x is considered valid if:
          1. Every element in list 'a' is a factor of x (i.e., x % a[i] == 0 for all i).
          2. x is a factor of every element in list 'b' (i.e., b[j] % x == 0 for all j).

        The function counts and returns how many such integers exist
        in the inclusive range [max(a), min(b)].

        :param a: List[int] - A list of integers (the first set).
        :param b: List[int] - A list of integers (the second set).
        :return: int - The count of integers satisfying the conditions.

        Example:
            >>> getTotalX([2, 4], [16, 32, 96])
            3
            # The valid integers are 4, 8, 16

            >>> getTotalX([3, 4], [24, 48])
            2
            # The valid integers are 12, 24
    """
    # Write your code here
    count = 0
    for x in range(max(a), min(b) + 1):
        flag = True
        for i in a:
            if x % i != 0:
                flag = False
                break
        if flag:
            for j in b:
                if j % x != 0:
                    flag = False
                    break
        if flag:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
