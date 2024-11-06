function getid(id) {
    return document.getElementById(id);
}

function click (id, button) {
    return getid(id).addEventListener('click', button);
}

click ('buttonGoodAfternoon', function() {
    var name = getid('name').value;
    getid('resultGood').innerHTML = 'Boa Tarde' + ' ' + name;
});

click ('buttonGoodEvening', function() {
    var name = getid('name').value;
    getid('resultGood').innerHTML = 'Boa Noite' + ' ' + name;
});

var numberRandom = Math.floor((Math.random() * 10) + 1);
getid('resultNumberRandom').innerHTML = 'Este número foi gerado aleatoriamente com JS:' + ' ' + numberRandom;

click 