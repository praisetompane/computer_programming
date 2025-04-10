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

    def _compress():
        character_count = 0
        current_character = string_input[0]
        compressed_string = ""
        last_index = string_length - 1

        for i in range(string_length):
            character = string_input[i]
            if character == current_character:
                character_count = character_count + 1

            if character != current_character or i == last_index:
                compressed_string = (
                    compressed_string + str(current_character) + str(character_count)
                )
                character_count = 1
                current_character = character
        return compressed_string

    if string_length == 0:
        return string_input
    else:
        compressed_string = _compress()
        if len(compressed_string) >= string_length:
            return string_input
        else:
            return compressed_string


print(compress("") == "")  # true
print(compress("aabcccccaaa") == "a2b1c5a3")  # true
print(compress("abcdef") == "abcdef")  # true  compressed same as original


"""
    Performance
        N = length of string
        Time = 𝑂(𝑁)
        Space = O(2N) => 𝑂(𝑁)
            Compressed string might be twice as long for 
"""
