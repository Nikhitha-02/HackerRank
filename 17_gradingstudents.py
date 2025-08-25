#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    """
    Applies the rounding rules to student grades.

    Rules:
    - If a grade is less than 38, it is failing and not rounded.
    - If the difference between the grade and the next multiple of 5
      is less than 3, round up to that multiple.
    - Otherwise, leave the grade unchanged.

    Args:
        grades (List[int]): List of student grades.

    Returns:
        List[int]: List of final grades after applying rounding rules.
    """
    # Write your code here
    final_grade = []
    for i in grades:
        if i < 38:
            final_grade.append(i)
        else:
            n = i % 5
            if n >= 3:
                final_grade.append((i + (5 - n)))
            else:
                final_grade.append(i)
    return final_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
