function toggleAnswer(element) {
    var answer = element.nextElementSibling;
    answer.classList.toggle('show');
    var toggle = element.querySelector('.toggle');
    toggle.textContent = (toggle.textContent === '+') ? '-' : '+';
}