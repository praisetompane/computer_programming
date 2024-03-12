#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    length = len(q)
    swaps = 0
    MAX_BRIBES = 2
    swapped = False
    for i in range(length):
        for j in range(0, length - i - 1):
            if q[j] - (j + 1) > MAX_BRIBES:
                swaps = None
                return swaps
            adjacent = j + 1
            if q[j] > q[adjacent]:
                temp = q[j]
                q[j] = q[adjacent]
                q[adjacent] = temp
                swaps += 1
                swapped = True
        if swapped:
            swapped = False
        else:
            return swaps


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        bribes = minimumBribes(q)
        if bribes is None:
            print("Too chaotic")
        else:
            print(bribes)
