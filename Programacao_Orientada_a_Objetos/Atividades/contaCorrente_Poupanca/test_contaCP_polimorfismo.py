import pytest
from contaCP_polimorfismo import ContaCorrente, ContaPoupanca, ContaImposto, Banco

def test_adicionarConta():
    banco = Banco()
    contaC = ContaCorrente('123', 500)
    contaP = ContaPoupanca('123', 1000, 0.01)
    contaI = ContaImposto('123', 1500, 0.01)
    banco.adicionarConta(contaC)
    banco.adicionarConta(contaP)
    banco.adicionarConta(contaI)
    assert len(banco._contas) == 3
    banco.removerConta(contaP)
    assert len(banco._contas) == 2
    for i in banco._contas:
        assert isinstance(i, ContaCorrente) == True

def test_totalDepositado():
    banco = Banco()
    contaC = ContaCorrente('123', 500)
    contaP = ContaPoupanca('456', 1000, 0.01)
    contaI = ContaImposto('789', 1500, 0.01)
    banco.adicionarConta(contaC)
    banco.adicionarConta(contaP)
    banco.adicionarConta(contaI)
    banco.listaContas()
    assert self._valor_contas == 3000
