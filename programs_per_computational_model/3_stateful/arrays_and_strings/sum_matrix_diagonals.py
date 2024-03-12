#
# Complete the 'diagonal_difference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""
    Context:
        Given:
            sqaure matrix
                i.e. width = lenght (e.g. 3 * 3)
    Objective:
        calculate the absolute difference  
            between sum of its diagonals
    
    Assmptions:
        matrix is never empty
    
    Constraints:
        -100 <= arr[i][j] <= 100
        
    Example:
        1 2 3
        4 5 6
        9 8 9
    
        left_diagonal  = 1 + 5 + 9 = 15
        right_diagonal = 3 + 5 + 9 = 17
        absolute_difference = |17 - 15| = 2
    
    Flow:
        left_diagonal = arr[0][0] + arr[1][1] + arr[2][2]
        right_diagonal = arr[2][0] + arr[1][2] + arr[0][2]
        absolute_difference = |left_diagonal - right_diagonal|
        return absolute_difference

    Performance:
        O(L). L is the dimension(either width or length of) of the matrix 
                             
"""


def diagonal_difference(arr):
    dimension = len(arr)
    max_index = dimension - 1
    left_diagonal_sum = 0
    right_diagonal_sum = 0

    # to sum the primary diagonal(top left to bottom right) of matrxix
    # increment row and col by 1
    # col is moving right, hence increment
    # row is moving down(increasing in depth) hence increment
    for i in range(dimension):
        left_diagonal_sum += arr[i][i]
    # to sum the secondary diagonal(bottom left to top right)
    # decrement the last row(maximum row) by 1
    # increment col by 1
    # col is moving right, hence increment
    # row is moving down(decreasing in depth) hence decrement
    for i in range(dimension):
        right_diagonal_sum += arr[max_index - i][i]
    return abs(left_diagonal_sum - right_diagonal_sum)
