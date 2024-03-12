def contain_all_unique_characters(s):
    sorted_version = sorted(s)
    string_length = len(s)
    last_index = string_length - 1
    for i in range(0, string_length):
        if i < last_index and sorted_version[i] == sorted_version[i + 1]:
            return False
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
        N = length of string

        Time = O( N log N + N)
            sort takes = N log N
        Space = 𝑂(𝑁)
            The space cost of the sorted array
"""
