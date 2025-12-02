function subtract() {
    let numOne = Number(document.getElementById('firstNumber').value);
    let numTwo = Number(document.getElementById('secondNumber').value);
    document.querySelector('#result').textContent = numOne - numTwo;
}