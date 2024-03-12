//N1 * N2
const intersection = (arr1, arr2) => {
    if (arr1.length < arr2.length) return intersect(arr1.arr2);
    else return intersect(arr2, arr1, []);
}

const intersect = (short, long, common) => {
    comparisons = 0;
    for (i = 0; i < short.length; i++) {
        for (j = 0; j < long.length; j++) {
            if (short[i] == long[j]) {
                common.push(short[i])
                break; // stop once we find the value
            }
               comparisons++;
        }
    }
    console.log(comparisons);
    return common;
}

function intersection_book_solution(first_array, second_array) {
    var result = [];
    var comparisons = 0;
    for (var i = 0; i < first_array.length; i++) {
        for (var j = 0; j < second_array.length; j++) {
            if (first_array[i] == second_array[j]) {
                result.push(first_array[i]);
                break;
            }
            comparisons++;
        }
    }
    console.log(comparisons)
    return result;
}

const data1 = [4, 2, 1, 3];
const data2 = [4, 2, 1, 3];

console.log(intersection(data1, data2))
console.log(intersection_book_solution(data1, data2))