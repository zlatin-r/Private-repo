document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const itemsData = document.querySelector('textarea');
    const data = JSON.parse(itemsData.value)

    for (const item of data) {
        console.log(item.name);
        console.log(item.price);
        console.log(item.decFactor);
    }
}