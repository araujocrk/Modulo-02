function getById(id) {
    return document.getElementById(id);
}

let visibility = true;
let btnChangeVisibility = getById('btnChangeVisibility');
btnChangeVisibility.addEventListener('click', () => {
    let pVisibility = getById('pVisibility');
    
    if (visibility) {
        pVisibility.style.visibility = 'hidden';
        visibility = false;
    }
    else {
        pVisibility.style.visibility = 'visible';
        visibility = true;
    }
});

let btnFontSizeDown = getById('btnFontSizeDown');
btnFontSizeDown.addEventListener('click', () => {
    let pFontSize = getById('pFontSize');
    // Obtém o tamanho da fonte calculado (se não estiver diretamente no style)
    let currentFontSize = parseInt(window.getComputedStyle(pFontSize).fontSize);
    pFontSize.style.fontSize = (currentFontSize - 1) + 'px';
});

let btnFontSizeUp = getById('btnFontSizeUp');
btnFontSizeUp.addEventListener('click', () => {
    let pFontSize = getById('pFontSize');
    // Obtém o tamanho da fonte calculado (se não estiver diretamente no style)
    let currentFontSize = parseInt(window.getComputedStyle(pFontSize).fontSize);
    pFontSize.style.fontSize = (currentFontSize + 1) + 'px';
});

let btnChangeBackground = getById('btnChangeBackground');
btnChangeBackground.addEventListener('click', () => {
    let inputHour = getById('inputHour');
    let hour = parseInt(inputHour.value);
    if (hour >= 0 && hour <= 6 || hour >= 18 && hour <= 23) {
        document.body.style.backgroundColor = 'black';
        document.body.style.color = 'white';
    }
    else {
        document.body.style.backgroundColor = 'white';
        document.body.style.color = 'black';
    }
});

let btnChangeClass = getById('btnChangeClass');
btnChangeClass.addEventListener('click', () => {
    let boxClass = getById('boxClass');
    boxClass.classList.toggle('novoEstilo');
});