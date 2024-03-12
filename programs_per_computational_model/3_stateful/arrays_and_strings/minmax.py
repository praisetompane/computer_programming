def birthdayCakeCandles(n, ar):
    length = len(ar)
    if length == 0:
        return 0
    maxHeight = max(ar)

    def countAppearance(appearanceTotal, index):
        nextIndex = index + 1
        if index == length:
            return appearanceTotal
        elif ar[index] == maxHeight:
            return countAppearance(appearanceTotal + 1, nextIndex)
        else:
            return countAppearance(appearanceTotal, nextIndex)

    return countAppearance(0, 0)


assert birthdayCakeCandles(4, [3, 2, 1, 3]) == 2
assert birthdayCakeCandles(15, [3, 2, 1, 3, 7, 7, 7, 1, 2, 5, 3, 3, 5, 2, 1]) == 3  # 3
assert (
    birthdayCakeCandles(4, [3, 2, 1]) == 1
)  # note the age and ar elements are not the same, for sneaky input
assert birthdayCakeCandles(4, []) == 0
assert birthdayCakeCandles(1, [1]) == 1
assert birthdayCakeCandles(2, [1, 2]) == 1
