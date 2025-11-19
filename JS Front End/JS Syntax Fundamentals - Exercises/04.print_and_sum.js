function solve(first, second) {
    let result = ""
    let summ = 0

    for (let i = first; i <= second; i++) {
        result += i + " "
        summ += i
    }
    console.log(result)
    console.log(`Sum: ${summ}`)
}

solve(5, 10)