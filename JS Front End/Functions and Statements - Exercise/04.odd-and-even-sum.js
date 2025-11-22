function oddAndEvenSum(number) {
    let arr = String(number).split("");
    let oddSum = 0;
    let evenSum = 0;

    arr.forEach((value) => {
        let number = Number(value);
        if (number % 2 === 0) {
            evenSum += number;
        } else {
            oddSum += number;
        }
    });
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddAndEvenSum(3495892137259234)
