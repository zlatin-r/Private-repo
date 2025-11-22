function solve(arr) {
    const first_el = arr.shift()
    const last_el = arr.pop()

    console.log(first_el + last_el)
}

solve([20, 30, 40])