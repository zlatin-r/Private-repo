function wordsTracker(array) {
    let keys = array.shift().split(" ");
    let counts = {};

    keys.forEach(key => counts[key] = 0);

    array.forEach(word => {
        if (counts.hasOwnProperty(word)) {
            counts[word]++;
        }
    });

    let sortedKeys = keys.sort((a, b) => counts[b] - counts[a]);

    sortedKeys.forEach(key => {
        console.log(`${key} - ${counts[key]}`);
    });
}

wordsTracker([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have', 'to', 'count', 'the', 'occurrences', 'of', 'the', 'words',
    'this', 'and', 'sentence', 'because', 'this', 'is', 'your', 'task'
]);

wordsTracker([
    'is the',
    'first', 'sentence', 'Here', 'is', 'another', 'the', 'And', 'finally', 'the', 'the', 'sentence'])