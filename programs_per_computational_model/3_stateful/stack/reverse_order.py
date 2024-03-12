from impl.stack import Stack

"""
    general use case = reverse order
    Performance:
        N = length of item list
        Time = O(2 * N) = 𝑂(𝑁)
        Space = O(2 * N) = 𝑂(𝑁)
"""


def reverse_order(item_list):
    reverse_order = Stack()
    reversed = None
    for item in item_list:
        reverse_order.push(item)
    if type(item_list) == str:
        reversed = ""
        while reverse_order.is_empty() is False:
            reversed += reverse_order.pop()
    else:
        reversed = []
        while reverse_order.is_empty() is False:
            reversed.append(reverse_order.pop())

    return reversed


def main():
    s1 = "apple"
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = ""
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = "racecar"
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = [1, 2, 3, 4, 5]
    print(s1, "reversed:", reverse_order(s1))
    s1 = []
    print(s1, "reversed:", reverse_order(s1))


if __name__ == "__main__":
    main()
