function solve(fruit, weight, price) {
    let weight_kg = weight / 1000
    let total_price = weight_kg * price;
    console.log(`I need $${total_price.toFixed(2)} to buy ${weight_kg.toFixed(2)} kilograms ${fruit}.`);
}

solve('orange', 2500, 1.80)
solve('apple', 1563, 2.35)
