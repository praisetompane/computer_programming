"""
    Assumptions:
        The string uses 128 ASCII character set
"""


def contain_all_unique_characters(s):
    ascii_number_of_characters = 128
    characters = [False] * ascii_number_of_characters

    if len(s) > ascii_number_of_characters:
        return False  # s cannot have more than the possible unique ascii characters and still be unique
    else:
        for i in range(0, len(s) - 1):
            ascii_number = ord(s[i])
            if characters[ascii_number]:
                return False
            else:
                characters[ascii_number] = True
    return True


s1 = "gofreetech"  # false
print(contain_all_unique_characters(s1))

s2 = "python"  # true
print(contain_all_unique_characters(s2))

s3 = "p"  # true
print(contain_all_unique_characters(s3))

s4 = ""  # true
print(contain_all_unique_characters(s4))


"""
    Performance
        C = size of character set = 128
        N = length of string, N <= C


        Time = 𝑂(𝑁) = O(C)
        Space = O(C)
            128 for all runs, therefore constant 
            The space cost of the boolean array

        Could argue time and space complecity = O(1), as the for loop will never execute more than C

"""
