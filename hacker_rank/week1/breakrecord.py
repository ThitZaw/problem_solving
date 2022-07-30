#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minimum, maximun = scores[0], scores[0]
    countmax, countmin = 0, 0
    for game in scores:
        if game > maximun:
            maximun = game
            countmax += 1
        if game < minimum:
            minimum = game
            countmin += 1
            
    return [countmax, countmin]

if __name__ == '__main__':
    scores = [12,24,10,24]
    result = breakingRecords(scores)