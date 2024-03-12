def contain_all_unique_characters(s):
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
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

        Time = O(N^2)

"""
