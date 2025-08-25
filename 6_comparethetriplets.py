#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    """
       Compares the scores of Alice and Bob across three categories and assigns points.

       Each category score is compared:
           - If Alice's score is greater than Bob's, Alice gets 1 point.
           - If Bob's score is greater than Alice's, Bob gets 1 point.
           - If they are equal, no points are awarded.

       :param a: List[int] - A list of 3 integers representing Alice's scores.
       :param b: List[int] - A list of 3 integers representing Bob's scores.
       :return: List[int] - A two-element list [Alice's total points, Bob's total points].

       Example:
           >>> compareTriplets([5, 6, 7], [3, 6, 10])
           [1, 1]
           >>> compareTriplets([17, 28, 30], [99, 16, 8])
           [2, 1]
    """
    # Write your code here
    count_alice = count_bob = 0
    for i in range(3):
        if a[i] > b[i]:
            count_alice += 1
        elif a[i] < b[i]:
            count_bob += 1
    return [count_alice, count_bob]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
