from datetime import *
from random import *
class CartaoEmbarque:
    assentos = ['A1', 'B1', 'C1', 'D1', 'A2', 'B2', 'C2', 'D2', 'A3', 'B3', 'C3', 'D3', 'A4', 'B4', 'C4', 'D4', 'A5', 'B5', 'C5', 'D5', 'A6', 'B6', 'C6', 'D6', 'A7', 'B7', 'C7', 'D7', 'A8', 'B8', 'C8', 'D8', 'A9', 'B9', 'C9', 'D9', 'A10', 'B10', 'C10', 'D10']
    assentosOcupados = []
    def __init__ (self, nome, numeroVoo, codigoDaReserva, data, horario, checkIn = 'Não realizado', assento = None):
        self.nome = nome
        self.numeroVoo = numeroVoo
        self.codigoDaReserva = codigoDaReserva
        self.data = self.validarData(data)
        self.horario = self.validarHorario(horario)
        self.checkIn = checkIn
        self.assento = self.assentoEstahDisponivel(self, assento)
    
    def validarData(self, dataStr):
        try:
            dia = int(dataStr[:2])
            mes = int(dataStr[2:4])
            ano = int(dataStr[4:])
        except ValueError:
            raise ValueError('Data inválida! Digite números no formato ddmmaaaa')
        if date(ano, mes, dia):
            return (dia * 1000000) + (mes * 10000) + ano
    
    def validarHorario(self, horario):
        try:
            hora = int(horario[:2])
            minuto = int(horario[2:])
        except ValueError:
            raise ValueError('Horário inválido! Digite números no formato hhmm')
        if time(hora, minuto):
            return (hora * 100) + minuto
    
    def checkIn(self):
        if self.checkIn == 'Não realizado':
            self.checkIn = 'Realizado'
            if self.assento == None:
                self.assento = self.assentoEstahDisponivel(self, random.choice(CartaoEmbarque.assentos))
            else:
                return self.checkIn(self)
        else:
            print('Check=in já foi realizado.')
            
    def assentoEstahDisponivel(self, assento):
        if assento in CartaoEmbarque.assentos:
            if assento not in CartaoEmbarque.assentosOcupados:
                self.assento = assento
                CartaoEmbarque.assentosOcupados.append(assento)
            else:
                print('Este assento já está ocupado.')
        else:
            raise ValueError('Assento inválido.')
        
    def alterarAssento(self):
        if self.checkIn == 'Realizado':
            CartaoEmbarque.assentosOcupados.remove(self.assento)
            assento = input('Para qual assento deseja mudar? ')
            self.assentoEstahDisponivel(self, assento)
        else:
        
        
    def __str__(self):
        return f'Nome: {self.nome}\nNúmero do Voo: {self.numeroVoo}\nCódigo da Reserva: {self.codigoDaReserva}\nData: {self.data}\nHorário: {self.horario}\nCheck In: {self.checkIn}\nAssento: {self.assento}'
        
def main():
    
if __name__ == '__main__':
    main()
        