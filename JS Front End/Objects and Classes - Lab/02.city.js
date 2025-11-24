function city(obj) {
    let entries = Object.entries(obj);
    for (let [k, v] of entries) {
        console.log(`${k} -> ${v}`);
    }
}

city(
    {
        name: "Sofia",
        area: 492,
        population: 1238438,
        country: "Bulgaria",
        postCode: "1000"
    }
)

