import string

"""
    def pangram: a string that contains every letter of the alphabet
"""
def pangrams(s):
    unique_characters = set(s.lower())
    for c in string.ascii_lowercase:
        if c not in unique_characters:
            return "not pangram"
    return "pangram"

assert(pangrams("We promptly judged antique ivory buckles for the next prize") == "pangram")
assert(pangrams("We promptly judged antique ivory buckles") == "not pangram")