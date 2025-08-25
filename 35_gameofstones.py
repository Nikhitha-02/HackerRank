#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):
    """
    Determines the winner of the Game of Stones.

    Rules:
    - There are 'n' stones in a pile.
    - Each player may remove 2, 3, or 5 stones on their turn.
    - Player 1 always goes first.
    - The player who cannot make a move loses.

    Args:
        n (int): Number of stones.

    Returns:
        str: "First" if Player 1 wins, "Second" otherwise.
    """
    # Write your code here
    if n % 7 == 0 or n % 7 == 1:
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
