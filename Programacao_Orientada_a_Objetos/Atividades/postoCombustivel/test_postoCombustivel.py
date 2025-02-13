# cd Programacao_Orientada_a_Objetos/Atividades/postoCombustivel
import pytest
from pedro_posto_combustivel import PostoDeCombustivel, BombaDeCombustivel, Combustivel, Gasolina, Etanol, Abastecimento

def test_posto_de_combustivel():          # ***PASSOU NOS TESTES***
    jady = PostoDeCombustivel('Jady')
    assert jady.nome == 'Jady'
    
def test_adicionar_bomba_e_listar_bombas():          # ***PASSOU NOS TESTES***
    BombaDeCombustivel.contadorId = 0
    jady = PostoDeCombustivel('Jady')
    bombaUm = BombaDeCombustivel()
    bombaDois = BombaDeCombustivel()
    
    assert jady.adicionar_bomba(bombaUm) == 'Cadastrando bomba 1...'
    assert jady.adicionar_bomba(bombaDois) == 'Cadastrando bomba 2...'
    assert jady.listar_bombas() == 'Bomba: 1, Bomba: 2'
    
def test_bomba_de_combustivel():          # ***PASSOU NOS TESTES***
    BombaDeCombustivel.contadorId = 0
    bombaUm = BombaDeCombustivel()
    assert bombaUm.identificador == 1
    assert bombaUm.combustivel == None
    
    bombaDois = BombaDeCombustivel()
    assert bombaDois.identificador == 2
    assert bombaDois.combustivel == None
    
def test_associar_combustivel():          # ***PASSOU NOS TESTES***
    BombaDeCombustivel.contadorId = 0
    posto = PostoDeCombustivel('Jady')
    bombaUm = BombaDeCombustivel()
    bombaDois = BombaDeCombustivel()
    combustivelGas = Gasolina(5, 'sim')
    combustivelEtanol = Etanol(5, 'milho')

    assert bombaUm.associar_combustivel(combustivelGas) == 'Associando Gasolina (aditivada: Sim) a bomba 1...'
    assert bombaUm.combustivel == combustivelGas
    
    assert bombaDois.associar_combustivel(combustivelEtanol) == 'Associando Etanol (origem: Milho) a bomba 2...'
    assert bombaDois.combustivel == combustivelEtanol
    
    with pytest.raises(TypeError, match='Combustível inválido. O combustível deve ser do tipo Combustivel.'):
        bombaUm.associar_combustivel(bombaDois)
    with pytest.raises(TypeError, match='Combustível inválido. O combustível deve ser do tipo Combustivel.'):
        bombaUm.associar_combustivel(posto)
    with pytest.raises(TypeError, match='Combustível inválido. O combustível deve ser do tipo Combustivel.'):
        bombaUm.associar_combustivel('Gasolina')
    
def test_combustivel():
    combustivel = Combustivel('Gasolina', 5)
    assert combustivel.nome == 'Gasolina'
    assert combustivel.preco_por_litro == 5
    
    with pytest.raises(ValueError, match='Nome inválido. O nome deve ser "Gasolina" ou "Etanol".'):
        Combustivel('Gas', 5.5)
    with pytest.raises(ValueError, match='Preço por litro deve ser maior que zero.'):
        Combustivel('Gasolina', -5.5)
    with pytest.raises(TypeError, match='Preço por litro deve ser um float ou inteiro.'):
        Combustivel('Etanol', '10')
    with pytest.raises(NotImplementedError, match='Método não implementado na superclasse'):
        combustivel.calcular_valor('10')
    
# def test_gasolina():
#     gasolinaAditivada = Gasolina(5.5, 'sim')
#     assert gasolinaAditivada.preco_por_litro == 5.5
#     assert gasolinaAditivada.aditivada == True
#     gasolinaNaoAditivada = Gasolina(5, 'não')
#     assert gasolinaNaoAditivada.preco_por_litro == 5
#     assert gasolinaNaoAditivada.aditivada == False