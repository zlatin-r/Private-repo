function employees(arr) {
    const obj = {};
    arr.forEach(e => obj[e] = e.length);
    for (let [key, value] of Object.entries(obj)) {
        console.log(`Name: ${key} -- Personal Number: ${value}`);
    }
}

employees([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
]);
