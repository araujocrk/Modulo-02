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
selectEmotions.addEventListener('change', () =>{
    let imgEmotions = getById('imgEmotions');
    imgEmotions.innerHTML = selectEmotions.value;
    let emotion = selectEmotions.value
    switch (emotion) {
        case emotion == 'alegre':
            imgEmotions.innerHTML = selectEmotions.value;
            break;
    
        case (emotion == 'triste'):
            imgEmotions.innerHTML = selectEmotions.value;
            break;
        
        case (emotion == 'raiva'):
            imgEmotions.innerHTML = selectEmotions.value;
            break;
    }
});

