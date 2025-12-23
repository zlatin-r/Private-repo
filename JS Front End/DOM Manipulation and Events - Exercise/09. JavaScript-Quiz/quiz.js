document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const questions = Array.from(document.querySelectorAll('.question'));
    const answers = Array.from(document.querySelectorAll('.quiz-answer'));
    const resultsDiv = document.getElementById('results');
    const title = document.querySelector('h1');

    const correctAnswers = [
        'onclick',
        'JSON.stringify()',
        'A programming API for HTML and XML documents'
    ];

    let currentQuestion = 0;
    let rightAnswers = 0;

    answers.forEach(answer => {
        answer.addEventListener('click', () => {
            if (answer.textContent === correctAnswers[currentQuestion]) {
                rightAnswers++;
            }

            questions[currentQuestion].style.display = 'none';
            currentQuestion++;

            if (currentQuestion < questions.length) {
                questions[currentQuestion].style.display = 'block';
            } else {
                showResults();
            }
        });
    });

    function showResults() {
        resultsDiv.style.display = 'block';

        if (rightAnswers === correctAnswers.length) {
            title.textContent = 'You are recognized as top JavaScript fan!';
        } else if (rightAnswers === 1) {
            title.textContent = 'You have 1 right answer';
        } else {
            title.textContent = `You have ${rightAnswers} right answers`;
        }
    }
}
