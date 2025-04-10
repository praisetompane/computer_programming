"""
For two strings to be permutations of each other, they must contain the same:
    - characters
            characters include all possible characters in Unicode char set (whitespace etc)
    - number of characters

"""


def are_permutations(string_1, string_2):
    return sorted(string_1) == sorted(string_2)


print(are_permutations("gofreetech", "haha"))  # false
print(are_permutations("abc", "bca "))  # false
print(are_permutations("python", "onpyth"))  # true
print(are_permutations("python", "oNpyth"))  # false
print(are_permutations("p", "p"))  # true
print(are_permutations("", ""))  # true


"""
    Performance
        SL1 = length of first string
        SL2 = length of second string

        Time = O(SL1 log SL1) + O(SL2 log SL2) + O(SL1) + O(SL2) => O(SL1 + SL2) 
            O(SL1 log SL1) sort first string
            O(SL2 log SL2) sort second string

            Therefore O(SL1 + SL2), as this is the dominant term
"""
