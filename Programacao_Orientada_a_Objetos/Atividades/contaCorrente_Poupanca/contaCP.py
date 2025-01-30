class ContaCorrente: #Superclasse
    def __init__(self,numero,saldo):
        self._numero = numero
        if self.valorEhIntFloat:
            if self.valorEhMaiorOuIgualZero:
                self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo(self, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorOuIgualZero(valor):
                self._saldo = valor
                    
    def creditar(self, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorQueZero(valor):
                self._saldo += valor
        return self._saldo
    
    def debitar(self, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorQueZero(valor):
                if self.valorMaiorQueSaldo(valor):
                    self._saldo -= valor
        return self._saldo

    def transferir(self, conta, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorQueZero(valor):
                if self.valorMaiorQueSaldo(valor):
                    if isinstance(conta, (ContaCorrente, ContaPoupanca)):
                        self.debitar(valor)
                        conta.creditar(valor)
        return self._saldo, conta._saldo

    def valorEhIntFloat(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor deve ser um número')
        return True
    
    def valorEhMaiorOuIgualZero(self, valor):
        if valor <= 0:
            raise ValueError('Valor deve ser maior ou igual a zero')
        return True
    
    def valorEhMaiorQueZero(self, valor):
        if valor < 0:
            raise ValueError('Valor deve ser maior que zero')
        return True
    
    def valorMaiorQueSaldo(self, valor):
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        return True
                
class ContaPoupanca(ContaCorrente):
    def __init__(self,numero,saldo,taxa_juros):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros