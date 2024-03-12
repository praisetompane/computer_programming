#!/bin/python3

import math
import os
import random
import re
import sys

# source: https://github.com/RyanFehr/HackerRank/blob/master/Algorithms/Constructve%20Algorithms/Flipping%20Matrix/Solution.java

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
"""
    Given: 
        2n * 2n integer matrix
        
        can:
            reverse rows
            reverse cols
        goal:
            mazimize n * n submatrix(located in upper left quadrant)
            
        options : 
            random
                rotate a col
                    if sum(n*x upper left) > other quadrants
                        return
                    else:
                        rotate
                        if not
        
                        UL = 112 + 42 + 56 + 125   => 335
                        UR = 83 + 119 + 49 + 56    => 307
                        BR = 101 + 43 + 114 + 108  => 366
                        BL = 15 + 78 + 62 + 98     => 253
            bubble up max numbers:
                for all cols
                    if bottom number in col > top   
                        rotate col           
                if sum UL < UR
                    rotate row 0
        
        """


def flippingMatrix(matrix):
    last_index = len(matrix[0]) - 1
    n = len(matrix[0]) // 2
    top_row_index = 0
    # rotate max value to top of cols
    # rotate max value left of rows
    for col in range(len(matrix[0])):
        if matrix[top_row_index][col] < matrix[last_index][col]:
            rotate_col(col)
    upper_left_quadarant = matrix[top_row_index][0] + matrix[top_row_index][1]
    upper_right_quadarant = (
        matrix[top_row_index][last_index - 1] + matrix[top_row_index][last_index]
    )
    if upper_left_quadarant < upper_right_quadarant:
        rotate_row(top_row_index)

    upper_left_quadarant_sum = 0
    for row in range(n):
        for col in range(n):
            upper_left_quadarant_sum += matrix[row][col]
