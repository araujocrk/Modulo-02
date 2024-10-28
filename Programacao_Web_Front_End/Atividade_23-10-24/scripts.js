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
resultNumberRandom.innerHTML = 'Este número foi gerado aleatoriamente com JS:' + ' ' + numberRandom;

var buttonNumberAbs = document.getElementById('buttonNumberAbs');
buttonNumberAbs.addEventListener('click', clickButtonNumberAbs);

function clickButtonNumberAbs() {
    var resultNumberAbs = document.getElementById('resultNumberAbs');
    var numberAbs = document.getElementById('numberAbs').value;
    numberAbs = Math.abs(numberAbs);
    resultNumberAbs.innerHTML = 'O valor absoluto de seu número é:' + ' ' + numberAbs;
}

var buttonNumberMax = document.getElementById('buttonNumberMax');
buttonNumberMax.addEventListener('click', clickButtonNumberMax);

function clickButtonNumberMax() {
    var resultNumberMax = document.getElementById('resultNumberMax');
    var number1 = document.getElementById('number1').value;
    var number2 = document.getElementById('number2').value;
    resultNumberMax.innerHTML = 'O maior número entre os dois é:' + ' ' + Math.max(number1, number2);
}

var buttonNumberRound = document.getElementById('buttonNumberRound');
buttonNumberRound.addEventListener('click', clickButtonNumberRound);

function clickButtonNumberRound() {
    var resultNumberRound = document.getElementById('resultNumberRound');
    var numberRound = document.getElementById('numberRound').value;
    resultNumberRound.innerHTML = 'Seu número arredondado é:' + ' ' + Math.round(numberRound);
}

var buttonNumberPow = document.getElementById('buttonNumberPow');
buttonNumberPow.addEventListener('click', clickButtonNumberPow);

function clickButtonNumberPow() {
    var resultNumberPow = document.getElementById('resultNumberPow');
    var numberPow1 = document.getElementById('numberPow1').value;
    var numberPow2 = document.getElementById('numberPow2').value;
    resultNumberPow.innerHTML = 'O primeiro número elevado ao segundo é:' + ' ' + Math.pow(numberPow1, numberPow2);
}

var buttonWordLength = document.getElementById('buttonWordLength');
buttonWordLength.addEventListener('click', clickButtonWordLength);

function clickButtonWordLength() {
    var resultWordLength = document.getElementById('resultWordLength');
    var wordLength = document.getElementById('wordLength').value;
    resultWordLength.innerHTML = 'Sua palavra tem' + ' ' + wordLength.length + ' ' + 'letras';
}

var buttonPhraseLower = document.getElementById('buttonPhraseLower');
buttonPhraseLower.addEventListener('click', clickButtonPhraseLower);

function clickButtonPhraseLower() {
    var resultPhraseLower = document.getElementById('resultPhraseLower');
    var phraseLower = document.getElementById('phraseLower').value;
    resultPhraseLower.innerHTML = 'Sua palavra em letras minúsculas é:' + ' ' + phraseLower.toLowerCase();
}

var buttonPhraseReplace = document.getElementById('buttonPhraseReplace');
buttonPhraseReplace.addEventListener('click', clickButtonPhraseReplace);

function clickButtonPhraseReplace() {
    var resultPhraseReplace = document.getElementById('resultPhraseReplace');
    var phraseReplace = document.getElementById('phraseReplace').value;
    resultPhraseReplace.innerHTML = 'Sua frase:' + ' ' + phraseReplace.replace(/a/g, '@').replace(/e/g, '3').replace(/i/g, '1').replace(/o/g, '0');
}

var buttonPhraseTrim = document.getElementById('buttonPhraseTrim');
buttonPhraseTrim.addEventListener('click', clickButtonPhraseTrim);

function clickButtonPhraseTrim() {
    var resultPhraseTrim = document.getElementById('resultPhraseTrim');
    var phraseTrim = document.getElementById('phraseTrim').value;
    resultPhraseTrim.innerHTML = 'Sua frase sem espaços antes e depois é:' + ' ' + phraseTrim.trim();
}

var buttonFullName = document.getElementById('buttonFullName');
buttonFullName.addEventListener('click', clickButtonFullName);

function clickButtonFullName() {
    var resultFullName = document.getElementById('resultFullName');
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    resultFullName.innerHTML = 'Nome completo:' + ' ' + firstName + ' ' + lastName;
}

var buttonSumAndDifference = document.getElementById('buttonSumAndDifference');
buttonSumAndDifference.addEventListener('click', clickButtonSumAndDifference);

function clickButtonSumAndDifference() {
    var resultSumAndDifference = document.getElementById('resultSumAndDifference');
    var number1 = document.getElementById('number1SumAndDifference').value;
    var number2 = document.getElementById('number2SumAndDifference').value;
    resultSumAndDifference.innerHTML = 'Soma:' + ' ' + (parseInt(number1) + parseInt(number2)) + '<br>' + 'Diferença:' + ' ' + (parseInt(number1) - parseInt(number2));
}

var buttonCleanText = document.getElementById('buttonCleanText');
buttonCleanText.addEventListener('click', clickButtonCleanText);

function clickButtonCleanText() {
    document.getElementById('cleanText').value = '';
}

var buttonCopyText = document.getElementById('buttonCopyText');
buttonCopyText.addEventListener('click', clickButtonCopyText);

function clickButtonCopyText() {
    var copyText = document.getElementById('copyText').value;
    document.getElementById('resultCopyText').value = copyText;
}