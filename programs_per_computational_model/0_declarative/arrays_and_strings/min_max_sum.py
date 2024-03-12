"""
    Context: 
        Given:
            five positive integers
            
    Objective:
        find:
            minimum sum of four of the integers
            maximum sum of four of the integers
        print the min and max
            on one line, space separated
        
    Example:
        [1,3,5,7,9]
        min_sum = 1 + 3 + 5 + 7
        max_xum = 3 + 5 + 7 + 9
          
    Assumptions():?
        Is array always sorted? No mention, there assume it's not
        output can 32 bit integer
        
    Constraints:
        1 <= arr[i] <= 10^9 : array value range 
        require 64 bit integer
        
    Flow:
        sort array
        array_size = 5
        min_sum = sum(arr[:array_size])
        max_sum = sum(arr[2:])
        print(min_sum max_sum)
    
    Performance 
        N = size of array
        S = O(NlogN): sorting time
        MIS = O(N - 1) = 𝑂(𝑁) : minimum sum
        MAS = O(N - 1) = 𝑂(𝑁) : maximum sum

        𝑂(𝑁𝑙𝑜𝑔𝑁 + 𝑁)
"""


def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    array_size = 5
    min_sum = sum(arr_sorted[: array_size - 1])
    max_sum = sum(arr_sorted[1:])
    print(f"{min_sum} {max_sum}")
