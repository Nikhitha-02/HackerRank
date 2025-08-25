#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    """
    Determines the winner of the Tower Breakers game.

    Rules:
    - There are n towers, each of height m.
    - Players alternate turns. On each turn, a player chooses a tower of height x > 1
      and reduces it to any height y such that 1 <= y < x and x % y == 0.
    - Player 1 moves first.
    - The player who cannot make a move loses.

    Args:
        n (int): Number of towers.
        m (int): Initial height of each tower.

    Returns:
        int: 1 if Player 1 wins, 2 if Player 2 wins.
    """
    # Write your code here
    if m == 1 or n % 2 ==  0:
        return 2
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
