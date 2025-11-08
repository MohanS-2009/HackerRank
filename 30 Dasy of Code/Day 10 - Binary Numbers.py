#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    binary_rep = bin(n)[2:]
    
    # Split binary string by '0' and find the longest group of '1's
    consecutive_ones = binary_rep.split('0')
    max_consecutive = max(len(group) for group in consecutive_ones)
    
    print(max_consecutive)