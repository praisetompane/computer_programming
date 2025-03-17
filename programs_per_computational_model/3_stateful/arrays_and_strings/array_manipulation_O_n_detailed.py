#!/bin/python3

# Complete the arrayManipulation function below.
'''
1 indexed array
    values = 0

list of operations
    for each element in array
        between some index range (inclusive)
            add a GIVEN value

    return maximum value in array
'''

'''
    array = [n]

    queries = [
                x,y,z
                x,y,z
              ]
'''

'''
 for query in queries
    for x in range(query[0], query[1])
        array[x] += query[2]

 find max value in array

'''


def _print_list_states(addition_start_index_marks, size_of_list):
    """
        useful for visualizing.
        NB: at the large input values of size_of_list and addition_start_index_marks, it will be slow, because it is 

        O(M*N), where
            M = size_of_list - addition_start_index_marks.start : i.e. longest range
            N = size_of_list
    """
    print(f"{addition_start_index_marks=}\n")
    list_values = [0] * size_of_list
    print(f"{list_values=}")
    for i in sorted(addition_start_index_marks.keys()):
        n_inclusive_end_index = n+1
        for j in range(i, n_inclusive_end_index):
            if j < n_inclusive_end_index:
                # values[j-1], because the list_values is 0 index, but the operations(e.g. {1: 100}) encoded in the addition_start_index_marks are 1 indexed.
                list_values[j-1] += addition_start_index_marks[i]
        print(list_values)


def construct_manipulation_instructions(mutation_requests):
    """
    Explanation:
        addition_start_index_marks data structure:
            - data structure meaning:
                This data structure encodes marking an index(𝑥) from which to add some value(𝑘) until the end of the list.
            - data structure usage:
                Example:
                    given:
                        n = 5, therefore, values = [0, 0, 0, 0, 0]
                        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
                        addition_start_index_marks = {1: 100, 2: 100, 3: 0, 5: -100, 6: -100}
                    then:
                        apply query/operation: [1, 2, 100]
                            NB: we subtract -1 from the indices when applying them to an actual list, because the commands {𝑥 = 2: 100} are 1 indexed.
                                because lists are zero index.
                            1. {𝑥 = 1: 100} = add 100 from index 1-1 until the end of the list
                                ∴ values = [100, 100, 100, 100, 100]
                            2. {𝑥 = 2: 100} = add 100 from index 2-1 until the end of the list
                                ∴ values = [100, 100+100, 100+100, 100+100, 100+100]
                                ∴ values = [100, 200, 200, 200, 200]        
                            3. {𝑥 = 3: 0} = add 0 from index 3-1 until the end of the list
                                ∴ values = [100, 200, 200+0, 200+0, 200+0]
                                ∴ values = [100, 200, 200, 200, 200]    
                            4. {𝑥 = 5: -100} add -100 from index 5-1 until the end of the list
                                ∴ values = [100, 200, 200, 200, 200-100]   
                                ∴ values = [100, 200, 200, 200, 100]   
                            5. {𝑥 = 6: -100} add -100 from index 6-1 until the end of the list
                                ∴ values = [100, 200, 200, 200, 100]   
                                NB: Nothing is done, because index 6 is out of bounds of our list, which has length 5.
    """
    addition_start_index_marks = {}
    for a, b, k in mutation_requests:
        """
        Steps to construct addition_start_index_marks:
            1. mark adding 𝑘 from index 𝑎 to the end of the list.
            2. mark adding -𝑘 from index (𝑏 + 1) to the end of the list, because you only need to add 𝑘 until index 𝑏(as per the query(𝑏) parameter).
                NB: You are actually subtracting the unnecessary 𝑘 you added, to reset the list values to their state from index 𝑏+1 until the end.
        """
        addition_index = a
        if a not in addition_start_index_marks:
            addition_start_index_marks[addition_index] = k
        else:
            # Increase the value to add to the list values, starting from index a
            addition_start_index_marks[addition_index] += k

        subtraction_index = b + 1
        if subtraction_index not in addition_start_index_marks:
            addition_start_index_marks[subtraction_index] = -k
        else:
            # Increase the value to subtract from the list values, starting from index a
            addition_start_index_marks[subtraction_index] -= k
    return addition_start_index_marks


def arrayManipulation(n, queries):
    addition_start_index_marks = construct_manipulation_instructions(queries)

    total_value_added_to_some_list_indices = 0
    highest_total_value_reached_in_some_list_indices = 0

    """
    _print_list_states(addition_start_index_marks, n)
    """
    for i in sorted(addition_start_index_marks.keys()):
        total_value_added_to_some_list_indices += addition_start_index_marks[i]
        highest_total_value_reached_in_some_list_indices = max(
            highest_total_value_reached_in_some_list_indices, total_value_added_to_some_list_indices)

    return highest_total_value_reached_in_some_list_indices


if __name__ == '__main__':
    with open("array_manipulation_data_10000000_100000.txt", 'r') as file:
        all_lines = file.readline()
        nm = all_lines.split()

        n = int(nm[0])
        m = int(nm[1])

        queries = []
        for i in range(m):
            queries.append(list(map(int, file.readline().rsplit())))
        result = arrayManipulation(n, queries)

        print(result)
        assert result == 2497169732

"""
References: 
    - https://www.techrbun.com/array-manipulation-hackerrank-solution/
    - https://www.thepoorcoder.com/hackerrank-array-manipulation-solution/
"""
