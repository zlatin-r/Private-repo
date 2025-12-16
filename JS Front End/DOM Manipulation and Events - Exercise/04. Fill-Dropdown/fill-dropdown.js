document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const text = document.getElementById('newItemText');
    const value = document.getElementById('newItemValue');
    const form = document.querySelector('form');

    const menuElement = document.getElementById('menu');

    form.addEventListener('submit', e => {
        e.preventDefault();

        const newOptionEl = document.createElement('option');

        [newOptionEl.textContent, newOptionEl.value] = [text.value, value.value];

        menuElement.appendChild(newOptionEl);

        [text.value, value.value] = ["", ""];
    });
}