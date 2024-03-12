#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
"""
    Context: Given 2D array
    
    Objective: Find the highest hour glass sum
    
    Definitions:
        hour glass := centre + 3 top nodes + 3 bottom nodes
        
        top_nodes:
            top_left                = center_row - 1, center_col - 1
            top_moddle              = center_row - 1, center_col
            top_right               = center_row - 1, center_col + 1
        
        bottom_nodes:
            bottom_left             = center_row + 1, center_col - 1
            bottom_middle           = center_row + 1, center_col
            bottom_right            = center_row + 1, center_col + 1
            
    Assumptions:
        array is always 6 * 6
         \therefore always have 16 hour glasses
                   
    Flow:
        Start_center = [1][1]
        for every center 
            [increment center_col by 1 until 4] : 4 is last valid center
                reset to next row start center at end
                
            hour_glass_sum= center + top_nodes + bottom_nodes
            if hour_glass_sum > max
                max = hour_glass_sum
                
    Performance:    
        NR = number of center rows = 6 - 2 = 4 
        NC = number of center cols = 6 - 2 = 4
        O(NR * NC) = O(4 * 4) = O(16) = O(1)
        
        Eligible centers are compose of:
            cols at least 1 index from boarder
            rows at least 1 index from boarder
"""


def hourglassSum(arr):
    hour_glass_sum_max = -9 * 7
    excluded_indices = 1
    max_index = len(arr[0]) - excluded_indices
    print(max_index)

    def sum_hour_glass(center):
        def sum_row(row, col):
            return arr[row][col - 1] + arr[row][col] + arr[row][col + 1]

        row = center[0]
        col = center[1]
        return arr[row][col] + sum_row(row - 1, col) + sum_row(row + 1, col)

    for row in range(1, max_index):
        for col in range(1, max_index):
            current_center = [row, col]
            hourglasssum = sum_hour_glass(current_center)
            if hourglasssum > hour_glass_sum_max:
                hour_glass_sum_max = hourglasssum
    return hour_glass_sum_max


"""
 input example: 
        0 -4 -6 0 -7 -6
        -1 -2 -6 -8 -3 -1
        -8 -4 -2 -8 -8 -6
        -3 -1 -2 -5 -7 -4
        -3 -5 -3 -6 -6 -6
        -3 -6 0 -8 -6 -7
"""
if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    result = hourglassSum(arr)
    print(f"max sum {result}")
