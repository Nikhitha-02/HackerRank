#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    """
        Reduces a string by repeatedly removing pairs of adjacent matching characters.

        The process continues until no such pairs remain:
          - If two adjacent characters are the same, they are removed.
          - Otherwise, the character is kept.
        If the final string is empty, the function returns "Empty String".

        :param s: str - The input string consisting of lowercase English letters.
        :return: str - The reduced string, or "Empty String" if no characters remain.

        Example:
            >>> superReducedString("aaabccddd")
            'abd'

            >>> superReducedString("abba")
            'Empty String'

            >>> superReducedString("abc")
            'abc'
    """
    # Write your code here
    l = []
    for i in range(len(s)):
        if len(l) == 0 or l[-1] != s[i]:
            l.append(s[i])
        else:
            l.pop()
    if len(l) == 0:
        return "Empty String"
    else:
        return "".join(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
