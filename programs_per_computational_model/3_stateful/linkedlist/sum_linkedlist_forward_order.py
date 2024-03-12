"""
    Context:
        Given two numbers represented as a
            each represented as a (singly)linkedlist

    Objective:
        Write function that: 
            adds the two numbers
            returns sum as linkedlist

    Defintions:

    Constraints:

    Assumptions:
        base 10 number system
    Example:

        input = (6 -> 1 -> 7) + (2 -> 9 -> 5)
        output = (9 -> 1 -> 2)

    Options:
        1: Use doubly linked list
            keep pointer to head and tail
            for forward addition
                start from the tail.
            I CHOOSE THIS ONE, as per the book progression I do not know Stacks yet! :)
        2. Use stacks
            convert the linked list into stacks
                - Can be:
                    - a node based stack
                    - a list based stack
                7   5
                1   9
                6   2
                    removing the head and add it to stack
                    the last value(i.e. ones places will be the first values we process(i.e.))
                Each place value addition result is added to a stack
                    We'll start at the ones,
                    therefore the highest place value(i.e. will be the last inserted, thus the first removed when 
                    converting the result to integer)
            result stack
                9
                1
                2
                which is equal to 912

"""
from impl.linkedlist_doubly import LinkedListDoubly


def add(first_number, second_number):
    number_system_base = 10
    carry = 0
    result = LinkedListDoubly()

    d1 = first_number.tail
    d2 = second_number.tail

    def a(d1=0, d2=0, carry=0):
        sum = d1 + d2 + carry
        next_digit = sum % number_system_base
        result.add(next_digit)
        return sum // number_system_base

    while d1 is not None or d2 is not None:
        if d1 is not None and d2 is not None:
            carry = a(d1.data, d2.data, carry)
            d1 = d1.prev
            d2 = d2.prev
        elif d1 is not None and d2 is None:
            carry = a(d1.data, 0, carry)
            d1 = d1.prev
        elif d2 is not None and d1 is None:
            carry = a(d2.data, 0, carry)
            d2 = d2.prev

    if carry > 0:
        result.add(carry)
    return result


if __name__ == "__main__":
    print(
        "supply numbers with the place value schema: ones tens hundreds thounsands .."
    )
    first_number = input("first number: ")
    second_number = input("second number: ")
    print("adding %s and %s", (first_number, second_number))

    first_numberList = [int(n) for n in first_number]
    second_numberList = [int(n) for n in second_number]

    add(first_numberList, second_numberList).toString()
