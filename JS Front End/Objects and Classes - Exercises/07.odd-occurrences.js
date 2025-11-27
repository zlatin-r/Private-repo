function oddOccurrences(sentence) {
    const words = sentence.split(' ');
    const counts = {};
    const order = []; // to preserve first appearance

    words.forEach(word => {
        const lower = word.toLowerCase();
        if (!counts.hasOwnProperty(lower)) {
            counts[lower] = 0;
            order.push(lower);
        }
        counts[lower]++;
    });

    // Filter words that appear an odd number of times
    const oddWords = order.filter(word => counts[word] % 2 !== 0);

    console.log(oddWords.join(' '));
}

// Example 1
oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
// Output: c# php 1 5

// Example 2
oddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');
// Output: soft food
