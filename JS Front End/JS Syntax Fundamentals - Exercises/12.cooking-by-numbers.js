function solve(num, op1, op2, op3, op4, op5) {
    let number = Number(num);
    const operators = [op1, op2, op3, op4, op5];

    for (let op of operators) {
        switch (op) {
            case "chop":
                number /= 2; break;
            case "dice":
                number = Math.sqrt(number); break;
            case "spice":
                number += 1; break;
            case "bake":
                number *= 3; break;
            case "fillet":
                number *= 0.8; break;
        }
        console.log(number);
    }
}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop')
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')
