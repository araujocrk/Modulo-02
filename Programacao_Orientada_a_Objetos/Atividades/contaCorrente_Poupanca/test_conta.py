import pytest 
from contaCP import ContaCorrente, ContaPoupanca, ContaImposto
#
def test_creditar():
    conta = ContaCorrente('123', 1000.00)
    resultado_esperado = 1500.50
    resultado = conta.creditar(500.50)
    assert resultado_esperado == resultado
        
def test_debitar():
    conta = ContaCorrente('123', 1000.00)
    resultado_esperado = 699.50
    resultado = conta.debitar(300.50)
    assert resultado_esperado == resultado
    
def test_saldo():
    conta = ContaCorrente('123', 1000.00)
    resultado_esperado = 1000.00
    resultado = conta.saldo
    assert resultado_esperado == resultado
    
def test_transferir():
    conta_origem = ContaCorrente('123', 1000.00)
    conta_destino = ContaCorrente('456', 0.00)
    resultado_esperado_origem, resultado_esperado_destino = conta_origem.transferir(conta_destino, 400)
    assert resultado_esperado_origem == 600.00
    assert resultado_esperado_destino == 400.00
    
def test_renderJuros():
    conta = ContaPoupanca('123', 1000.00, 0.01)
    resultado_esperado = 1010.0
    resultado = conta.renderJuros()
    assert resultado_esperado == resultado
    
def test_calcularImposto():
    conta = ContaImposto('123', 1000.00, 0.01)
    resultado_esperado = 990.0
    resultado = conta.calcularImposto()
    assert resultado_esperado == resultado