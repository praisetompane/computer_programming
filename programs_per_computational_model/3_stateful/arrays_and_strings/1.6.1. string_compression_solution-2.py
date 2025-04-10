"""
Context:
    String compression
        using counts
            of repeated characters
Definitions:

Objective:

Assumptions:
    Only lower and upper case letters present

Constraints:

Inputs:
    string value

Algorithm flow:
    Compress the string
    if string empty: return emotty
    if length of compressed string >= original string
        return original string
    else
        return compressed string

Example(s):
    aabcccccaaa => a2b1c5a3

Possible Solutions
    character_count = 1
    current_character = set to first character in string
    compressed_string = ''
    for the length of string
        pick a character at current index
            compare character with current_character
                if same
                    increment character_count by 1
                if not
                    append current_character and character_count to character_count
                    set character_count to 1
                    set current_character = character

Walk through
    string length = 10
    current_character = a
    character_count = 3
    compressed_string = a2b1c5a3

"""


def compress(string_input):
    string_length = len(string_input)
    compressed_strings = []
    count_consecutive = 0

    for i in range(string_length):
        count_consecutive = count_consecutive + 1
        if i + 1 >= string_length or string_input[i] != string_input[i + 1]:
            compressed_strings.append(string_input[i] + str(count_consecutive))
            count_consecutive = 0

    compressed_string = "".join(compressed_strings)
    if len(compressed_string) >= string_length:
        return string_input
    else:
        return compressed_string


print(compress("") == "")  # true
print(compress("aabcccccaaa") == "a2b1c5a3")  # true
print(compress("abcdef") == "abcdef")  # true  compressed same as original


"""
    Reference: https://waymoot.org/home/python_string/
    Performance
        P = length of original string
        K = number of consecutive character sequences; K <= P
        Time = O(P)
        Space = O(K) => 𝑂(𝑁)
            
"""
