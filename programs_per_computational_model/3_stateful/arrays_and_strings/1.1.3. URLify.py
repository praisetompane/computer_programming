"""

    replace space
        with "%20" character

    design:
        interate though string characters
            if character == " "
                replace with "%20"

"""


def urlify(string):
    encoded = []
    for c in string:
        if c == " ":
            encoded.append("%20")
        else:
            encoded.append(c)
    return "".join(encoded)


print(urlify("Mr 3ohn Smith"))  # "Mr%203ohn%20Smith"


"""
    Performance
        N = length string

        Time = 𝑂(𝑁) 
        Space = 𝑂(𝑁)
            store list of characters from the orignal string, with spaces encoded
"""
