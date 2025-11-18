function solve(people, group_type, day) {
    let price = 0
    let total_price = 0

    switch (group_type) {
        case "Students":
            if (day === "Friday") {
                price = 8.45
            } else if (day === "Saturday") {
                price = 9.80
            } else if (day === "Sunday") {
                price = 10.46
            }
            break;
        case "Business":
            if (day === "Friday") {
                price = 10.90
            } else if (day === "Saturday") {
                price = 15.60
            } else if (day === "Sunday") {
                price = 16
            }
            break;
        case "Regular":
            if (day === "Friday") {
                price = 15
            } else if (day === "Saturday") {
                price = 20
            } else if (day === "Sunday") {
                price = 22.50
            }
            break;
    }
    if (group_type === "Students" && people >= 30) {
        total_price = (price * people) * 0.85
    } else if (group_type === "Business" && people >= 100) {
        total_price = price * (people - 10)
    } else if (group_type === "Regular" && people >= 10 && people <= 20) {
        total_price = (price * people) * 0.95
    } else {
        total_price = price * people
    }
    console.log(`Total price: ${total_price.toFixed(2)}`)
}

solve(30, "Students", "Sunday")
solve(40, "Regular", "Saturday")