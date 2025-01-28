function getById(id) {
    return document.getElementById(id);
}

let botaoDigimon = getById('botaoDigimon');
botaoDigimon.addEventListener('click', pesquisarDigimon);

async function pesquisarDigimon() {
    let digimon = getById('inputPersonagem').value;
    let resultadoDigimon = getById('resultadoDigimon');
    let url = `https://digi-api.com/api/v1/digimon/${digimon}`;

    try {
        if (digimon) {
            let response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }

            let json = await response.json();

            let type = json.types.map(types => types.type).join(', ');
            let level = json.levels.map(levels => levels.level).join(', ');
            let attribute = json.attributes.map(attributes => attributes.attribute).join(', '); 
            resultadoDigimon.innerHTML = `
            <p><strong>Nome:</strong> ${json.name || 'Desconhecido'}</p>
            <p><strong>Tipo:</strong> ${type || 'Desconhecido'}</p>
            <p><strong>Level:</strong> ${level || 'Desconhecido'}</p>
            <p><strong>Atributo:</strong> ${attribute || 'Desconhecido'}</p>
            `;
        }
    } catch (error) {
        resultadoDigimon.innerHTML = 'Erro: ' + error.message;
    }
};

let botaoAtributo = getById('botaoAtributo');
botaoAtributo.addEventListener('click', pesquisarAtributo);

async function pesquisarAtributo() {
    let atributo = getById('inputAtributo').value;
    let resultadoAtributo = getById('resultadoAtributo');
    let url = `https://digi-api.com/api/v1/attribute/${atributo}`;

    try {
        if (atributo) {
            let response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }

            let json = await response.json();

            resultadoAtributo.innerHTML = `
            <p><strong>Nome:</strong> ${json.name || 'Desconhecido'}</p>
            <p><strong>Descrição:</strong> ${json.description || 'Desconhecido'}</p>
            `;
        }
    } catch (error) {
        resultadoDigimon.innerHTML = 'Erro: ' + error.message;
    }
};