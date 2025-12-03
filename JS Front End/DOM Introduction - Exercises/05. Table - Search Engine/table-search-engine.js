function solve() {
    const searchField = document.querySelector('#searchField');
    const searchText = searchField.value.toLowerCase();

    const rows = Array.from(document.querySelectorAll('tbody tr'));

    rows.forEach(row => row.classList.remove('select'));

    rows.forEach(row => {
        const rowText = row.textContent.toLowerCase();
        if (searchText !== '' && rowText.includes(searchText)) {
            row.classList.add('select');
        }
    });

    searchField.value = '';
}
