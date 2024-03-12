"""
    Context:
        Given:
            array of integers
                unsorted
            each element appears twice except for one
    Objective:
        Find the the unique element
        
    Example:
        a = [1,2,3,4,1,2,3]
        unique 4
    
    Assumtions:
        there will always be a lonlely integer (i.e. n will always be odd)
        
    Flow
        option 1: 𝑂(𝑁 + 𝑁) = O(2N) = 𝑂(𝑁)
            initialise empty hash occurances = array_value -> count
            for each value in a
                store count in occurances
            find entry(key) with only one occurances
            CHOSE THIS ONE
        Option 2: 𝑂(𝑁𝑙𝑜𝑔𝑁 + 𝑁)
            sort
            return number whose adjacent is not equal to itself
        
        Option 3: 𝑂(𝑁) + O(1) = 𝑂(𝑁) = WRONG THOUGH
            Since an odd number + odd number = even
                  an even number + odd number = even    
                  sum of n(which odd) is going to be odd
                  
            lonlely_integer = sum(a)%2
            
    Constraints: 
        1 <= n <= 100: size of the array
        0 <= arr[i] <= 100, where 0 <= i <= 100(n) 

    Performance

"""


def lonelyinteger(a):
    occurances = {}
    for number in a:
        if number in occurances:
            occurances[number] += 1
        else:
            occurances[number] = 1
    for n in occurances.items():
        if n[1] == 1:
            return n[0]


def lonelyinteger(a):
    max_array_value = 100
    max_index_bound_exclusive = max_array_value + 1
    occurances = [0] * max_index_bound_exclusive

    for n in a:
        occurances[n] += 1
    for i in range(max_index_bound_exclusive):
        if occurances[i] == 1:
            return i
