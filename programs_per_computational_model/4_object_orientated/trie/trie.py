"""
implement subset of english dictionary
"""


class Letter:
    next_letters = []
    is_final_letter_in_word = False

    def __init__(self, next_letters, is_final_letter_in_word):
        self.next_letters = next_letters
        self.is_final_letter_in_word = is_final_letter_in_word
