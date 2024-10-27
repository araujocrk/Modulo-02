var buttonGoodAfternoon = document.getElementById('buttonGoodAfternoon');
buttonGoodAfternoon.addEventListener('click', clickButtonGoodAfternoon);

function clickButtonGoodAfternoon() {
    var resultGood = document.getElementById('resultGood');
    var name = document.getElementById('name');
    resultGood.innerHTML = 'Boa Tarde' + ' ' + name.value;
}

var buttonGoodEvening = document.getElementById('buttonGoodEvening');
buttonGoodEvening.addEventListener('click', clickButtonGoodEvening);

function clickButtonGoodEvening() {
    var resultGood = document.getElementById('resultGood');
    var name = document.getElementById('name');
    resultGood.innerHTML = 'Boa Noite' + ' ' + name.value;
}

var resultNumberRandom = document.getElementById('resultNumberRandom');
var numberRandom = Math.floor((Math.random() * 10) + 1);
resultNumberRandom.innerHTML += numberRandom;

var buttonNumberAbs = document.getElementById('buttonNumberAbs');
buttonNumberAbs.addEventListener('click', clickButtonNumberAbs);

function clickButtonNumberAbs() {
    var resultNumberAbs = document.getElementById('resultNumberAbs');
    var numberAbs = document.getElementById('numberAbs').value;
    numberAbs = Math.abs(numberAbs);
    resultNumberAbs.innerHTML += ' ' + numberAbs + ';';
}

var buttonNumberMax = document.getElementById('buttonNumberMax');
buttonNumberMax.addEventListener('click', clickButtonNumberMax);

function clickButtonNumberMax() {
    var resultNumberMax = document.getElementById('resultNumberMax');
    var number1 = document.getElementById('number1').value;
    var number2 = document.getElementById('number2').value;
    resultNumberMax.innerHTML += ' ' + Math.max(number1, number2) + ';';
}

var buttonNumberRound = document.getElementById('buttonNumberRound');
buttonNumberRound.addEventListener('click', clickButtonNumberRound);

function clickButtonNumberRound() {
    var resultNumberRound = document.getElementById('resultNumberRound');
    var numberRound = document.getElementById('numberRound').value;
    resultNumberRound.innerHTML += ' ' + Math.round(numberRound) + ';';
}

var buttonNumberPow = document.getElementById('buttonNumberPow');
buttonNumberPow.addEventListener('click', clickButtonNumberPow);

function clickButtonNumberPow() {
    var resultNumberPow = document.getElementById('resultNumberPow');
    var numberPow1 = document.getElementById('numberPow1').value;
    var numberPow2 = document.getElementById('numberPow2').value;
    resultNumberPow.innerHTML += ' ' + Math.pow(numberPow1, numberPow2) + ';';
}

