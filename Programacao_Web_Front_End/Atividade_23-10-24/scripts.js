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
    resultNumberAbs.innerHTML = numberAbs;
}

