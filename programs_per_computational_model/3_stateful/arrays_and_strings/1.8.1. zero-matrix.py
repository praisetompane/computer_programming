"""
    Context:
        Given an M*N matrix

    Definitions:

    Objective:
        In a matrix(M*N)
            set the entire row and column to zero
                if any point in the row or col is zero

    Assumptions:

    Constraints:

    Algorithm flow:
        for each point (row,col) in grid
            if point is zero
                for each point in point's row
                    set each point to zero in result matrix
                for each point in point's col
                    set each point to zerp in result matix
    
    Possible Solutions
    
    Example(s):
        N = 4
        Matrix:
            110
            111
            011
            111

        Result
            000
            010
            000
            010

"""


def zero_matrix(source_matrix):
    number_of_rows = len(source_matrix)
    number_of_cols = len(source_matrix[0])
    result = [
        [source_matrix[row][col] for col in range(number_of_cols)]
        for row in range(number_of_rows)
    ]

    def set_row_to_zero(row):
        for col in range(number_of_cols):
            result[row][col] = 0

    def set_col_to_zero(col):
        for row in range(number_of_rows):
            result[row][col] = 0

    for row in range(number_of_rows):
        for col in range(number_of_cols):
            if source_matrix[row][col] == 0:
                set_row_to_zero(row)
                set_col_to_zero(col)

    return result


source = [[1, 1, 0], [1, 1, 1], [0, 1, 1], [1, 1, 1]]

assert(zero_matrix(source) == [[0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0]])

source = [[1, 1, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1]]

assert(zero_matrix(source) == [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0]])

print("completed successfully")
""" 
    Performance
        M = rows
        N = cols
        
        Time = O(M*N) 
            We have to inspect every element in the matrix
        Space = O(M*N)    
            Storage for resulting matrix
"""
