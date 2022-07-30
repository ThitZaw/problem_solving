import math
import os
import random
import re
import sys
from time import time_ns

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time_list = s.split(':')  

    if s[-2:] == 'PM':
        if time_list[0] != '12':
            time_list[0] = str(int(time_list[0])+12)
    else:
        if time_list[0] == '12':
            time_list[0] = str(int(time_list[0])-12)
    output = ':'.join(time_list)
    print(output[:-2])

if __name__ == '__main__':
    s = "07:05:45PM"

    result = timeConversion(s)
