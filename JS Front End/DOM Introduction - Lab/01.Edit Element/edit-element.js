function editElement(el, match, replacer) {
    el.textContent = el.textContent.replaceAll(match, replacer);
}
