# Sort the array
# iterate over unsorted array
# Check that current number is where it should be compare to sorted array
# if not move it to where it should
# update index of the corresponding swapped value in the itemUnsortedIndexDictionary
# else continue


def minimumSwaps(arr):
    sortedArr = sorted(arr)
    itemUnsortedIndexDictionary = {v: i for i, v in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        correctValue = sortedArr[i]
        currentValue = arr[i]
        if correctValue is not currentValue:
            itemUnsortedIndex = itemUnsortedIndexDictionary[correctValue]

            temp = currentValue
            arr[i] = arr[itemUnsortedIndex]
            arr[itemUnsortedIndex] = temp

            itemUnsortedIndexDictionary[temp] = itemUnsortedIndex
            swaps += 1

    return swaps


print("Swaps:", minimumSwaps([4, 3, 1, 2]))
