#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    """
     Determines whether Anna was correctly charged for her share of the bill.

     Anna and Brian order several items, but Anna does not eat the item at index k.
     Brian splits the bill evenly, but Anna wants to verify if she was overcharged.

     The function prints:
       - "Bon Appetit" if Anna was charged correctly.
       - The overcharged amount if Brian charged her too much.

     :param bill: List[int] - A list of integers where each element represents the cost of an item.
     :param k: int - The zero-based index of the item Anna did not eat.
     :param b: int - The amount Brian charged Anna.
     :return: None - The function prints the result directly.

     Example:
         >>> bonAppetit([3, 10, 2, 9], 1, 12)
         5

         >>> bonAppetit([3, 10, 2, 9], 1, 7)
         Bon Appetit
     """
    # Write your code here
    bill.pop(k)
    sum = 0
    for i in bill:
        sum += i

    b_actual = sum // 2
    if b_actual == b:
        print("Bon Appetit")
    else:
        print(b - b_actual)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
