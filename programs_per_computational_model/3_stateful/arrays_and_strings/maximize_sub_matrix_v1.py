"""
DRAFT
Context:
    Given:
        2n * 2n matrix

Objective: maximize the upper left n * n quadrant
           rotating rows and cols

Example:
    n = 2 * 2 => 2(1) * 2(1) => n = 1
    n = len(matrix row) = 2/2 = 1
    [
        [1,2],
        [3,4],
    ]

    [
        [1,2],
        [4,3] *
    ]

    [
         *
        [4, 2],
        [1, 3]
    ]
    Key:
        * rot here

Flow:
    n = len(matrix row)//2

    for each col
        if sum(firt n numbers) < sum(last n numbers)
            rotate col
    for each row
        if sum(firt 2n numbers) < sum(last n numbers)
            rotate row

    sum the n * n matrix
    n_by_n_matrix_sum = 0

    for row in matrix:
        for col in matrix:
            n_by_n_matrix_sum += col

    return n_by_n_matrix_sum

Performance:
    NR = number of row = 2N
    𝑂(𝑁 + 𝑁) = O(2N) = visit top N and bottom N rows

    O(2N * 2N) => rotation cost

    NC = number of cols = 2N
    𝑂(𝑁 + 𝑁) = O(2N) = visit top N and bottom N cols

    O(2N + 2N)
        visit each col
"""


def flippingMatrix(matrix):
    matrix_szie = len(matrix[0])
    n = matrix_szie // 2
    # sum cols
    # sum rows

    for col in range(matrix_szie):
        for row in range(matrix_szie):
            first_n_elements_sum = matrix[row][col]
            last_n_elements_sum = 0

            if first_n_elements_sum < last_n_elements_sum:
                # rotate col
                pass
            # sum rows
    for row in matrix:
        if sum(row[:n]) < sum(row[-n:]):
            row.reverse()

    n_by_n_matrix_sum = 0
    for row in matrix[:n]:
        for col in matrix[:n]:
            n_by_n_matrix_sum += col

    return n_by_n_matrix_sum
