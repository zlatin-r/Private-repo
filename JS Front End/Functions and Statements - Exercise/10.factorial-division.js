function factorialDivision(a, b) {
    function factorial(n) {
        let result = 1;
        for (let i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    const first = factorial(a);
    const second = factorial(b);
    const result = first / second;

    console.log(result.toFixed(2));

}