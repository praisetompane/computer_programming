def search_substring(s):
    subtring = "SOS"
    subtring_last_index = 2
    subtring_index = 0
    mutated_characters = 0

    for message_char in s:
        if message_char != subtring[subtring_index]:
            mutated_characters += 1
        if subtring_index < subtring_last_index:
            subtring_index += 1
        else:
            subtring_index = 0

    return mutated_characters


assert search_substring("SOSSPSSQSSOR") == 3
assert search_substring("SOSSOT") == 1
print("successfully completed")
