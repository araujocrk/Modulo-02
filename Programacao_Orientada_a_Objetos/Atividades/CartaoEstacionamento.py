import random
import string
from datetime import datetime

class CartaoEstacionamento:
    numCartoesAtivos = []
    def __init__(self, dataHoraEntrada):
        self.dataHoraEntrada = self.validarDataHora(dataHoraEntrada)
        self.__numCartao = self.gerarNumCartao()
        self.status = 'Ativo'
        self.dataHoraSaida = 'Não informado'
        self.__valor = 0

    def validarDataHora(self, dataHora):
        dataHora = datetime.strptime(dataHora, '%d/%m/%Y %H:%M')
        return dataHora.strftime('%d/%m/%Y %H:%M')

    def gerarNumCartao(self):
        numCartao = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        if numCartao not in CartaoEstacionamento.numCartoesAtivos:
            CartaoEstacionamento.numCartoesAtivos.append(numCartao)
            return numCartao
        else:
            return self.gerarNumCartao()

    @property
    def numCartao(self):
        return self.__numCartao

    def calcularValor(self):
        dataHoraEntrada = datetime.strptime(self.dataHoraEntrada, '%d/%m/%Y %H:%M')
        permanencia = datetime.now() - dataHoraEntrada
        minutos = permanencia.total_seconds() // 60
        if minutos <= 120:
            return 8.0
        else:
            excesso = minutos - 120
            valor_excesso = (excesso // 15) * 0.50
            return 8.0 + valor_excesso

    def verValor(self):
        return f'R${self.calcularValor():.2f}'

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def finalizarSaida(self):
        dataHoraSaida = datetime.today()
        dataHoraEntrada = datetime.strptime(self.dataHoraEntrada, '%d/%m/%Y %H:%M')
        if dataHoraSaida < dataHoraEntrada:
            raise ValueError('Data ou horário de saída inválidos')
        else:
            self.status = 'Finalizado'
            self.dataHoraSaida = dataHoraSaida.strftime('%d/%m/%Y %H:%M')
            CartaoEstacionamento.numCartoesAtivos.remove(self.numCartao)
            self.valor = self.calcularValor()
            print('Saída confirmada. Até a proxima!')

    def __str__(self):
        return f'Cartão: {self.numCartao}\nEntrada: {self.dataHoraEntrada}\nSaida: {self.dataHoraSaida}\nStatus: {self.status}\nValor total: R${self.valor:.2f}'

def main():
    cartao1 =  CartaoEstacionamento(input('Digite a data e hora de entrada no formato dd/mm/aaaa hh:mm: '))
    cartao1.finalizarSaida()
    print(cartao1)
    cartao2 = CartaoEstacionamento(input('Digite a data e hora de entrada no formato dd/mm/aaaa hh:mm: '))
    print(cartao2.verValor())
    cartao2.finalizarSaida()
    cartao3 = CartaoEstacionamento(input('Digite a data e hora de entrada no formato dd/mm/aaaa hh:mm: '))
    print(cartao3)

if __name__ == '__main__':
    main()