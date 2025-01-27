function getByID(id) {
    return document.getElementById(id);
}

let botaoConsultar = getByID('botaoConsultar');
botaoConsultar.addEventListener('click', consultarPreco);
async function consultarPreco() {
    let moedaBase = getByID('moedaBase').value.toUpperCase(); // Moeda base (ex.: BTC)
    let moedaConversao = getByID('moedaConversao').value.toUpperCase(); // Moeda de conversão(ex.: USDT)
    let resultado = getByID('resultado');
    const url =
        `https://api.binance.com/api/v3/ticker/price?symbol=${moedaBase}${moedaConversao}`;
    try {
        if (moedaBase && moedaConversao) {
            let response = await fetch(url); // Faz a requisição à API Binance
            if (!response.ok) {
                throw new Error(`HTTP Error: ${response.status} - ${response.statusText}`);
            }
            let json = await response.json();
            resultado.innerHTML = `
            <p><strong>Par de Moedas:</strong> ${json.symbol}</p>
            <p><strong>Preço:</strong> ${parseFloat(json.price).toFixed(2)} ${moedaConversao}</p>`;
        } else {
            resultado.innerHTML = 'Por favor, insira um par de moedas.';
        }
    } catch (error) {
        resultado.innerHTML = 'Erro: ' + error.message;
    }
}

let botaoLimpar = getByID('botaoLimpar');
botaoLimpar.addEventListener('click', limparCampos);
function limparCampos() {
    getByID('moedaBase').value = '';
    getByID('moedaConversao').value = '';
    getByID('resultado').innerHTML = '';
}

let botaoInverter = getByID('botaoInverter');
botaoInverter.addEventListener('click', () => {
    let moedaBase = getByID('moedaBase').value;
    let moedaConversao = getByID('moedaConversao').value;
    getByID('moedaBase').value = moedaConversao;
    getByID('moedaConversao').value = moedaBase;
});
