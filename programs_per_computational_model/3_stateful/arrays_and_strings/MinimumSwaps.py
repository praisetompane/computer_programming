"""
    Foreach value, currentIndex pair
        expectedIndexValue = index + 1
        if expectedIndexValue == value, continue
        else 
            currentValueCorrectIndex = value - 1
            swap(currentIndex, currentValueCorrectIndex)

"""


def minimumSwaps(arr):
    def swap(indexA, indexB):
        tempB = arr[indexB]
        arr[indexB] = arr[indexA]
        arr[indexA] = tempB

    swaps = 0
    swapped = True
    zeroIndexOffset = 1
    while swapped:
        swapped = False
        for x in range(0, len(arr)):
            expectedIndexValue = x + zeroIndexOffset
            value = arr[x]
            if expectedIndexValue != value:
                swapped = True
                swaps += 1
                currentValueCorrectIndex = value - zeroIndexOffset
                swap(x, currentValueCorrectIndex)
    return swaps


print(minimumSwaps([4, 3, 1, 2]))
