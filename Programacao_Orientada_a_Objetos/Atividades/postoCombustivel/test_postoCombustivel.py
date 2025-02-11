import pytest
from pedro_posto_combustivel import PostoDeCombustivel, BombaDeCombustivel, Combustivel, Gasolina, Etanol, Abastecimento

def test_combustivel():
    combustivel = Combustivel('Gasolina', 5)
    assert combustivel.nome == 'Gasolina'
    assert combustivel.preco_por_litro == 5
    with pytest.raises(ValueError, match='Preço por litro deve ser maior que zero.'):
        Combustivel('Gasolina', -5.5)
    with pytest.raises(TypeError, match='Preço por litro deve ser um float ou inteiro.'):
        Combustivel('Gasolina', '10')
    with pytest.raises(NotImplementedError, match='Método não implementado na superclasse'):
        combustivel.calcular_valor('10')
        
def test_gasolina():
    gasolinaAditivada = Gasolina(5.5, 'sim')
    assert gasolinaAditivada.preco_por_litro == 5.5
    assert gasolinaAditivada.aditivada == True
    gasolinaNaoAditivada = Gasolina(5, 'não')
    assert gasolinaNaoAditivada.preco_por_litro == 5
    assert gasolinaNaoAditivada.aditivada == False