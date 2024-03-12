"""
    input = string
    objective = determine if input is
                    a permutation of
                        a palindrome

    definitions:
        permutaion:
            For two strings to be permutations of each other, they must contain the same:
                - characters 
                        characters include all possible characters in Unicode char set (whitespace etc)
                - number of characters

        palindrome:
            a word/phrase
                same
                    backwards AND forwards
            What is required to write a set of characters the SAME way backwards AND forwards?
                #Note to self => The character/string questions treat them as a set (a/A to z/Z)

                Even number of characters
                Maximum of one odd character(for the middle)

    question: can the input string be rewritten
                so the new string(permutation)
                    is a palindrome(i.e. reads the same forwards and backwards)?

"""


def build_character_frequency(string_input):
    def get_character_number(character):
        z_ascii_number = ord("z")
        a_ascii_number = ord("a")
        character_ascii_number = ord(character)
        if (
            a_ascii_number <= character_ascii_number
            and character_ascii_number <= z_ascii_number
        ):
            return (
                character_ascii_number - a_ascii_number
            )  # not sure about this substraction
        return -1  # non letter

    number_of_characters = 26
    table = [0] * number_of_characters
    for c in string_input:
        character_ascii_number = get_character_number(c.lower())
        if character_ascii_number != -1:
            table[character_ascii_number] = table[character_ascii_number] + 1
    return table


def is_palindrome_permutation(string_input):
    def has_max_one_odd_character(table):
        found_odd = False
        for count in table:
            if count % 2 == 1:
                if found_odd:
                    return False
                found_odd = True
        return True

    table = build_character_frequency(string_input)
    return has_max_one_odd_character(table)


print(is_palindrome_permutation("Tact Coa"))  # false
print(is_palindrome_permutation("act TCoa"))  # false
print(is_palindrome_permutation("A but tuba"))  # true
print(is_palindrome_permutation("ut tu Ab ba"))  # true
print(is_palindrome_permutation("u"))  # true
print(is_palindrome_permutation(""))  # true
print(is_palindrome_permutation("peter"))  # false

"""
    Performance
        N = length string

        Time = 𝑂(𝑁) + O(26) => 𝑂(𝑁)
            N to count all character occurences 
"""
