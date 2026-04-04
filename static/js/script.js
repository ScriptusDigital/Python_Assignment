//Page event listeners//
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menuToggle');
    const mainNav = document.getElementById('mainNav');
    const quizForm = document.getElementById('quizForm');
    const cards = document.querySelectorAll('.question-card');
    const nextButtons = document.querySelectorAll('.next-btn');
    const backButtons = document.querySelectorAll('.back-btn');
    
    const progressText = document.getElementById('progressText');
    const progressBar = document.getElementById('progressBar');

let currentCard = 0;

//Menu Toggle - based on https://dev.to/ljcdev/easy-hamburger-menu-with-js-2do0//
if (menuToggle && mainNav) {
    menuToggle.addEventListener("click", () => {
    const isOpen = mainNav.classList.toggle("open");
   menuToggle.setAttribute("aria-expanded", isOpen? "true" : "false");
    });
}

//Quiz Buttons 
//Based on tutorials from https://css-tricks.com/how-to-create-multi-step-forms-with-vanilla-javascript-and-css//
//https://www.w3schools.com/howto/howto_js_form_steps.asp //
//https://webdesign.tutsplus.com/how-to-build-a-multi-step-form-wizard-with-javascript--cms-93342t//

//Validation messagae element for unanswered quiz questions
function getCurrentQuizMessage() {
const currentCardElement = cards[currentCard];
if (!currentCardElement) return null;
return currentCardElement.querySelector('.quiz-message');
}

//Show next card and update progress bar

function showCard(index) {
    cards.forEach((card, i) => {
      card.classList.toggle('active', i === index);
    });


const currentStep = index + 1;
const totalSteps = cards.length;

if(progressText) {
    progressText.textContent = `Question ${currentStep} of ${totalSteps}`;

}
    if (progressBar) {
        const width = (currentStep / totalSteps) * 100;
        progressBar.style.width = `${width}%`;
    }

  const quizMessage = getCurrentQuizMessage();
  if (quizMessage) {
     quizMessage.textContent = "";
  }
    }


function currentQuestionAnswered(index) {
    const currentCardElement = cards[index];
    if (!currentCardElement) return false;

    const selectedOption = currentCardElement.querySelector('input[type="radio"]:checked');
    return !!selectedOption;
}


nextButtons.forEach(button => {
    button.addEventListener('click', () => {
    if (!currentQuestionAnswered(currentCard)) {
     const quizMessage = getCurrentQuizMessage();
        if (quizMessage) {
            quizMessage.textContent = "Please answer the question before proceeding.";
        }
        return;
    }
    if (currentCard < cards.length - 1) {
        currentCard += 1;
        showCard(currentCard);
    }
});
});

backButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (currentCard > 0) {
            currentCard -=1;
            showCard(currentCard);
        }
    });
});

if (quizForm) {
    quizForm.addEventListener('submit', (e) => {
if (!currentQuestionAnswered(currentCard)) {
    e.preventDefault();
    const quizMessage = getCurrentQuizMessage();
    if (quizMessage) {
        quizMessage.textContent = "Please answer the question before submitting.";
    }
}
});
}

if (cards.length > 0) {
    showCard(currentCard   );       
}
});