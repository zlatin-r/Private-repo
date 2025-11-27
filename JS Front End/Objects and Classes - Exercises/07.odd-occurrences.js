function oddOccurrences(sentence) {
    const words = sentence.split(' ');
    const counts = {};
    const order = [];

    words.forEach(word => {
        const lower = word.toLowerCase();
        if (!counts.hasOwnProperty(lower)) {
            counts[lower] = 0;
            order.push(lower);
        }
        counts[lower]++;
    });

    const oddWords = order.filter(word => counts[word] % 2 !== 0);

    console.log(oddWords.join(' '));
}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');
