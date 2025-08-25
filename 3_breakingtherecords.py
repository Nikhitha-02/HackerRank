#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    """
       Determines the number of times a player breaks their highest and lowest scoring records.

       A record is considered "broken" if the score is strictly greater than the current
       maximum (highest score so far) or strictly less than the current minimum (lowest score so far).
       The function returns two values:
           - The number of times the highest score record was broken.
           - The number of times the lowest score record was broken.

       :param scores: list[int] - A list of integers representing the player's scores in sequential games.
       :return: tuple[int, int] - A tuple containing:
                                  (number of times the maximum record was broken,
                                   number of times the minimum record was broken)

       Example:
           >>> breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])
           (2, 4)
           # Max record broken: 20, 25 -> 2 times
           # Min record broken: 5, 4, 2, 1 -> 4 times
    """
    # Write your code here
    min = []
    max = []
    min_score = max_score = scores[0]
    for i in scores[1:]:
        if i < min_score:
            min_score = i
            min.append(i)
        elif i > max_score:
            max_score = i
            max.append(i)
    return len(max), len(min)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
