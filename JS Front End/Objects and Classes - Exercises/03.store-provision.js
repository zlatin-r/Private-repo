function storeProvision(arr, arr2) {
    let data = {}
    for (let i = 0; i < arr.length; i += 2) {
        let product = arr[i];
        let quantity = Number(arr[i + 1])
        data[product] = quantity;
    }
    for (let j = 0; j < arr2.length; j+=2) {
        let product = arr2[j];
        let quantity = Number(arr2[j + 1]);
        if (data.hasOwnProperty(product)) {
            data[product] += quantity;
        } else {
            data[product] = quantity;
        }
    }
    for (let [item, key] of Object.entries(data)) {
        console.log(`${item} -> ${key}`);
    }
}

storeProvision(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']);
