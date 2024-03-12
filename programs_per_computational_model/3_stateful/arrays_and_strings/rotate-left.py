def new_index(index, rotations, arr_length):
    target_index = index - rotations
    abs_target_index = abs(target_index)
    if target_index < 0:
        return arr_length - abs_target_index
    else:
        return abs_target_index


def rotateLeft(d, arr):
    arr_length = len(arr)
    print(arr_length)
    new_array = [0 for _ in range(arr_length)]
    for i in range(arr_length):
        new_array[new_index(i, d, arr_length)] = arr[i]
    return new_array
