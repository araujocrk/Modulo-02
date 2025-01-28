function getById(id) {
    return document.getElementById(id);
}

let botaoPersonagem = getById('botaoPersonagem');
botaoPersonagem.addEventListener('click', pesquisarPersonagem); 

async function pesquisarPersonagem() {
    let personagem = parseInt(getById('inputPersonagem').value);
    let resultadoPersonagem = getById('resultadoPersonagem');
    let url = `https://narutodb.xyz/api/character/${personagem}`;

    try {
        if (personagem) {
            let response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }

            let json = await response.json();
            
            resultadoPersonagem.innerHTML = `
            <p><strong>Nome:</strong> ${json.name || 'Desconhecido'}</p>
            <p><strong>Tipo da Natureza:</strong> ${json.natureType || 'Desconhecido'}</p>
            <p><strong>Sexo:</strong> ${json.personal.sex || 'Desconhecido'}</p>
            `;
        }
    } catch (error) {
        resultadoPersonagem.innerHTML = 'Erro: ' + error.message;
    }
};

let botaoTime = getById('botaoTime');
botaoTime.addEventListener('click', pesquisarTime);

async function pesquisarTime() {
    let time = parseInt(getById('inputTime').value);
    let resultadoTime = getById('resultadoTime');
    let url = `https://narutodb.xyz/api/team/${time}`;

    try {
        if (time) {
            let response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }

            let json = await response.json();
            const integrantes = json.characters.map(character => character.name).join(', ');
            resultadoTime.innerHTML = `
            <p><strong>Nome do time:</strong>${json.name || 'Desconhecido'}</p>
            <p><strong>Integrantes:</strong>${integrantes || 'Desconhecido'}</p>
            `;
        }
    } catch (error) {
        resultadoTime.innerHTML = 'Erro: ' + error.message;
    }
};