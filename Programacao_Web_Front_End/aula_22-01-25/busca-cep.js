
function getByID(id) {
  return document.getElementById(id);
}

let botaoConsultar = getByID('botaoConsultar');

botaoConsultar.addEventListener('click', consultarCEP);

async function consultarCEP() {
  let cep = getByID('textoCEP').value;
  let resultado = getByID('resultado');
  let url = `https://viacep.com.br/ws/${cep}/json/`;
  
  try {
    let response = await fetch(url);
    
    // Verificar se a resposta foi bem-sucedida
    if (!response.ok) {
      throw new Error(`Erro ao consultar CEP: ${response.status} - ${response.statusText}`);
    }

    let json = await response.json();

    // Exibe apenas as informações desejadas
    resultado.innerHTML = `
      <p><strong>Logradouro:</strong> ${json.logradouro || 'Não disponível'}</p>
      <p><strong>Bairro:</strong> ${json.bairro || 'Não disponível'}</p>
      <p><strong>Cidade:</strong> ${json.localidade || 'Não disponível'}</p>
      <p><strong>UF:</strong> ${json.uf || 'Não disponível'}</p>`;
  } catch (error) {
    resultado.innerHTML = 'Erro: ' + error.message;
  }    
}

/*
async function consultarCEP() {
  try {
    let url = `https:viacep.com.br/ws/${cep}/json/`
    let response = await fetch(url);
    let json = await response.json();
    console.log(json);
  } catch (error) {
    console.error(error.message);
  }
}
consultarCEP('64218100');*/