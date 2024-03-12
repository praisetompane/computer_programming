"""
    Context:
        Given:
            integer array
    
    Objective: 
        calculate ratio of numbers that are:
            positive
            negative
            and zero
        print ratio for each number set on new line(in the order mentioned above)
            6 deciaml precision
    
    Constraint:
        >= 10^4 and <= 10^6 precision
        0 < n <= 100: size of array
        -100 <= arr[i] <= 100: range of values
        
    Example:
        [1,1,0,-1,-1]
        n = 5, number of elements
        
        positive: 2/5 = 0.4000000
        negative: 2/5 = 0.4000000
        zero:     1/5 = 0.2000000
        
    Flow
        array_size = len(arr)
        positive_count = 0
        negative_count = 0
        zero_count = 0
        
        #count positive, negative and zero values in array
        for value in arr
            if value > 0: positive_count += 1
            elif value < 0: negative_count += 1 
            else: zero_count += 1
        
        print positive_count/array_size
        print negative_count/array_size
        print zero_count/array_size
        
    Performance:
        N = number of elements in array
        𝑂(𝑁)
"""


def plusMinus(arr):
    array_size = len(arr)
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for value in arr:
        if value > 0:
            positive_count += 1
        elif value < 0:
            negative_count += 1
        else:
            zero_count += 1

    print("{:.6f}".format(positive_count / array_size))
    print("{:.6f}".format(negative_count / array_size))
    print("{:.6f}".format(zero_count / array_size))
