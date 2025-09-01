#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    """
        Calculate the maximum number of games that can be purchased during the Halloween Sale.

        The first game starts at price `p`. Each subsequent game costs `d` units less than the
        previous one, but the price cannot drop below `m`. Given a budget `s`, this function
        returns how many games can be bought.

        Parameters:
            p (int): The initial price of the first game.
            d (int): The discount applied to the price of each subsequent game.
            m (int): The minimum price a game can cost.
            s (int): The total budget available to spend.

        Returns:
            int: The maximum number of games that can be purchased within the budget.

        Example:
            >>> howManyGames(20, 3, 6, 80)
            6
            >>> howManyGames(20, 3, 6, 85)
            7
    """
    # Return the number of games you can buy
    c = 0
    cost = p
    while s >= cost:
        s -= cost
        c += 1
        cost = max(cost - d, m)
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
