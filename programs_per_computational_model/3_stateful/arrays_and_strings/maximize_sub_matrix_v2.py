#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
"""
    DRAFT
    Context:
        Given:
            game:
                data:
                    2n * 2n integer matrix
                
                actions:
                    reverse cols and rows arbitary times
                
                    goal: maximize sum of n*n submatrix
                        in upper-left quadrant
    Objective:
        return the maximal sum
            of uppper-left quadrant
            => maybe by reversing rows and cols
            
    Example:
        initial_matrix = [
                            [1, 2],
                            [3, 4]
                         ]
            2 * 2 matrix
            there upper-left quadrant = 1 * 1 : How??
            
        reverse row 1
            [
                [1, 2],
                [4, 3]
            ]
        reverse col 0
            [
                [4, 2]
                [1, 3]
            ]
        return matrix[0][0] = 4
        Performance:
            
    Flow:
        upper_left_quadrant_size = n * n
        max_values = [0] * upper_left_quadrant_size
        initialise matrix with first {upper_left_quadrant_size} numbers
        
        for num in matrix
            if number > any in max_values
                swap number with max_values
        return sum max_Values
    Constraints:
        1 <= q <= 16
        1 <= 
    Performance
        n = q = number of queries
        MS = Matrix size ,MS <= 2n * 2n
        UQS = Upper quadrant size, UQS <= n
        
        O(MS * UQS)
    
"""


# TODO rest
def flippingMatrix(matrix):
    n = len(matrix[0]) / 2
    upper_left_quadrant_size = n * n
    max_values = []
    for i in range(upper_left_quadrant_size):
        max_values.append(matrix[0][i])

    for row in matrix:
        for col in matrix:
            for i in range(upper_left_quadrant_size):
                if matrix[row][col] > matrix[i]:
                    matrix[i] = matrix[row][col]

    return sum(max_values)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + "\n")

    fptr.close()
