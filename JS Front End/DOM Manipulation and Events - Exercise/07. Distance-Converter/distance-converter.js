document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const convertBtn = document.getElementById('convert');
    const inputUnitSelect = document.getElementById('inputUnits');
    const outputUnitSelect = document.getElementById('outputUnits');
    const inputValue = document.getElementById('inputDistance');
    const outputValue = document.getElementById('outputDistance');

    convertBtn.addEventListener('click', (e) => {
        e.preventDefault();

        const inputUnit = inputUnitSelect.value;
        const outputUnit = outputUnitSelect.value;
        const distanceValue = Number(inputValue.value);

        console.log(inputUnit, outputUnit, distanceValue);
    })


}