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

