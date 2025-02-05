class Veiculo:
    def __init__(self, chassi, ano):
        self._chassi = chassi
        self._ano = ano

    def calcular_custo(self, distancia, preco_comb):
        raise NotImplementedError('Método não implementado na classe pai')
    def __str__(self):
        return f'Chassi: {self._chassi}\n Ano: {self._ano}'

class Moto(Veiculo):
    def __init__(self, chassi, ano, cilindradas):
        super().__init__(chassi, ano)
        self._cilindradas = cilindradas
        self._consumo = 25
    
    def calcular_custo(self, distancia, preco_comb):
        litros = distancia / self._consumo
        return litros * preco_comb

    def __str__(self):
        return super().__str__() + f'\nCilindradas: {self._cilindradas}\n Consumo: {self._consumo}'

class Carro(Veiculo):
    def __init__(self, chassi, ano, motor):
        super().__init__(chassi, ano)
        self._motor = motor
        self._consumo = 12

    def calcular_custo(self, distancia, preco_comb):
        litros = distancia / self._consumo
        return litros * preco_comb

    def __str__(self):
        return super().__str__() + f'\nMotor: {self._motor}\n Consumo: {self._consumo}'
    
class Caminhao(Veiculo):
    def __init__(self, chassi, ano, capacidade):
        super().__init__(chassi, ano)
        self._capacidade = capacidade
        self._consumo = 5

    def calcular_custo(self, distancia, preco_comb):
        litros = distancia / self._consumo
        return litros * preco_comb
    
    def __str__(self):
        return super().__str__() + f'\nCapacidade: {self._capacidade}\n Consumo: {self._consumo}'
    
class ControleDeViagens:
    def __init__(self):
        self._veiculos = []
        self._totalCusto = 0

    def adicionarVeiculos(self, veiculo):
        self._veiculos.append(veiculo)
    
    def listarVeiculos(self):
        for veiculo in self._veiculos:
            print(veiculo)

    def calculaCustoTotal(self, veiculo, distancia, preco_comb):
        self._totalCusto = veiculo.calcular_custo(distancia, preco_comb)
        return self._totalCusto
