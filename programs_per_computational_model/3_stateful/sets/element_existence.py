# Enter your code here. Read input from STDIN. Print output to STDOUT
"""

constraints:
    0 < n, m < 10⁵
    n = max length of intergers
    m = max number of elements in set_a and set_b

performance:
    O(n): load integers
    O(2m): load set_a and set_b
    ∴ O(n + 2m) = O(n + m)

    O(n) + O(1): iterate integers and check existence
    total asymptotic computational complexity: O(n)
"""
counter = 0
n, m = input().split(" ")
integers = input().split(" ")
set_a = set(input().split(" "))
set_b = set(input().split(" "))

for num in integers:
    """
    in operator is O(1) for sets, because items are hashed when stored in set.
    for each item x:
        key = hash_function(x): constant time to compute key
        store x this way: { key: x }: constant time append key-value pair into store

    for retrieval:
        key = hash_function(x): same constant time to compute key
        store[key]: constant time to access value for key. like an array index.
    """
    if num in set_a:
        counter += 1
    elif num in set_b:
        counter -= 1

print(counter)
