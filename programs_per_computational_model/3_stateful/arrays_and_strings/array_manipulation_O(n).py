#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
"""
    for all a, b, k:
        set instruction to increment by k:
            from index a to index n: HOW? 
                    mark where the increase by k must start with k(i.e. array[a] = 100)
                BUT since we actually ONLY want to increment by until index b
                    set instruction to decrement by k from {b + 1 to n} HOW?
                        mark where the decrease by k must start with -k(i.e. array[b+1] = -k)
                    
    NB: Since we are not actually going from a to b<=n
        the cost of setting the instruction to:
            increment by k
            decrement by k
            is O(1)
    
"""

"""
    array = [n]

    queries = [
                x,y,z
                x,y,z
              ]
"""


def arrayManipulation(n, queries):
    sums = [0] * (n + 1)
    for query in queries:
        k = query[2]
        # set start index from where all indices are incremented by k
        zero_based_start = query[0] - 1
        sums[zero_based_start] += k
        # set start index from where all indices are decremented by k
        sums[query[1]] += -k
        # print(f'a = {query[0]} b = {query[1]} and sums = {sums}')

    max_consective_increase = 0
    # print(f'susm final {sums}')
    for i in range(len(sums)):
        if max_consective_increase < max_consective_increase + sums[i]:
            max_consective_increase = max_consective_increase + sums[i]

    return max_consective_increase


if __name__ == "__main__":
    print("first problem")
    n = 5
    m = 3
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    result = arrayManipulation(n, queries)
    print(result)
    assert result == 200

    print("second problem")
    n = 10
    m = 4
    queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]
    result = arrayManipulation(n, queries)
    print(result)
    assert result == 31

    print("third problem")
    n = 10000000
    m = 100000
    with open("array_manipulation_data_10000000_100000.txt", "r") as file:
        all_lines = file.readline()
        nm = all_lines.split()

        n = int(nm[0])
        m = int(nm[1])

        queries = []
        for i in range(m):
            queries.append(list(map(int, file.readline().rsplit())))
        result = arrayManipulation(n, queries)

    result = arrayManipulation(n, queries)
    print(result)
    assert result == 2497169732
