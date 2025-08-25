#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    """
        Determines the fine for returning a library book late.

        Rules:
        - If the book is returned on or before the due date → fine = 0
        - If returned late but within the same month and year → fine = 15 * days late
        - If returned late but within the same year → fine = 500 * months late
        - If returned in a later year → fine = 10000

        Args:
            d1 (int): Returned day
            m1 (int): Returned month
            y1 (int): Returned year
            d2 (int): Due day
            m2 (int): Due month
            y2 (int): Due year

        Returns:
            int: The calculated fine.
    """
    # Write your code here

    if d2 < d1 and y1 == y2 and m1 == m2:
        return 15 * (d1 - d2)
    elif m2 < m1 and y1 == y2:
        return 500 * (m1 - m2)
    elif y2 < y1:
        return 10000
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
