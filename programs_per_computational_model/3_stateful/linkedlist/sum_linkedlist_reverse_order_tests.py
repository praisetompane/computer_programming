import unittest

from impl.linkedlist import LinkedList
from sum_linkedlist_reverse_order import add


class SumLinkedListTests(unittest.TestCase):
    def test_add_equal_length(self):
        first = LinkedList()
        first.initialise_from_array([7, 1, 6])

        second = LinkedList()
        second.initialise_from_array([5, 9, 2])

        result = add(first, second)
        self.assertEqual(219, result.toInt(), "617 + 295 = 912 in forward order")

    def test_add_equal_length_with_carry(self):
        first = LinkedList()
        first.initialise_from_array([7, 1, 6])

        second = LinkedList()
        second.initialise_from_array([5, 9, 3])

        result = add(first, second)
        self.assertEqual(2101, result.toInt(), "617 + 395 = 1012 in forward order")

    def test_add_different_length(self):
        first = LinkedList()
        first.initialise_from_array([7, 1])

        second = LinkedList()
        second.initialise_from_array([5, 9, 2])

        result = add(first, second)
        self.assertEqual(213, result.toInt(), "17 + 295 = 312 in forward order")

    def test_add_single_with_carry(self):
        first = LinkedList()
        first.initialise_from_array([7])

        second = LinkedList()
        second.initialise_from_array([5])

        result = add(first, second)
        self.assertEqual(21, result.toInt(), "7 + 5 = 12 in forward order")

    def test_add_single_with_no_carry(self):
        first = LinkedList()
        first.initialise_from_array([7])

        second = LinkedList()
        second.initialise_from_array([1])

        result = add(first, second)
        self.assertEqual(8, result.toInt(), "7 + 1 = 8 in forward order")
        return

    def test_add_empty(self):
        first = LinkedList()
        first.initialise_from_array([])

        second = LinkedList()
        second.initialise_from_array([])

        result = add(first, second)
        self.assertEqual(0, result.toInt(), "empty + empty = empty 0")
        return


if __name__ == "__main__":
    unittest.main()
