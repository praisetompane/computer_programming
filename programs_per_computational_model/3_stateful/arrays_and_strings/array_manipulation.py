#!/bin/python3

import math
import os
import random
import re
import sys

"""
1 indexed array
    values = 0

list of operations
    for each element in array
        between some index range (inclusive)
            add a GIVEN value

    return maximum value in array
"""

"""
    array = [n]

    operationss = [
                x,y,z
                x,y,z
              ]
"""


def arrayManipulation(n, operations):
    """
     find max value in array

    time complexity
        Q = number of operations = queries : <= 200000
        QL = range length per op = a + b : <= 200000 * n ****
        N = number of elements in array = n

    ----------------------------------------------------------
        N for initialisation

        O(N * (Q * QL)) where QL <= N
        Therefore => O(N * N) = O(n^2)

        N for finding max

        Therefore: Quadratic = TOO slow!
    ----------------------------------------------------------

    array = [0 for _ in range(n)]
    for query in queries:
        for x in range(query[0], query[1] + 1):
            zeroIndex = x - 1
            array[zeroIndex] += query[2]
    return max(array)
    """

    """
    # this demarcates lower bound of range of n that will be get an addition of k 

    most_frequent_upper_bound =
    in all a,b
        find the b that occurs the most

    sum all k
        for operations where b >= most_frequent_upper_bound
    """
    print("Finding max sum")
    upper_bounds_frequency = {}
    most_frequent_upper_bound = operations[0][1]
    for op in operations:
        array_subset_last_index = op[1]
        if array_subset_last_index in upper_bounds_frequency:
            upper_bound = upper_bounds_frequency[array_subset_last_index]
            upper_bound[0] += 1
            upper_bound[1] += op[2]
        else:
            upper_bounds_frequency[array_subset_last_index] = [1, op[2]]

    for key in upper_bounds_frequency.keys():
        if (
            upper_bounds_frequency[key]
            > upper_bounds_frequency[most_frequent_upper_bound]
        ):
            most_frequent_upper_bound = key
    sum = 0
    if 1 == 1:
        print("No most_frequent_upper_bound found")
        # Sum ALL the numbers added to ALL upper bounds
    else:
        for op in operations:
            array_subset_last_index = op[1]
            if array_subset_last_index >= most_frequent_upper_bound:
                sum = sum + op[2]

    print("upper_bounds_frequency", upper_bounds_frequency)
    print("most_frequent_upper_bound ", most_frequent_upper_bound)
    return sum


print(
    "Print sum",
    arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100], [4, 5, 100]]),
)

"""
    1   2   3   4   5
    100 100
        100 100 100 100
            100 100
"""
print("Print sum", arrayManipulation(5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]))

"""                     
testData = open("test8.data", "r")
n = 10000000
m = 100000
print("Gathering operations")
operations = []
for _ in range(m):
    operationss.append(list(map(int, testData.readline().rstrip().split())))
print("Summing")
result = arrayManipulation(n, operations)
print(result)
print("Done")

"""
