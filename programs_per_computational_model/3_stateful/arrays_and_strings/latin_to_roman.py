"""
Context:
    Given:
        number in latin representation
Objective:
    Convert to roman numeral representation

Assumptions:
    valid number provided

Constraints:

Example:
    1245

Flow
    latin_numbers
    roman_numbers
    while number is not 0
        if <= number

Performance
    N = number
    LR = 1000
    Time = O(N/LR)

    Space = O((N/LR * 2)) characters
        *2 because average roman number is 2 characters
"""


def latin_to_roman(number):
    i = 12
    latin_numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_numbers = [
        "I",
        "IV",
        "V",
        "IX",
        "X",
        "XL",
        "L",
        "XC",
        "C",
        "CD",
        "D",
        "CM",
        "M",
    ]
    roman = ""
    while number != 0:
        # looking for a factor number's current value in set of latin_numbers
        if latin_numbers[i] <= number:
            number = number - latin_numbers[i]
            roman += roman_numbers[i]
        i -= 1
    return roman


print(latin_to_roman(1))  # I
print(latin_to_roman(6))  # VI
print(latin_to_roman(2))  # II
print(latin_to_roman(3))  # II
print(latin_to_roman(4))  # II
