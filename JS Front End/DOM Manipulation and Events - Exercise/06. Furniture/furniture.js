document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const inputTextarea = document.querySelector('#input textarea');
    const generateBtn = document.querySelector('#input input[type="submit"]');
    const buyBtn = document.querySelector('#shop input[type="submit"]');
    const tableBody = document.querySelector('#shop table tbody');

    generateBtn.addEventListener('click', (e) => {
        e.preventDefault();

        tableBody.innerHTML = '';

        const data = JSON.parse(inputTextarea.value);

        for (const item of data) {
            const row = document.createElement('tr');

            // IMAGE
            const imgTd = document.createElement('td');
            const img = document.createElement('img');
            img.src = item.img;
            imgTd.appendChild(img);
            row.appendChild(imgTd);

            // NAME
            const nameTd = document.createElement('td');
            const nameP = document.createElement('p');
            nameP.textContent = item.name;
            nameTd.appendChild(nameP);
            row.appendChild(nameTd);

            // PRICE
            const priceTd = document.createElement('td');
            const priceP = document.createElement('p');
            priceP.textContent = item.price;
            priceTd.appendChild(priceP);
            row.appendChild(priceTd);

            // DECORATION FACTOR
            const decTd = document.createElement('td');
            const decP = document.createElement('p');
            decP.textContent = item.decFactor;
            decTd.appendChild(decP);
            row.appendChild(decTd);

            // CHECKBOX
            const checkTd = document.createElement('td');
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkTd.appendChild(checkbox);
            row.appendChild(checkTd);

            tableBody.appendChild(row);
        }
    });

    buyBtn.addEventListener('click', (e) => {
        e.preventDefault();

        const outputEl = document.querySelector('#shop textarea');

        const data = [...document.querySelectorAll('table tbody tr')]
            .filter(row => row.querySelector('input[type="checkbox"]').checked)
            .map(row => ({
                name: row.children[1].textContent.trim(),
                price: Number(row.children[2].textContent),
                decFactor: Number(row.children[3].textContent)
            }));

        let output = `Bought furniture: ${data.map(el => el.name).join(', ')}\n`;
        output += `Total price: ${data.reduce((sum, el) => sum + el.price, 0).toFixed(2)}\n`;
        output += `Average decoration factor: ${data.reduce((sum, el) => sum + el.decFactor, 0) / data.length}`;

        outputEl.value = output;
    });
}
