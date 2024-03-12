def search_reducing_search_space(search_string, search_space):
    search_string_length = len(search_string)
    search_string_index = 0

    for i in range(0, len(search_space)):
        if search_string_index < search_string_length:
            if search_space[i] == search_string[search_string_index]:
                search_string_index += 1
    return search_string_index == search_string_length


search_string = "hackerrank"
assert search_reducing_search_space(search_string, "hereiamstackerrank") == True
assert search_reducing_search_space(search_string, "hackerworld") == False
print("successfully completed")