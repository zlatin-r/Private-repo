document.addEventListener('DOMContentLoaded', solve);

function encode(text) {
    let result = '';

    for (let i = 0; i < text.length; i++) {
        const charCode = text.charCodeAt(i);
        result += String.fromCharCode(charCode + 1);
    }

    return result;
}

function decode(text) {
    let result = '';

    for (let i = 0; i < text.length; i++) {
        const charCode = text.charCodeAt(i);
        result += String.fromCharCode(charCode - 1);
    }

    return result;
}

function solve() {
    let message = document.querySelector('#encode textarea');
    let receivedMessage = document.querySelector('#decode textarea');

    const encodeBtn = document.querySelector('#encode button');
    const decodeBtn = document.querySelector('#decode button');

    encodeBtn.addEventListener('click', (e) => {
        e.preventDefault();

        receivedMessage.value = encode(message.value);
        message.value = "";
    })

    decodeBtn.addEventListener('click', (e) => {
        e.preventDefault();

        receivedMessage.value = decode(receivedMessage.value);
    })
}