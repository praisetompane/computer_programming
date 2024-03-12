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
        if string empty: return empty
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
    compressed_string = ""
    count_consecutive = 0

    for i in range(string_length):
        count_consecutive = count_consecutive + 1
        if i + 1 >= string_length or string_input[i] != string_input[i + 1]:
            compressed_string = (
                compressed_string + string_input[i] + str(count_consecutive)
            )
            count_consecutive = 0

    if len(compressed_string) >= string_length:
        return string_input
    else:
        return compressed_string


print(compress("") == "")  # true
print(compress("aabcccccaaa") == "a2b1c5a3")  # true
print(compress("abcdef") == "abcdef")  # true  compressed same as original


"""
    Performance
        P = length of original string
        K = number of consecutive character sequences

        Time = O(P + K^2)
                K^2 because string concatenation is O(N^2)
                For each character sequence
                    we copy the compressed version and the current character sequence compression
                        into a new compressed string

                Why is concatenation O(N^2)?
                    X = length of current string
                    N = number of strings

                    1st iteration = 1X copy
                    2nd iteration = 2X copy
                    3rd iteration = 3X copy
                    Nth iteration = NX copy

                    O(1X + 2X + 3X ... NX) => O(N^2)
                    1 + 2 + ... N = N(N + 1)/2 = O(N^2 + N) => O(N^2)

        Space = O(2P) => O(P)
            Compressed string might be twice as long 
"""
