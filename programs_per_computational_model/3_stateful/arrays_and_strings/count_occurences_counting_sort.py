"""
    Given:
        array of integers
    Objective:
        return a frequency array of the elements
            count the number of times a value appears in the array
        NB: Aways return a 100 value frequency array 
    Assumptions:
    
    Example:
        arr = [1, 1, 3, 2, 1]
        values range = [0 ... 3]
        
    Flow
        frequencies = [0] * values range
        for n in arr:
            frequencies[n] += 1
        from the start of the array(i.e. index 0)
            append each index(i.e. the number) to sorted array
                as many times as stiputed by its frequncy    

    # => result will be a sorted array
    Constraints:
        100 <= n <= 10^6 : size of the array
        0 <= arr[i] < 100 range of values
    Performance
            𝑂(𝑁): we visit each array element
            O(100): initialise frequncy table of size 100
            O(N + 100) = 𝑂(𝑁) : drop constants
"""


def counting_sort(arr):
    max_value = 100
    max_index = 100 + 1
    frequencies = [0] * max_index
    arr_sorted = []
    for n in arr:
        frequencies[n] += 1
    for number in range(max_value):
        frequency = frequencies[number]
        for i in range(frequency):
            arr_sorted.append(number)
    return arr_sorted


def main():
    print(counting_sort([1, 8, 9, 22, 5, 89, 100]))
    print(counting_sort([]))
    print(counting_sort([1]))
    # limitattion, does not handle negatives correctly, beause negatives are
    # do not belong to the set of counting numbers = {1,2,3,4,5 ...}
    print(counting_sort([-1, 0, 9, 1]))
    print(counting_sort([9, -7, -1, 9]))


if __name__ == "__main__":
    main()
