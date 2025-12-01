function sumTable() {
    const tableCells = document.querySelectorAll('table tbody tr:not(:last-child) td:last-child');
    const sumElement = document.querySelector('#sum');

    sumElement.textContent = [...tableCells]
        .map(el => Number(el.textContent))
        .reduce((a, b) => a + b, 0);
}