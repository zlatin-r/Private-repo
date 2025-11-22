function solve(number) {
    let result = 0;
    let check = false;
    const str_number = String(number);

    for (let i = 0; i < str_number.length; i++) {
        result += Number(str_number[i]);
    }
    check = str_number.split("").every(d => d === str_number[0]);

    console.log(check);
    console.log(result);
}

solve(2222222)
solve(1234)
