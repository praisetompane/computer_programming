#!/bin/python3

def _print_list_states(addition_start_index_marks: dict[int, int], size) -> None:
    """Useful for visualizing.

    Args:
        dict[int: index, int: value]: operation application markings
        size (int): number of elements in the array.
    Returns: None

        NB: at the large input values of size_of_list and addition_start_index_marks, it will be slow, because it is 

        O(M*N), where
            M = size_of_list - addition_start_index_marks.start : i.e. longest range
            N = size_of_list
    """
    print(f"{addition_start_index_marks=}\n")
    list_values = [0] * size
    print(f"{list_values=}")
    for i in sorted(addition_start_index_marks.keys()):
        n_inclusive_end_index = n+1
        for j in range(i, n_inclusive_end_index):
            if j < n_inclusive_end_index:
                # values[j-1], because the list_values is 0 index, but the operations(e.g. {1: 100}) encoded in the addition_start_index_marks are 1 indexed.
                list_values[j-1] += addition_start_index_marks[i]
        print(list_values)


def construct_manipulation_instructions(operation_requests):
    """Constructs the operation_start_index_marks data structure

    Steps to construct operation_start_index_marks:
        1. mark adding 'value' from index 'start_index' to the end of the array.
        2. mark adding '-value' from index ('stop_index' + 1) to the end of the array, because you only need to add 'value' until index 'stop_index'(as per the query('stop_index') parameter).
        You are actually subtracting the unnecessary 'value' you added, to reset the array values to their previous state from index 'stop_index'+1 until the end.

    Args:
        operation_requests ([start_index: int, stop_index: int, value: int]): operation to apply to array. Defaulted to addition.

    Returns:
        dict[int: index, int: value]: operation application markings.

    Detailed Explanation:
        operation_start_index_marks data structure:
            - data structure meaning:
                This data structure encodes marking an index(𝑥) from which to add some value(𝑘) until the end of the array.
            - data structure usage:
                Example:
                    given:
                        n = 5, therefore, values = [0, 0, 0, 0, 0]
                        queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
                        addition_start_index_marks = {1: 100, 2: 100, 3: 0, 5: -100, 6: -100}
                    then:
                        apply query/operation: [1, 2, 100]
                            NB: we subtract -1 from the indices when applying them to an actual array, because the commands {𝑥 = 2: 100} are 1 indexed.
                                because lists are zero index.
                            1. {𝑥 = 1: 100} = add 100 from index 1-1 until the end of the array
                                ∴ values = [100, 100, 100, 100, 100]
                            2. {𝑥 = 2: 100} = add 100 from index 2-1 until the end of the array
                                ∴ values = [100, 100+100, 100+100, 100+100, 100+100]
                                ∴ values = [100, 200, 200, 200, 200]        
                            3. {𝑥 = 3: 0} = add 0 from index 3-1 until the end of the array
                                ∴ values = [100, 200, 200+0, 200+0, 200+0]
                                ∴ values = [100, 200, 200, 200, 200]    
                            4. {𝑥 = 5: -100} add -100 from index 5-1 until the end of the array
                                ∴ values = [100, 200, 200, 200, 200-100]   
                                ∴ values = [100, 200, 200, 200, 100]   
                            5. {𝑥 = 6: -100} add -100 from index 6-1 until the end of the array
                                ∴ values = [100, 200, 200, 200, 100]   
                                NB: Nothing is done, because index 6 is out of bounds of our array, which has length 5.
    """

    operation_start_index_marks = {}
    for start_index, stop_index, value in operation_requests:
        addition_index = start_index
        if start_index not in operation_start_index_marks:
            operation_start_index_marks[addition_index] = value
        else:
            # Increase the value to add to the array values, starting from index a
            operation_start_index_marks[addition_index] += value
        subtraction_index = stop_index + 1
        if subtraction_index not in operation_start_index_marks:
            operation_start_index_marks[subtraction_index] = -value
        else:
            # Increase the value to subtract from the array values, starting from index a
            operation_start_index_marks[subtraction_index] -= value
    return operation_start_index_marks


def arrayManipulation(n, queries):
    """ Calculate maximum value in array after applications of queries

    Args:
        n (int): size of the 1-index array
        queries ([start_index: int, stop_index: int, value: int]):  operation to apply to array.

    Returns:
        int: maximum value
    """
    operation_start_index_marks = construct_manipulation_instructions(queries)
    total_value_added_to_some_list_indices = 0
    highest_total_value_reached_in_some_list_indices = 0

    """ debugging visualization
        _print_list_states(operation_start_index_marks, n)
    """
    for i in sorted(operation_start_index_marks.keys()):
        total_value_added_to_some_list_indices += operation_start_index_marks[i]
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
    - Roy, A. 2023. https://www.techrbun.com/array-manipulation-hackerrank-solution/
    - Basumatary, V. 2020. https://www.thepoorcoder.com/hackerrank-array-manipulation-solution/
"""
