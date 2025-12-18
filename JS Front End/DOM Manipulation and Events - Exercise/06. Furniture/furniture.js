document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const inputTextarea = document.querySelector('#input textarea');
    const generateBtn = document.querySelector('#input input[type="submit"]');
    const buyBtn = document.querySelector('#shop input[type="submit"]');
    const tableBody = document.querySelector('#shop table tbody');
    const outputTextarea = document.querySelector('#shop textarea');

    generateBtn.addEventListener('click', (e) => {
        e.preventDefault();

        const data = JSON.parse(inputTextarea.value);

        for (const item of data) {
            const row = document.createElement('tr');

            // Image
            const imgTd = document.createElement('td');
            const img = document.createElement('img');
            img.src = item.img;
            imgTd.appendChild(img);
            row.appendChild(imgTd);

            // Name
            const nameTd = document.createElement('td');
            const nameP = document.createElement('p');
            nameP.textContent = item.name;
            nameTd.appendChild(nameP);
            row.appendChild(nameTd);

            // Price
            const priceTd = document.createElement('td');
            const priceP = document.createElement('p');
            priceP.textContent = item.price;
            priceTd.appendChild(priceP);
            row.appendChild(priceTd);

            // Decoration factor
            const decTd = document.createElement('td');
            const decP = document.createElement('p');
            decP.textContent = item.decFactor;
            decTd.appendChild(decP);
            row.appendChild(decTd);

            // Checkbox
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

        const rows = Array.from(tableBody.querySelectorAll('tr'));
        const bought = [];

        for (const row of rows) {
            const checkbox = row.querySelector('input[type="checkbox"]');
            if (checkbox && checkbox.checked) {
                const cells = row.children;
                bought.push({
                    name: cells[1].textContent,
                    price: Number(cells[2].textContent),
                    decFactor: Number(cells[3].textContent)
                });
            }
        }

        const names = bought.map(i => i.name).join(', ');
        const totalPrice = bought.reduce((s, i) => s + i.price, 0);
        const avgDecFactor =
            bought.reduce((s, i) => s + i.decFactor, 0) / bought.length;

        outputTextarea.value =
            `Bought furniture: ${names}\n` +
            `Total price: ${totalPrice}\n` +
            `Average decoration factor: ${avgDecFactor}`;
    });
}
