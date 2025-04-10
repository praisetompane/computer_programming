"""
abstract function to return subset of values
in interval [start_point, end_point]

members of values collection must have:
    - well defined ordering
        ∴ > , <, >=, >=, = definitions
"""


def values_in_range(start_point, end_point, values):
    def is_in_range(value):
        return value >= start_point and value <= end_point

    return list(filter(is_in_range, values))


if __name__ == "__main__":
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert values_in_range(4, 8, values) == [4, 5, 6, 7, 8]
    assert values_in_range(10, 15, values) == []

    values = ["praise", "test", "banana", "apple"]
    assert values_in_range("aaa", "ooo", values) == ["banana', 'apple"]
    print("completed successfully")
