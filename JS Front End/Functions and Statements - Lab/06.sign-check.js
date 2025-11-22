function signCheck(a, b, c) {
    const arr = [a, b, c];
    const negatives = arr.filter(x => x < 0).length;
    console.log(negatives % 2 === 0 ? "Positive" : "Negative");
}
