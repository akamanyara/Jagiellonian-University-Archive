const file = 'test.json'
let currentIndex = 0;
let correct = 0;

let questionBlocks = []

let timeLeft = 6;
let timerInterval = null;
const timePerQuestion = 6;


window.onload = () => {
    readFile(file);
};

function readFile(file){
    fetch(file)
        .then(response => response.json())
        .then(data => {
            questionBlocks = data;
            RunQuiz();
            // loadQuestion(questionBlocks[currentIndex]);
        })
        .catch(err => console.error("JSON reading error: ", err))
}

// Make each question an async func
// with a throw if time runs out
// then move to the next question on finally

async function RunQuiz(){
    currentIndex = 0;
    correct = 0;

    while ((currentIndex < questionBlocks.length)) {
        const questionBlock = questionBlocks[currentIndex];
        await RunQuestion(questionBlock).catch(timeRanOut).finally(tryLoadQuestion);
    }
    

    finishQuiz();
}

async function timeRanOut(ex) {
    if (!(ex instanceof TimerExpiredError)) {
        throw ex; // re-throw unexpected errors
    }
    document.getElementById("Timer").innerText = `Time's up!`;
    disableButtons();
    await delay(1500);
}

async function RunQuestion(questionBlock) {
    loadQuestion(questionBlock);

    // Wait for answer
    await RunTimer();
    // let post answer result linger
    await delay(800);

    // Next question transition
    disableButtons();
    await delay(500);
}

//#region Timer

// https://stackoverflow.com/a/47480429
let bShouldTickTimer = false;
let bQuestionFinished = false;

const delay = ms => new Promise(res => setTimeout(res, ms));

class TimerExpiredError extends Error {
    constructor(message) {
        super(message);
        this.name = "TimerExpiredError";
    }
}

async function RunTimer() {
    const currQuestion = currentIndex;
    const tickTime = 1000;

    timeLeft = timePerQuestion;
    function updateTimerDisplay() {
        document.getElementById("Timer").innerText = `Timer: ${timeLeft}s`;
    }

    bShouldTickTimer = true;
    updateTimerDisplay();
    for (let i = 0; i < 6; i++){
        if (!bShouldTickTimer)
        {
            console.log("Question finished");
            // Question has finished early, exit timer
            return;
        }
        updateTimerDisplay();
        timeLeft--;
        console.log("1000ms delay...");
        await delay(tickTime);
    }
    throw new TimerExpiredError("Timer expired");
    return;
    
}

//#endregion Timer


function disableButtons() {
    for (let i = 1; i <= 4; i++) {
        document.getElementById(`Button${i}`).disabled = true;
    }
}

async function checkAnswer(buttonIndex) {

    bShouldTickTimer = false;
    const currentQuestion = questionBlocks[currentIndex];
    const button = document.getElementById(`Button${buttonIndex}`);

    if (buttonIndex - 1 === currentQuestion.correct) {
        button.style.backgroundColor = "rgb(50, 205, 50)";
        correct++;
    } else {
        button.style.backgroundColor = "rgb(255, 68, 51)";
    }

    await delay(800);

    return;
}

function tryLoadQuestion() {
    currentIndex++;
    if (currentIndex < questionBlocks.length) {
        loadQuestion(questionBlocks[currentIndex]);
    }
}

function loadQuestion(questionBlock){
    const { question, answers } = questionBlock;

    for (let i = 1; i <= 4; i++) {
        document.getElementById(`Button${i}`).style.backgroundColor =  'rgb(178, 134, 142)';
        document.getElementById(`Button${i}`).disabled = false;
    }

    document.getElementById('Question').innerText = question;

    for (let i = 0; i < 4; i++) {
        document.getElementById(`Button${i + 1}`).innerText = answers[i];
    }
}

function finishQuiz(){
    alert(`You have reached the end!\nYour score: ${correct} / ${questionBlocks.length}`)
    currentIndex = 0;
    correct = 0;

    // Let's go again
    // Yes, I know this will stack overflow eventually but sssssh
    RunQuiz();
}