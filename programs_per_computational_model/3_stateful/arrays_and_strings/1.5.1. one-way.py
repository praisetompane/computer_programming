"""
    Context:
        Three edits on a string
            insert a character
            remove a character
            replace a character
    Objective:
        Given two strings
            check if they are
                one edit
                or zero edits
                away

    algorithm flow:
            if string_1 is longer than string_2 #insert and remove (since removal is inverse of insertion)
                from string_1 
                    remove one character at a time
                        compare to string_2
                            return when string_1 equals string_2
                            move to next character if not equal
            if string_1 is not longer than string_2 #insert and remove
                from string_2
                    remove one character at a time
                    compare to string_1
                            return when string_1 equals string_2
                            move to next character if not equal
            if string_1 length is equal string_2
                check that only one character is different
            
    Example:
        pale, ple -> true #removal/insertion 

            rm p
            ale == ple? false
            rm a
            ple ==ple? true

        pale, bake -> false
            b and k different in string_2 => false

        pale, bale -> true
            b different in string_2 => true

"""


def determine_if_only_one_change_exists(long_string, long_string_length, short_string):
    for i in range(long_string_length):
        if long_string[:i] + long_string[i + 1:] == short_string:
            return True
    return False


def one_away(string_1, string_2):
    string_1_length = len(string_1)
    string_2_length = len(string_2)
    if abs(string_1_length - string_2_length) > 1:
        return False
    if string_1_length > string_2_length:
        return determine_if_only_one_change_exists(string_1, string_1_length, string_2)
    if string_2_length > string_1_length:
        return determine_if_only_one_change_exists(string_2, string_2_length, string_1)
    if string_1_length == string_2_length:
        found_mismatch = False
        for i in range(string_1_length):
            if string_1[i] != string_2[i]:
                if found_mismatch:
                    return False
                found_mismatch = True
        return True


print(one_away("pale", "ple"))  # true
print(one_away("pale", "bake"))  # false
print(one_away("pale", "bale"))  # true
print(one_away("pales", "pale"))  # true
print(one_away("pales", "ple"))  # false


"""
    Performance
        N, Where N is the length of the longest string

        Time = 𝑂(𝑁)
"""
