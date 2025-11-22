function solve(input) {
    const words = input.split(' ');

    for (let word of words) {
        if (word.startsWith('#')) {
            const tag = word.slice(1);

            if (/^[A-Za-z]+$/.test(tag)) {
                console.log(tag);
            }
        }
    }
}

solve('The symbol # is known #variously in English-speaking #regions as the #number sign');