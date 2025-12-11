document.addEventListener('DOMContentLoaded', solve);

function solve() {
   let inputText = document.querySelector('#task-input input[type="text"]').value;
   let resultContent = document.querySelector('#content');
   let sections = inputText.split(', ');

   sections.forEach(section => {
       let newDivElement = document.createElement('div');
       let newParagraph = document.createElement('p');

       newDivElement.appendChild(newParagraph);
       resultContent.appendChild(newDivElement);
   });
}
