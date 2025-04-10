"""
reference: Demaine E. Devadas S. 2011. MIT 6.006 Introduction To Algorithms. Lecture 1: Algorithmic Thinking, Peak Finding.
Context:
    peak finder
        1 dimensional
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        [ 1,   2,   3,   4,   5,   6,   7,   8,   9]

        runs on array of numbers(integers) with indexed positions
            a to i are numbers
            with positions 1 to 9


objective: find peak, if it exists

definitions:
    position 2 is a peak
        if and only if
        b >= a AND b >= c
        for edges
            position_edge is a peak
            if and only if
                position_edge >= its side{leftside or rightside depending on where the edge is}

algorithms:
    straightforward_algorithm:
        start from left
            run compare
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        [ 1,   2,... N/2,...,N - 1,   N]

        Performance:
            Worst case: θ(N) => Theta N
                        N = number of  elements

    binarysearch_algorithm:
        ...


"""


def generate_char_and_index():
    number_of_letters = 9
    letters = [chr(c) for c in range(ord("a"), ord("a") + number_of_letters)]
    indices = [n for n in range(1, number_of_letters + 1)]
    print(letters)
    print(indices)
