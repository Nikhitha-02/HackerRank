#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """
    Converts time from 12-hour AM/PM format to 24-hour format.

    Args:
        s (str): Time string in the format "hh:mm:ssAM" or "hh:mm:ssPM".

    Returns:
        str: Time string in 24-hour format ("HH:MM:SS").
    """
    # Write your code here
    meridiem = s[-2:]
    time = s[:-2]
    h, m, s = map(int, time.split(":"))
    if meridiem == "AM":
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12
    return f"{h:02d}:{m:02d}:{s:02d}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
