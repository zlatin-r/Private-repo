function solve(number) {
    let sum = 0;
    const strNumber = number.toString();

    for (let i = 0; i < strNumber.length; i++) {
        sum += Number(strNumber[i]);
    }
    console.log(sum);
}

solve(245678)
