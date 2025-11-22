function solve(prod, count) {
    let price = 0;
    let total = 0;

    if (prod === "coffee") {
        price = 1.5;
    } else if (prod === "water") {
        price = 1;
    } else if (prod === "coke") {
        price = 1.4;
    } else if (prod === "snacks") {
        price = 2;
    }
    total = price * count
    console.log(total.toFixed(2));
}

solve("water", 5)
solve("coffee", 2)