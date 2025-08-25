#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    """
    Simulates the cloud jumping game and computes remaining energy.

    Rules:
    - Start with 100 energy at cloud 0.
    - Each jump reduces energy by 1.
    - Landing on a thundercloud (value 1) reduces energy by an extra 2.
    - The player moves in steps of 'k' and stops when back at cloud 0.

    Args:
        c (List[int]): List of clouds (0 = safe, 1 = thundercloud).
        k (int): Fixed jump distance.

    Returns:
        int: Remaining energy after completing the game.
    """
    e = 100
    i = 0
    n = len(c)
    while True:
        i = (i + k) % n
        e -= 1 + 2 * c[i]
        if i == 0:
            break
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
