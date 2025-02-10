# Pode conter múltiplas bombas de combustível (associação 1:N).
class PostoDeCombustivel:
    def __init__(self,qtdBombaComb):
        self._qtdBombaComb = qtdBombaComb
       
    def adicionarBombaComb(self, bombaComb):
        pass
    def listarBombasComb(self):
        pass
    
        
# Pode estar associada a um único tipo de combustível
class BombaDeCombustivel:
    def __init__(self, tipoComb):
        self._tipoComb = tipoComb
        
    def associarComb(self, comb):
        pass
    
    def abastecimento(self, qtdComb):
        pass 
      
# Superclasse  
class Combustivel:
    def __init__(self, nome, valorLitro):
        self._nome = nome
        self._valorLitro = valorLitro
    
    def calcularValor(qtdLitros):
        raise NotImplementedError('Método não implementado na superclasse')

# Subclasse
class Gasolina(Combustivel):
    def __init__(self,valorLitro,aditivada):
        super().__init__('Combustível', valorLitro)
        self._aditivada = aditivada
        
    def calcularValor(self, qtdLitros):
        return qtdLitros * self._valorLitro
    
class Etanol(Combustivel):
    def __init__(self,valorLitro,origem):
        super().__init__('Etanol', valorLitro)
        self._origem = origem
        
    def calcularValor(self, qtdLitros):
        return qtdLitros * self._valorLitro