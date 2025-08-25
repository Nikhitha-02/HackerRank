#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    """
    Encrypts a string using the Caesar Cipher technique.

    Each letter in the string is shifted by 'k' positions in the alphabet:
    - Lowercase letters remain lowercase.
    - Uppercase letters remain uppercase.
    - Non-alphabetic characters are not modified.

    Args:
        s (str): The input string to encrypt.
        k (int): The number of positions to shift.

    Returns:
        str: The encrypted string.
    """
    # Write your code here
    r = ""
    for i in s:
        if i.islower():
            char = (ord(i) - ord('a') + k) % 26 + ord('a')
            r += chr(char)
        elif i.isupper():
            char = (ord(i) - ord('A') + k) % 26 + ord('A')
            r += chr(char)

        else:
            r += i
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

