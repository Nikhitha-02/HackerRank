#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    """
       Determines whether two kangaroos, starting at different positions and moving at different speeds,
       will land at the same location after the same number of jumps.

       The kangaroos start on a number line:
           - Kangaroo 1 starts at position x1 with a jump distance of v1.
           - Kangaroo 2 starts at position x2 with a jump distance of v2.

       The function checks if there exists a non-negative integer n such that:
           x1 + n*v1 == x2 + n*v2

       :param x1: int - Starting position of kangaroo 1.
       :param v1: int - Distance kangaroo 1 jumps each move.
       :param x2: int - Starting position of kangaroo 2.
       :param v2: int - Distance kangaroo 2 jumps each move.
       :return: str - "YES" if the kangaroos will meet at the same location
                      after the same number of jumps, otherwise "NO".

       Example:
           >>> kangaroo(0, 3, 4, 2)
           'YES'
           # Both land at position 12 after 4 jumps.

           >>> kangaroo(0, 2, 5, 3)
           'NO'
           # They never land at the same location.
       """
    # Write your code here
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    a = (x2 - x1) % (v1 - v2)
    b = (x2 - x1) / (v1 - v2)
    if a == 0 and b >= 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
