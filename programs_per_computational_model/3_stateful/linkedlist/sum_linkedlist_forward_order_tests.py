import unittest

from impl.linkedlist_doubly import LinkedListDoubly
from sum_linkedlist_forward_order import add


class SumLinkedListForwardOrder(unittest.TestCase):
    def test_add_equal_length_same_length_result(self):
        result = add(LinkedListDoubly([6, 1, 7]), LinkedListDoubly([2, 9, 5]))
        self.assertEqual(912, result.toInt(), "617 + 295 = 912")

    def test_add_equal_length(self):
        result = add(LinkedListDoubly([1, 2, 8]), LinkedListDoubly([9, 8, 3]))
        self.assertEqual(1111, result.toInt(), "128 + 983 = 1111")

    def test_add_equal_length_with_carry(self):
        result = add(LinkedListDoubly([7, 1, 6]), LinkedListDoubly([5, 9, 3]))
        self.assertEqual(1309, result.toInt(), "617 + 395 = 1012")

    def test_add_different_length(self):
        result = add(LinkedListDoubly([1, 7]), LinkedListDoubly([2, 9, 5]))
        self.assertEqual(312, result.toInt(), "17 + 295 = 312")

    def test_add_single_with_carry(self):
        result = add(LinkedListDoubly([7]), LinkedListDoubly([5]))
        self.assertEqual(12, result.toInt(), "7 + 5 = 12")

    def test_add_single_with_no_carry(self):
        result = add(LinkedListDoubly([7]), LinkedListDoubly([1]))
        self.assertEqual(8, result.toInt(), "7 + 1 = 8")

    def test_add_empty(self):
        result = add(LinkedListDoubly([]), LinkedListDoubly([]))
        self.assertEqual(0, result.toInt(), "empty + empty = empty 0")


if __name__ == "__main__":
    unittest.main()
