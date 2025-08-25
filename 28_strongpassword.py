#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    """
    Determines the minimum number of characters to add to make a password strong.

    A password is considered strong if it contains at least:
    - One digit [0-9]
    - One lowercase letter [a-z]
    - One uppercase letter [A-Z]
    - One special character from !@#$%^&*()-+
    - Minimum length of 6

    Args:
        n (int): The current length of the password.
        password (str): The current password string.

    Returns:
        int: The minimum number of characters to add.
    """
    # Return the minimum number of characters to make the password strong
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    count = 0
    if not (set(password) & numbers):
        count += 1
    if not (set(password) & lower_case):
        count += 1
    if not (set(password) & upper_case):
        count += 1
    if not (set(password) & special_characters):
        count += 1

    return max(count, 6 - n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
