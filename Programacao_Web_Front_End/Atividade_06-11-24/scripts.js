function getid(id){
    return document.getElementById(id);
}

function click (id, button) {
    return getid(id).addEventListener('click', button);
}

click ('buttonPadStart', () => {
    var padStart = getid('padStart').value;
    getid('resultPadStart').innerHTML = 'Seu número com 5 zeros a esquerda:' + ' ' + padStart.padStart(padStart.length + 5, '0');
});

click ('buttonOperations', () => {
    var q2n1 = parseFloat(getid('q2n1').value);
    var q2n2 = parseFloat(getid('q2n2').value);
    var sum = q2n1 + q2n2;
    var difference = q2n1 - q2n2;
    var product = q2n1 * q2n2;
    var quotient = q2n1 / q2n2;
    getid('resultOperations').innerHTML = 
    `Soma: ${sum} <br>
     Subtração: ${difference} <br>
     Produto: ${product} <br>
     Quociente: ${quotient}`
});

click ('buttonCelsius', () => {
    var celsius = parseFloat(getid('temperatureCelsius').value);
    getid('resultCelsiusToFahrenheit').innerHTML = 'Temperatura em Fahrenheit:' + ' ' + 
    ((celsius * (9 / 5)) + 32) + ' ' + 'F°'
});

const date = new Date();
getid('resultCurrentDate').innerHTML = date.toLocaleDateString('pt-BR');
// getid('resultCurrentDate').innerHTML = date.getDate() + '/' + (date.getMonth() + 1) + '/' + date.getFullYear();

function onKeyUp() {
    var onKeyUp = getid('onKeyUp').value;
    getid('resultOnKeyUp').innerHTML = onKeyUp;
}

click ('buttonTextReverse', () => {
    var text = getid('textReverse').value;
    getid('resultReverse').innerHTML = 'Seu texto invertido:' + ' ' + text.split('').reverse('').join('');
});