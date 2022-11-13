#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cp=cn=cz=0
    for a in arr:
        if a>0:
            cp+=1
        elif a<0:
            cn+=1
        else:
            cz+=1
    print(f'{cp/len(arr):.6f}',round(cn/len(arr),6),round(cz/len(arr),6),sep="\n")
        
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
