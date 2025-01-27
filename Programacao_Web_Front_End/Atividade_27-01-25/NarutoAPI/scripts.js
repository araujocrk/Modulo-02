function getById(id) {
    return document.getElementById(id);
}

let botaoPersonagem = getById('botaoPersonagem');
botaoPersonagem.addEventListener('click', pesquisarPersonagem); 

async function pesquisarPersonagem() {
    let Personagem = getById('inputPersonagem').value;
    let resultadoPersonagem = getById('resultadoPersonagem');
    let url = `https://narutodb.xyz/api/character/search?name=${Personagem}`;

    try {
        if (inputPersonagem) {
            let response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }

            let json = await response.json();
            
            resultadoPersonagem.innerHTML = `<p><strong>Nome:</strong> ${json.name}</p>`;
        }
    } catch (error) {
        resultadoPersonagem.innerHTML = 'Erro: ' + error.message;
    }
};