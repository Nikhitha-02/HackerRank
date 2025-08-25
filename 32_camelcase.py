#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    """
    Counts the number of words in a camelCase string.

    Rules:
    - The first word starts lowercase.
    - Each uppercase letter marks the start of a new word.

    Args:
        s (str): The camelCase string.

    Returns:
        int: The number of words in the string.
    """
    # Write your code here
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
