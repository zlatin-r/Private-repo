function solve(word, text) {
    let arr = text.split(' ');
    let wordToLowerCase = word.toLowerCase();

    let result = arr.find(w => w.toLowerCase() === wordToLowerCase);

    if (result) {
        console.log(wordToLowerCase);
    } else {
        console.log(`${wordToLowerCase} not found!`);
    }
}

solve('javascript', 'JavaScript is the best programming language')
