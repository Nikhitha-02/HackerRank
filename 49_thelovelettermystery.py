#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    """
        Calculate the minimum number of operations required to make a string
        a palindrome by only reducing characters.

        Rules:
            - You can only decrease the value of a character (e.g., 'd' → 'c'),
              but cannot increase it.
            - The character 'a' cannot be reduced further.
            - Each single decrement counts as one operation.

        The minimum number of operations is determined by comparing characters
        from both ends of the string and summing the absolute differences in
        their alphabet positions.

        Args:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            int: The minimum number of operations required to make the string a palindrome.

        Example:
            >>> theLoveLetterMystery("abc")
            2
            >>> theLoveLetterMystery("abcba")
            0
            >>> theLoveLetterMystery("abcd")
            4
            >>> theLoveLetterMystery("cba")
            2
    """
    # Write your code here
    alpha = "abcdefghijklmnopqrstuvwxyz"
    op = 0
    n = len(s)
    for i in range(n // 2):
        l = alpha.index(s[i])
        r = alpha.index(s[n - i - 1])
        op += abs(l - r)
    return op


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
