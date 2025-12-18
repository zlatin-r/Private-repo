document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const itemsData = document.querySelector('textarea');
    const data = JSON.parse(itemsData.value)

    for (const item of data) {
        let itemImage = document.createElement('img');
        itemImage.textContent = item.img;

        let itemName = document.createElement('p');
        itemName.textContent = item.name;

        let itemPrice = document.createElement('p');
        itemPrice.textContent = item.price;

        let itemDecFactor = document.createElement('p');
        itemDecFactor.textContent = item.itemDecFactor;

        let checkBox = document.createElement('input');
        checkBox.type = 'checkbox';

        // console.log(item.img);
        // console.log(item.name);
        // console.log(item.price);
        // console.log(item.decFactor);
    }
}