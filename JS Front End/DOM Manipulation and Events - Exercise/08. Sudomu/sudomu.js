document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const inputs = document.querySelectorAll('#solutionCheck td input');

    document.querySelector('.buttons').addEventListener('click', (e) => {
        e.preventDefault();

        const values = Array.from(inputs).map(input => input.value);

        if (e.target.value === 'Quick Check') {
            const rowsAndCells = [];

            rowsAndCells.push(
                [values[0], values[1], values[2]],
                [values[3], values[4], values[5]],
                [values[6], values[7], values[8]],
                [values[0], values[3], values[6]],
                [values[1], values[4], values[7]],
                [values[2], values[5], values[8]],
            );
            const allValid = rowsAndCells.every(
                arr => new Set(arr).size === arr.length
            );

            if (allValid) {
                document.querySelector('#check').textContent = "Success!";
            } else {
                document.querySelector('#check').textContent = "Keep trying...";
            }
        } else if (e.target.value === 'Clear') {

        }
    })
}