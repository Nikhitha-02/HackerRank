#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    """
    Solves the permutation equation problem.

    For each x in [1..n], find y such that:
        p[p[y]] = x

    Args:
        p (List[int]): A permutation of integers 1..n.

    Returns:
        List[int]: The list of results for each x.
    """
    # Write your code here
    r = []
    for i in range(1, len(p) + 1):
        position = p.index(i) + 1
        j = p.index(position) + 1
        r.append(j)
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
