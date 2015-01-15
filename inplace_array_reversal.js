/*
 * In-Place Array Reversal
 * Reverse an array using only constant extra space.
 */

reverse = function(arr) {
    for (var i = 0; i < Math.floor(arr.length / 2); i++) {
        var j = arr.length - i - 1;
        var tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
    return arr;
};

test_cases = [
    [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
    [[1, 2, 3, 4], [4, 3, 2, 1]],
    [[2, 3], [3, 2]],
    [[2], [2]]
];

for (var i = 0; i < test_cases.length; i++) {
    var test_case = test_cases[i][0];
    var ans = test_cases[i][1];
    /* This is not the recommended way to compare arrays
       In practice, I would use the underscore.js library */
    if ("" + reverse(test_case) !== "" + ans) {
        throw "wah";
    }
}

console.log('All is Good');