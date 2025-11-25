function phoneBook(arr) {
    let phoneBook = {};

    arr.forEach((element) => {
        const [name, number] = element.split(' ');
        phoneBook[name] = number;
    });
    for (let key in phoneBook) {
        console.log(`${key} -> ${phoneBook[key]}`);
    }
}
