class ContaCorrente: #Superclasse
    def __init__(self,numero,saldo):
        self._numero = numero
        self._saldo = float(saldo)
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo deve ser um número')
        
        if valor < 0:
            raise ValueError('Saldo não pode ser negativo')
        
        self._saldo = valor
    
    def creditar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor deve ser um número')

        self._saldo += valor
        return self._saldo
            
    def debitar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor deve ser um número')
        
        if valor <= 0:
            raise ValueError('Valor deve ser maior que zero')
        
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        
        self._saldo -= valor
        return self._saldo
    
    def transferir(self):
        pass
    
class ContaPoupanca(ContaCorrente):
    def __init__(self,numero,saldo,taxa_juros):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros