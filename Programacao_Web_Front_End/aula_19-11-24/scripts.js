function getById(id) {
    return document.getElementById(id);
}

var verificar = getById('verificar');
verificar.addEventListener('click', ()=> {
    var numero = parseInt(getById('numero').value);
    var resultado = getById('resultado');

    if (numero > 10) {
        resultado.innerHTML = 'O número é maior que 10'
    }
    else {
        if (numero < 10) {
            resultado.innerHTML = 'O número é menor que 10'
        }
        else {
            resultado.innerHTML = 'O número é igual a 10'
        }
    }
});

var verificarDia = getById('verificarDia');
verificarDia.addEventListener('click', () => {
    var dia = getById('dia').value;
    var resultadoSwitch = getById('resultadoSwitch');

    switch (dia) {
        case '1':
            resultadoSwitch.innerHTML = 'Domingo';
            break;
        case '2':
            resultadoSwitch.innerHTML = 'Segunda-Feira';
            break;
        case '3':
            resultadoSwitch.innerHTML = 'Terça-Feira';
            break;
        case '4':
            resultadoSwitch.innerHTML = 'Quarta-Feira';
            break;
        case '5':
            resultadoSwitch.innerHTML = 'Quinta-Feira';
            break;
        case '6':
            resultadoSwitch.innerHTML = 'Sexta-Feira';
            break;
        case '7':
            resultadoSwitch.innerHTML = 'Sábado';
            break;
        default:
            resultadoSwitch.innerHTML = 'Dia inválido';
            break;
    }
});

var contar = getById('contar');
contar.addEventListener('click', () => {
    let resultadoFor = getById('resultadoFor');
    for (let c = 1; c < 11; c = c + 1) {
                                // c++ (somar + 1)
        resultadoFor.innerHTML += c + ' ';
    }
    resultadoFor.innerHTML += '<br>Agora o inverso<br>';
    for (let c = 10; c > 0; c = c - 1) {
                            // c-- (subtrair - 1)
        resultadoFor.innerHTML += c + ' ';
    }
});

var mostrarArrayOf = getById('mostrarArrayOf');
mostrarArrayOf.addEventListener('click', () => {
    let resultadoForOf = getById('resultadoForOf');
    let frutas = ['uva', 'maçã', 'laranja'];

    for (let fruta of frutas) {
        resultadoForOf.innerHTML += fruta + ', ';
    }
});

var mostrarArrayIn = getById('mostrarArrayIn');
mostrarArrayIn.addEventListener('click', () => {
    var resultadoForIn = getById('resultadoForIn');
    var cidades = ['the', 'sp', 'phb', 'slz', 'for'];

    for (var indice in cidades) {
        resultadoForIn.innerHTML += cidades[indice] + ' ';
    }
});

var enviarNumParar = getById('enviarNumParar');
enviarNumParar.addEventListener('click', () => {
    var resultadoWhile = getById('resultadoWhile');
    var limite = getById('numParar').value;
    var contador = 1;
    resultadoWhile.innerHTML = ''

    while (contador <= limite) {
        resultadoWhile.innerHTML += contador + ' ';
        contador++;
    }
});

var enviarNumPararDoWhile = getById('enviarNumPararDoWhile');
enviarNumPararDoWhile.addEventListener('click', () => {
    var resultadoDoWhile = getById('resultadoDoWhile');
    var limiteDoWhile = getById('numPararDoWhile').value;
    var contador = 1;
    resultadoDoWhile.innerHTML = ''
    
    do {
        resultadoDoWhile.innerHTML += contador + ' ';
        contador++;
    }
    while (contador <= limiteDoWhile);
})

var encontrarNumMaior10 = getById('encontrarNumMaior10');
encontrarNumMaior10.addEventListener('click', () => {
    var resultadoBreak = getById('resultadoBreak');
    var numeros = [1, 3, 7, -10, -8, 5, 23, 15, 2];
    resultadoBreak.innerHTML = numeros + '<br>';

    for (var numero of numeros) {
        resultadoBreak.innerHTML += numero + ' ';
        if (numero > 10) {
            break;
        }
    }
});