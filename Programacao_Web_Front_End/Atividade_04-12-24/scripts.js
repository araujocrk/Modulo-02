function getById(id) {
    return document.getElementById(id);
}

let inputText = getById('inputText');
let receiveText = getById('receiveText');

inputText.addEventListener('keyup', () => {
    receiveText.value = inputText.value;
});

let inputTextUpper = getById('inputTextUpper');
let receiveTextUpper = getById('receiveTextUpper');

inputTextUpper.addEventListener('keyup', () => {
    receiveTextUpper.value = inputTextUpper.value.toUpperCase();
});

let selectEmotions = getById('selectEmotions');
selectEmotions.addEventListener('change', () => {
    let imgEmotions = getById('imgEmotions');
    let emotion = selectEmotions.value
    switch (emotion) {
        case 'alegre':
            imgEmotions.src = 'imagens/alegria.png';
            break;
    
        case 'triste':
            imgEmotions.src = 'imagens/tristeza.png';
            break;
        
        case 'raiva':
            imgEmotions.src = 'imagens/raiva.png';
            break;
    }
});

let inputChangeColor = getById('inputChangeColor');
let backgroundColorDefault = inputChangeColor.style.backgroundColor;
inputChangeColor.addEventListener('focus', () => {
    inputChangeColor.style.backgroundColor = 'yellow';
});

inputChangeColor.addEventListener('blur', () => {
    inputChangeColor.style.backgroundColor = backgroundColorDefault;
});

let inputPassword = getById('inputPassword');
let tamanhoPassword;
inputPassword.addEventListener('keyup', () => {
    let password = inputPassword.value;
    let passwordWithoutSpaces = password.trim();
    tamanhoPassword = parseInt(passwordWithoutSpaces.length);
});

inputPassword.addEventListener('blur', () => {
    let errorPassword = getById('errorPassword');
    if (tamanhoPassword < 8) {
        errorPassword.innerHTML = 'Erro: Sua senha tem menos de 8 caracteres';
    } 
    else {
        errorPassword.innerHTML = '';
    }
});