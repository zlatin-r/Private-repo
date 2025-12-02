function solve() {
    let text = document.getElementById('text').value;
    let convention = document.getElementById('naming-convention').value;
    let resultField = document.getElementById('result');

    let words = text.toLowerCase().split(" ");
    let result = "";

    if (convention === "Camel Case") {
        result = words
            .map((w, i) =>
                i === 0 ? w : w.charAt(0).toUpperCase() + w.slice(1)
            )
            .join("");
    } else if (convention === "Pascal Case") {
        result = words
            .map(w => w.charAt(0).toUpperCase() + w.slice(1))
            .join("");
    } else {
        result = "Error!";
    }

    resultField.textContent = result;
}
