def count_in_order_character_occurence(string_input):
    char_count = 0
    char_counts = []
    last_char_seen = ""

    idx = 0
    while idx < len(string_input):
        last_char_seen = string_input[idx]
        while idx < len(string_input) and string_input[idx] == last_char_seen:
            char_count += 1
            idx += 1
        char_counts.append((last_char_seen, char_count))
        char_count = 0

    return char_counts


if __name__ == "__main__":
    assert count_in_order_character_occurence("aaaabbbcca") == [
        ("a", 4),
        ("b", 3),
        ("c", 2),
        ("a", 1),
    ]
