class ContaCorrente: #Superclasse
    def __init__(self,numero,saldo):
        self.numero = numero
        self.saldo = saldo
        
    def creditar():
        pass
    
    def debitar():
        pass
    
    def saldo():
        pass
    
    def transferir():
        pass
    
class ContaPoupanca(ContaCorrente):
    def __init__(self,numero,saldo,taxa_juros):
        super().__init__(numero, saldo)
        self.taxa_juros = taxa_juros