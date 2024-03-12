"""
        For two strings to be permutations of each other, they must contain the same:
            - characters 
                    characters include all possible characters in Unicode char set (whitespace etc)
            - number of characters
        Constraints:
            - case senstivity matters
        Assumptions:
            - Strings will be ASCII encoded = 128 characters

"""


def are_permutations(string_1, string_2):
    if len(string_1) != len(string_2):
        return False  # optimisation, so we never need to sort
    else:
        ascii_character_set = [0] * 128
        for c in string_1:  # count characters in string_1
            ascii_number = ord(c)
            ascii_character_set[ascii_number] += 1

        for i in range(0, len(string_2) - 1):
            character = string_2[i]
            ascii_number = ord(character)
            ascii_character_set[ascii_number] -= 1
            if ascii_character_set[ascii_number] < 0:
                return False  # string_2 has more of this character
    return True


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

        Time = O(SL1 + SL2) 
"""
