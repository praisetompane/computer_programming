def contain_all_unique_characters(s):
    letter_count = {}
    for i in range(0, len(s)):
        key = s[i]
        if key in letter_count:
            letter_count[key] += 1
        else:
            letter_count[key] = 1

        if letter_count[key] > 1:
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
        NC = length of letter count storage, NC <= N 

        Time = 𝑂(𝑁)
        Space = O(NC) = 𝑂(𝑁)
            Space required to represent the dictionary storing the letter count

"""
