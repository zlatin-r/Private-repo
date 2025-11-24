function loadingBar(number) {
    let dots = `${".".repeat(10 - (number / 10))}`
    let bar = `[${"%".repeat(number / 10)}${dots}]`;

    if (number !== 100) {
        console.log(`${number}% ${bar}`);
        console.log(`Still loading...`);
    } else {
        console.log(`${number}% Complete!`);
        console.log(`${bar}`);
    }
}

loadingBar(30)
loadingBar(50)
loadingBar(100)
