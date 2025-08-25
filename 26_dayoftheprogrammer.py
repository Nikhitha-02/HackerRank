#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    """
    Determines the Day of the Programmer (the 256th day of the year) in Russia,
    accounting for the calendar transition from Julian to Gregorian.

    Rules:
    - Julian calendar (1700–1917): leap year if divisible by 4.
    - Transition year (1918): the 256th day falls on 26.09.1918.
    - Gregorian calendar (1919–2700): leap year if divisible by 400,
      or divisible by 4 but not by 100.

    Args:
        year (int): The year to evaluate.

    Returns:
        str: The date of the 256th day in the format "dd.mm.yyyy".
    """
    # Write your code here
    if year == 1918:
        return f"26.09.{year}"
    elif (year < 1918 and year % 4 == 0) or (
            year > 1918 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
