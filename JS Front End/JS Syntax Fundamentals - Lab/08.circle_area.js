function solve(arrg) {
    let result;

    if (typeof arrg === 'number') {
        result = (Math.pow(arrg, 2) * Math.PI).toFixed(2);
    } else {
        result = `We can not calculate the circle area, because we receive a ${typeof arrg}.`;
    }
    console.log(result);
}

solve(5)
solve("name")
