let currentInput = '';
let currentOperator = '';
let previousInput = '';

function AppendNumber(number) {
    currentInput += number;
    document.getElementById("Display").value = `${previousInput} ${currentOperator} ${currentInput}`;
}

function ChooseOperator(operator) {
    if (currentInput === '') return;
    previousInput = currentInput;
    currentInput = '';
    currentOperator = operator;
    document.getElementById("Display").value = `${previousInput} ${currentOperator}`;
}

function AllClear() {
    currentInput = '';
    currentOperator = '';
    previousInput = '';
    document.getElementById("Display").value = '';
}

function ClearEntry() {
    currentInput = '';
    document.getElementById("Display").value = `${previousInput} ${currentOperator}`;
}

function Calculate() {
    if (previousInput === '' || currentInput === '') return;

    const a = parseFloat(previousInput);
    const b = parseFloat(currentInput);
    let result = 0;

    switch (currentOperator) {
        case '+': result = a + b; break;
        case '-': result = a - b; break;
        case '*': result = a * b; break;
        case '/': result = b !== 0 ? a / b : 'Error'; break;
        case '%': result = a % b; break;
    }

    document.getElementById("Display").value = result;
    previousInput = '';
    currentInput = result.toString();
    currentOperator = '';
}
