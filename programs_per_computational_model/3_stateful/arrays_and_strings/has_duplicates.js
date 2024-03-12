//only works for positive integers
const hasDuplicates = (arr) => {
    number_exists = []

    for (i = 0; i < arr.length; i++) {
        if (number_exists[arr[i]] == undefined) {
            number_exists[arr[i]] = 1
        }
        else {
            return true;
        }
    }
    return false;
}

console.log(hasDuplicates([1, 2, 3, 4, 5, 7, 8]))
