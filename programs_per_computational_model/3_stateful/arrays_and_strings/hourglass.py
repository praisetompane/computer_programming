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
    current_center = [1, 1]
    max_row_and_col = len(arr[0]) - 1

    def sum_row_nodes(center_row, center_col):
        nodes_sum = (
            arr[center_row][center_col - 1]
            + arr[center_row][center_col]
            + arr[center_row][center_col + 1]
        )
        return nodes_sum

    def sum_hour_glass(current_center):
        top_row_sum = sum_row_nodes(current_center[0] - 1, current_center[1])
        bottom_row_sum = sum_row_nodes(current_center[0] + 1, current_center[1])
        hour_glass_sum = (
            arr[current_center[0]][current_center[1]] + top_row_sum + bottom_row_sum
        )
        return hour_glass_sum

    hour_glass_max = sum_hour_glass(
        current_center
    )  # or 7 * -9 = -63 : minimum taol hour glass sum
    current_center[1] += 1

    while current_center[0] < max_row_and_col:
        hour_glass_sum = sum_hour_glass(current_center)
        current_center[1] += 1
        if hour_glass_sum > hour_glass_max:
            hour_glass_max = hour_glass_sum

        if current_center[1] == max_row_and_col:
            current_center[0] += 1
            current_center[1] = 1
    return hour_glass_max


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
