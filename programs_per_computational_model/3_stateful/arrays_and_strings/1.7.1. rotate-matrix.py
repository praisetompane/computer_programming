"""
Context:
    Given Image
        Represented by N*N matrix
        Each pixel = 4bytes

Definitions:
    Rotate by 90 degrees?

Objective:
    Function to rotate the image 90 degrees

Assumptions:
    Rotation is clockwise

Constraints:

Algorithm flow:
    Clockwise Rotation => x, y : Cartesian
        (x,y) => (y, -1*x)

    Map to Matrix => x,y
        (x, y) => (abs(x),abs(y))

    create new matrix N*N matrix
    for each point (row,col) in grid
        new_cartesian_point = apply Clockwise Rotation above
        matrix_point = apply  Map to Matrix
        set matrix_point to value at (row,col)

Possible Solutions

Example(s):
    N = 4
    New Image:
        XXX
        XXX
        XXX

    Current Image:
        ABC  (0,0)(0,1)(0,2)
        EFG  (1,0)(1,1)(1,2)
        IJK  (2,0)(2,1)(2,2)

    Result:

        AEI
        BFJ
        CGK

"""

"""
    References:
    2D array = https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
    List comprehensions: https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
"""


def rotate_90_degrees(image):
    """rotate_on_cartesian_plane is added for explicitness
    I could just use generate the result of map_to_matrix_point in rotate_on_cartesian_plane
    """

    def rotate_on_cartesian_plane(point):
        return (point[1], -1 * point[0])

    def map_to_matrix_point(point):
        return (abs(point[1]), abs(point[0]))

    size = len(image)
    new_image = [[image[0][0] for _ in range(size)] for _ in range(size)]

    for row in range(size):
        for col in range(size):
            matrix_point = map_to_matrix_point(rotate_on_cartesian_plane((col, row)))
            new_image[matrix_point[0]][matrix_point[1]] = image[row][col]
    return new_image


image = [["A", "B", "C"], ["E", "F", "G"], ["I", "J", "K"]]

print("original image: ")
print(image)
rotated_image = rotate_90_degrees(image)
print("rotated image: ")
print(rotated_image)

"""
    Performance
        N = number of rows/cols(Equal in this problem)

        Time = O(N*N) => O(N^2)
        Space = O(N*N)
"""
