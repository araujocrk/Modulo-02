import random
import string
from datetime import datetime, timedelta
class CartaoEstacionamento:
    numCartoesAtivos = []
    def gerarCartao():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    def gerarDataHoraEntrada():
        return datetime.now()
    
    def __init__(self, numCartao=None, dataHoraEntrada=None, status='Ativo', dataHoraSaida=None, valorTotal=None):
        self.__numCartao = self.cartaoValido(numCartao)
        self.dataHoraEntrada = dataHoraEntrada
        self.status = status
        self.dataHoraSaida = dataHoraSaida
        self.__valorTotal = valorTotal
    
    def cartaoValido(self, numCartao):
        if numCartao not in CartaoEstacionamento.numCartoesAtivos:
            CartaoEstacionamento.numCartoesAtivos.append(numCartao)
            return numCartao
        else:
            return self.cartaoValido(CartaoEstacionamento.gerarCartao())
        
    def finalizarSaida(self):
        self.dataHoraSaida = datetime.now()
        if self.dataHoraSaida < self.dataHoraEntrada:
            self.status = 'Finalizado'
            CartaoEstacionamento.numCartoesAtivos.remove(self.__numCartao)
            self.calcularValorTotal()
    
    def calcularValorTotal(self):
        
        
    
    @property
    def numCartao(self):
        return self.__numCartao
    
def main():
    cartao1 = CartaoEstacionamento(CartaoEstacionamento.gerarCartao(), CartaoEstacionamento.gerarDataHoraEntrada())
    print(cartao1.numCartao)
if __name__ == '__main__':
    main()