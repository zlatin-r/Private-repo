function addItem() {
    let listEl = document.querySelector('#items');
    let inputText = document.querySelector('#newItemText').value;
    let newLiElement = document.createElement('li');
    
    newLiElement.textContent = inputText;

    listEl.appendChild(newLiElement);

    document.querySelector('#newItemText').value = '';
}
