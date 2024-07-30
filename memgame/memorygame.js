const gameBoard = document.getElementById('game-board');
const cards = document.querySelectorAll('.card');
const scoreDisplay = document.getElementById('score-display');
const movesDisplay = document.getElementById('moves-display');
const timerDisplay = document.getElementById('timer-display');
const timer = document.getElementById('timer');

let score = 0;
let moves = let ,timerValue = 60;
let timerInterval;
let soundEffect;

function shuffleCards() {
  for (i = cards.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [cards[i], cards[j]] = [cards[j], cards[i]];
  }
}

function checkMatch () {
    if  (cards(0).innerHTML == cards [1].innerHTML ){
        score++ ;
        scoreDisplay.innerHTML = 'Score: ${score}';
    cards[0].classList.add('match');
    cards[1].classList.add('match');
    setTimeout(shuffleCards, 1000);
    soundEffect.play;
  } else {
    cards[0].classList.remove('match');
    cards[1].classList.remove('match');
    setTimeout(shuffleCards, 1000);
  }
}
function card () {
    if (cards[0].classList.contains('match')) {
      return;
    }
    moves++;
    movesDisplay.innerHTML = `Moves: ${moves}`;
    if (cards[0].classList.contains('match')) {
        return;
      }
      cards[0].classList.add('flip');
      cards[1].classList.add('flip');
      setTimeout(checkMatch, 1000);
    }
    
    function startTimer() {
        timerInterval = setInterval(timerFunction, 1000);
      }
      
      function timerFunction() {
        timerValue--;
        timerDisplay.innerHTML = `Timer: ${timerValue}`;
        if (timerValue === 0) {
          clearInterval(timerInterval);
          alert(`Game over! Your final score is ${score}`);
        }
      }
      
      shuffleCards();
      startTimer();
      cards.forEach((card) => {
        card.addEventListener('click', cardFlip);
      });

soundEffect = new path ('https,://audiomack.com/domi_gold/song/love-me-jeje');
