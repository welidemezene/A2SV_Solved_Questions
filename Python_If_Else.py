#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    if n % 2 == 0:
        if n >= 6:
            if n<= 20:
                print("Weird")   
    if n % 2 == 0:
        if n > 20:
            print("Not Weird")
    if n % 2 ==0:           
        if n >=2:
            if n<=5:
                print("Not Weird")                 