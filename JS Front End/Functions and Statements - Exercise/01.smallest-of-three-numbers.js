function smallestOfThreeNumbers(a, b, c) {
    let arr = [a, b, c];
    let smallestNum = arr.reduce((a, b) => (a < b ? a : b));
    console.log(smallestNum);
}

smallestOfThreeNumbers(2, 5, 3)
