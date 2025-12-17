document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const textareas = document.querySelectorAll('textarea');
    const buttons = document.querySelectorAll('button');

    const sender = textareas[0];
    const receiver = textareas[1];

    const encodeBtn = buttons[0];
    const decodeBtn = buttons[1];

    encodeBtn.addEventListener('click', () => {
        let encoded = '';

        for (let ch of sender.value) {
            encoded += String.fromCharCode(ch.charCodeAt(0) + 1);
        }

        receiver.value = encoded;
        sender.value = '';
    });

    decodeBtn.addEventListener('click', () => {
        let decoded = '';

        for (let ch of receiver.value) {
            decoded += String.fromCharCode(ch.charCodeAt(0) - 1);
        }

        receiver.value = decoded;
    });
}
