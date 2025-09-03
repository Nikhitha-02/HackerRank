#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    """
    Calculates the minimum number of deletions required to make a string alternate
    between 'A' and 'B' characters, i.e., no two adjacent characters are the same.

    Args:
        s (str): The input string consisting only of characters 'A' and 'B'.

    Returns:
        int: The minimum number of deletions required.

    Example:
        >>> alternatingCharacters("AAAA")
        3
        >>> alternatingCharacters("ABABAB")
        0
        >>> alternatingCharacters("AAABBB")
        4
    """
    # Write your code here
    count = 0
    for i in range(1,len(s)):
        if s[i] == s[i - 1]:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
