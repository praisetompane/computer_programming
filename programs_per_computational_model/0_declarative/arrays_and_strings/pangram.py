import string

"""
    def pangram: a string that contains every letter of the alphabet
"""


def is_subset(s):
    universe = set(s.lower())  # not necessary, this is for set use explicitness
    fixed_domain = set(string.ascii_lowercase)
    if fixed_domain.issubset(universe):
        return "pangram"
    return "not pangram"


assert (
    is_subset("We promptly judged antique ivory buckles for the next prize")
    == "pangram"
)
assert is_subset("We promptly judged antique ivory buckles") == "not pangram"
