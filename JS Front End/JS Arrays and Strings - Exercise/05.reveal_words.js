function solve(keyWords, text) {
    let keys = keyWords.split(', ');

    for (let word of keys) {
        let wordLen = word.length;
        let searchedEl = "*".repeat(wordLen);

        text = text.replace(searchedEl, word);
    }
    console.log(text);
}

solve('great','softuni is ***** place for learning new programming languages')

