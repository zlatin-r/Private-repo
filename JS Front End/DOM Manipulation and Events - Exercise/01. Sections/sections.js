document.addEventListener('DOMContentLoaded', solve);

function solve() {

    const contendElement = document.querySelector('#content');
    const generateElement = document.querySelector('input[type="submit"]');

    generateElement.addEventListener('click', (e) => {
        e.preventDefault();

        const inputStrings = document.querySelector('input[type="text"]').value.split(', ');

        inputStrings.forEach((str) => {

            const newDiv = document.createElement('div');
            const newParagraph = document.createElement('p');

            newParagraph.textContent = str;
            newParagraph.style.display = 'none';

            newDiv.appendChild(newParagraph);
            newDiv.addEventListener('click', (e) => {
                e.target.querySelector('p').style.display = 'block';
            });

            contendElement.appendChild(newDiv);
        });
    });
}