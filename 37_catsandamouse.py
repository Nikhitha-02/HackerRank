#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    """
    Determines which cat will catch the mouse first, or if the mouse escapes.

    Args:
        x (int): Position of Cat A.
        y (int): Position of Cat B.
        z (int): Position of the Mouse.

    Returns:
        str:
            - "Cat A" if Cat A is closer to the mouse,
            - "Cat B" if Cat B is closer,
            - "Mouse C" if both cats reach the mouse at the same time.
    """
    if abs(x - z) < abs(y - z):
        return "Cat A"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
