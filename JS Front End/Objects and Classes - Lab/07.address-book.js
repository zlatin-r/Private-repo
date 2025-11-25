function phoneBook(arr) {
    let data = {}

    arr.forEach(item => {
        let [name, street] = item.split(':');
        data[name] = street;
    });

    Object.entries(data)
        .sort((a, b) => a[0].localeCompare(b[0]))
        .forEach(([name, street]) => {
            console.log(`${name} -> ${street}`);
        });
}

phoneBook(['Bob:Huxley Rd',
    'John:Milwaukee Crossing',
    'Peter:Fordem Ave',
    'Bob:Redwing Ave',
    'George:Mesta Crossing',
    'Ted:Gateway Way',
    'Bill:Gateway Way',
    'John:Grover Rd',
    'Peter:Huxley Rd',
    'Jeff:Gateway Way',
    'Jeff:Huxley Rd'])
