function solve() {
    const form = document.getElementById('solutionCheck');
    const table = document.querySelector('table');
    const checkResult = document.getElementById('check');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const inputs = Array.from(
            table.querySelectorAll('input[type="number"]')
        );

        const values = inputs.map(input => Number(input.value));

        const rowsAndCols = [
            [values[0], values[1], values[2]],
            [values[3], values[4], values[5]],
            [values[6], values[7], values[8]],
            [values[0], values[3], values[6]],
            [values[1], values[4], values[7]],
            [values[2], values[5], values[8]],
        ];

        const allValid = rowsAndCols.every(
            arr => new Set(arr).size === arr.length
        );

        table.style.border = allValid
            ? '2px solid green'
            : '2px solid red';

        checkResult.textContent = allValid
            ? 'Success!'
            : 'Keep trying ...';
    });

    form.addEventListener('reset', () => {
        checkResult.textContent = '';
        table.style.border = '';
    });
}
