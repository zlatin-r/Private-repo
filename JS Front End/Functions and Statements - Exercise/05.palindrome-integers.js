function palindromeInteger(arr) {
    arr.forEach((val) => {
        let reversedVal = String(val).split('').reverse().join('');
        console.log(val === Number(reversedVal));
    });
}

palindromeInteger([123,323,421,121]);
