//Event listeners pages//
document.addEventListener('DOMContentLoaded', () =>    {
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.getElementById('mainNav');
    const quizForm = document.getElementById('quizForm');
    const cards = document.querySelectorAll('.question-card');
    const nextButtons = document.querySelectorAll('.next-btn');
    const backButtons = document.querySelectorAll('.back-btn');    

let currentCard = 0;

//Menu Toggle//
if (menuToggle && mainNav) {
    menuToggle.addEventListener("click", () => {
    const isOpen = mainNav.classList.toggle("open");
   menuToggle.setAttribute("aria-expanded", isOpen? "true" : "false");
    });
}

//Quiz Buttons//
function showCard(index) {
    cards.forEach((card, i) => {
      card.classList.toggle('active', i === index);
    });
}

nextButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (currentCard < cards.length - 1) {
            currentCard++;
            showCard(currentCard);
        }
    });
});

backButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (currentCard > 0) {
            currentCard--;
            showCard(currentCard);
        }
    });
});

if (quizForm && cards.length > 0) {
    showCard(currentCard);
}

}); 

//Submit Quiz//


