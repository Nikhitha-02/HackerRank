#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    """
        Prints a right-aligned staircase pattern of '#' symbols with height and width equal to n.

        Each line consists of spaces followed by '#' characters such that the staircase
        is aligned to the right.

        :param n: int - The size of the staircase (number of rows and also the maximum number of '#').
        :return: None - This function prints the staircase directly and does not return a value.

        Example:
            >>> staircase(4)
               #
              ##
             ###
            ####
    """
    # Write your code here
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j >= n + 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
