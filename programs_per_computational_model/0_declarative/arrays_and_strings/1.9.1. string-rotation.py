"""
    Context:
        Given:
            method isSubstring
                checks if one word is a substring of another

    Definitions:
        rotation = letters moved n places left/right
            split string into two parts
                x,y
                rotated  string = yx
                original string = xy
            --------------------------------------
                s1 = abcd
                s2 = cdab

                s1
                    x = ab
                    y = cd
                    yx = cdab = s2

        is not:
            shuffling letters into arbitary positions
            
    Objective:
        Given two strings
            s1 and s2

        Write Algorithm to check
            if s2 is a 
                rotation
                    of s1
            
    Assumptions:
        s1 and s2 are same length
    Constraints:
        Only 1 call to isSubstring

    Algorithm flow:
        Using definition of rotation
            yxyx contains xy
            cdabcd contains abcd

        Flow:
            s2contact = concat s2 and s2
            check if s1 isSubstring of s2contact
    Possible Solutions
    
    Example(s):


"""


def string_rotation(s1, s2):
    def is_substring(search_string, source_string):
        return search_string in source_string

    return is_substring(s1, s2 + s2)


assert (string_rotation("waterbottle", "erbottlewat"))  # True
assert (string_rotation("abcd", "cdab"))  # True
assert (not string_rotation("abcd", "cdaob"))  # False
assert (not string_rotation("abcd", ""))  # False
print("completed successfully")

"""
    Performance
        N = length of 1 (where s2 == s3 in length)

        Time = O(2N + N) => 𝑂(𝑁)
             Time to concatenate s2 with itself and check if s1 is in s2

        Space = O(2N) => 𝑂(𝑁)
            Storage for concatenation of s2 by itself
"""
