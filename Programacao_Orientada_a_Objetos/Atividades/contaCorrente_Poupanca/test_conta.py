import pytest 
from contaCorrente_Poupanca import ContaCorrente, ContaPoupanca

# def test_creditar():
#     conta = ContaCorrente('123', 1000.00)
#     resultado_esperado = 1500.00
#     resultado = conta.creditar(500)
#     assert resultado_esperado == resultado
    
#     with pytest.raises(ValueError):
#         conta.creditar('500')
    
#     with pytest.raises(ValueError):
#         conta.creditar(-500)
        
def test_debitar():
    conta = ContaCorrente('123', 1000.00)
    resultado_esperado = 500.00
    resultado = conta.debitar(500)
    assert resultado_esperado == resultado
    
    with pytest.raises(ValueError):
        conta.debitar('500')
    
    with pytest.raises(ValueError):
        conta.debitar(-500)