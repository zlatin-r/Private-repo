function solve(a, b, op) {
    let result;

    switch (op) {
        case "multiply":
            result = (x, y) => x * y; break;
        case "divide":
            result = (x, y) => x / y; break;
        case "add":
            result = (x, y) => x + y; break;
        case "subtract":
            result = (x, y) => x - y; break;
    }

    console.log(result(a, b));
}