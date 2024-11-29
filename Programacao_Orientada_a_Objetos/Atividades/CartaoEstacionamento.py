import random
import string
from datetime import *
class CartaoEstacionamento:
    numCartoesAtivos = []
    def gerarCartao():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    def gerarDataHora():
        return datetime.now()
    
    def __init__(self):
        self.__numCartao = self.cartaoValido(CartaoEstacionamento.gerarCartao())
        self.dataHoraEntrada = CartaoEstacionamento.gerarDataHora()
        self.status = 'Ativo'
        self.dataHoraSaida = 'Sem saída'
        self.__valorTotal = 0
    
    @property
    def numCartao(self):
        return self.__numCartao
    
    @property
    def valorTotal(self):
        return self.__valorTotal
    
    @valorTotal.setter
    def valorTotal(self, valor):
        self.__valorTotal = valor
        
    def cartaoValido(self, numCartao):
        if numCartao not in CartaoEstacionamento.numCartoesAtivos:
            CartaoEstacionamento.numCartoesAtivos.append(numCartao)
            return numCartao
        else:
            return self.cartaoValido(CartaoEstacionamento.gerarCartao())
        
    def finalizarSaida(self):
        dataHoraSaida = CartaoEstacionamento.gerarDataHora()
        if dataHoraSaida < self.dataHoraEntrada:
            raise ValueError('Data ou horário de saída inválidos')
        else:
            self.dataHoraSaida = dataHoraSaida
            self.status = 'Finalizado'
            CartaoEstacionamento.numCartoesAtivos.remove(self.numCartao)
            self.calcularValorTotal(dataHoraSaida)
    
    def calcularValorTotal(self, dataHoraAtual):
        permanencia = dataHoraAtual - self.dataHoraEntrada
        minutos = permanencia.total_seconds() // 60
        if minutos <= 120:
            self.valorTotal = 8.0
            print(self.valorTotal)
        else:
            excesso = minutos - 120
            valor_excesso = (excesso // 15) * 0.50
            self.valorTotal = 8.0 + valor_excesso
            print(self.valorTotal)
            
    def __str__(self):
        entrada_formatada = self.dataHoraEntrada.strftime('%d-%m-%Y %H:%M')
        saida_formatada = (
        self.dataHoraSaida.strftime('%d-%m-%Y %H:%M') 
        if isinstance(self.dataHoraSaida, datetime) 
        else self.dataHoraSaida
    )
        return f'Cartão: {self.numCartao}\nEntrada: {entrada_formatada}\nSaida: {saida_formatada}\nStatus: {self.status}\nValor total: {self.valorTotal}'
    
def main():
    cartao1 = CartaoEstacionamento()
    cartao1.finalizarSaida()
    cartao2 = CartaoEstacionamento()
    cartao2.calcularValorTotal(CartaoEstacionamento.gerarDataHora())
    cartao3 = CartaoEstacionamento()
    print(cartao3)
    
if __name__ == '__main__':
    main()