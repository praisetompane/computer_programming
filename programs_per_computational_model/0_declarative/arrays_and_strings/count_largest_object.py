def birthday_cake_candles(ar: [int]) -> int:
    max_height = 0 if len(ar) == 0 else max(ar)
    return ar.count(max_height)


def main() -> None:
    assert birthday_cake_candles([3, 2, 1, 3]) == 2
    assert birthday_cake_candles([3, 2, 1, 3, 7, 7, 7, 1, 2, 5, 3, 3, 5, 2, 1]) == 3

    assert birthday_cake_candles([3, 2, 1]) == 1

    assert birthday_cake_candles([]) == 0
    assert birthday_cake_candles([1]) == 1
    assert birthday_cake_candles([1, 2]) == 1

    print("completed successfully")


if __name__ == "__main__":
    main()
