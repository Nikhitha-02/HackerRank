#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    """
        Determine whether a numeric string can be split into a sequence of
        increasing consecutive integers without leading zeros.

        A string is considered "beautiful" if:
            - It can be split into two or more positive integers.
            - Each subsequent integer is exactly 1 greater than the previous.
            - No integer in the sequence contains leading zeros.
            - The sequence must preserve the order of digits in the string.

        Args:
            s (str): The numeric string to evaluate.

        Returns:
            None: Prints the result directly.
                  If the string is beautiful, prints "YES x" where x is the first number.
                  Otherwise, prints "NO".

        Example:
            >>> separateNumbers("1234")
            YES 1
            >>> separateNumbers("91011")
            YES 9
            >>> separateNumbers("101103")
            NO
            >>> separateNumbers("1")
            NO
    """
    # Write your code here
    n = len(s)
    for i in range(1, n // 2 + 1):
        f = int(s[:i])
        number = f
        sequence = str(f)
        while len(sequence) < n:
            number += 1
            sequence += str(number)
        if sequence == s:
            print(f"YES {f}")
            return
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
