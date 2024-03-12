const hasDuplicates = (arr) => {
    for (i = 0; i < arr.length; i++) {
        for (j = 0; j < arr.length; j++) {
            if (i != j && arr[i] == arr[j]) {
                return true;
            }
        }
    }
    return false;
}

console.log(hasDuplicates([1, 2, 3, 4, 5, 7, 8]))
