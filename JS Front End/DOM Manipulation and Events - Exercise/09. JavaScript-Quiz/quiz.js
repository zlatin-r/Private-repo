document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const sections = Array.from(document.querySelectorAll('.question'));
    const resultsDiv = document.getElementById('results');

    const correctAnswers = [
        'onclick',
        'JSON.stringify()',
        'A programming API for HTML and XML documents'
    ];

    let rightAnswers = 0;

    sections.forEach((section, index) => {
        const answers = section.querySelectorAll('.quiz-answer');

        answers.forEach(answer => {
            answer.addEventListener('click', () => {

                if (answer.textContent === correctAnswers[index]) {
                    rightAnswers++;
                }

                section.style.display = 'none';

                if (index + 1 < sections.length) {
                    sections[index + 1].style.display = 'block';
                } else {
                    resultsDiv.style.display = 'block';

                    if (rightAnswers === 3) {
                        resultsDiv.textContent =
                            'You are recognized as top JavaScript fan!';
                    } else if (rightAnswers === 1) {
                        resultsDiv.textContent =
                            'You have 1 right answer';
                    } else {
                        resultsDiv.textContent =
                            `You have ${rightAnswers} right answers`;
                    }
                }
            });
        });
    });
}
