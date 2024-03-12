"""
    Context:
        Given Image
            Represented by N*N matrix
            Each pixel = 4bytes

    Definitions:
        Rotate by 90 degrees? 
            = (x,y) => (y, -x)

    Objective:
        Function to rotate the image 90 degrees
       
    Assumptions:
        Rotation is clockwise

    Constraints:

    Algorithm flow:
        Clockwise Rotation => (x,y) => (y, -x)
        
        create swapped hash table

        for each point (row,col) in grid
            if not in swapped
                new_cartesian_point = apply Clockwise Rotation above
                matrix_point = apply  Map to Matrix
                swap values at (row, col) with values matrix point
                add (row, col) and matrix point to swapped

    Possible Solutions
    
    Example(s):
        N = 4
        New Image:
            XXX
            XXX
            XXX
        Swapped = (0,0)
                  (O,1)
                  (1,0)
                  (0,2)
                  (2,0) 
                  (1,1)
                  (1,2)
                  (2,1)
                  (2,2)
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
    def rotate(point):
        return (point[1], point[0])

    def swap(source_point, target_point):
        temp = image[target_point[0]][target_point[1]]
        image[target_point[0]][target_point[1]] = image[source_point[0]][
            source_point[1]
        ]
        image[source_point[0]][source_point[1]] = temp

    swapped = {}
    size = len(image)
    points = [(row, col) for row in range(size) for col in range(size)]

    for p in points:
        if p not in swapped:
            matrix_point = rotate(p)
            swap(p, matrix_point)
            swapped[matrix_point] = 1
            swapped[p] = 1
    return image


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
            Matrix is N*N in size
                and we need to touch each point in the matrix
        Space = O(N*N)  
            Space to store all the points in the matrix 
"""
