from datetime import *
class CartaoEmbarque:
    def __init__ (self, nome, numeroVoo, codigoDeReserva, data, horario, checkIn, assento):
        self.nome = nome
        self.numeroVoo = numeroVoo
        self.codigoDeReserva = codigoDeReserva
        self.data = self.validarData(data)
        self.horario = self.validarHorario(horario)
        self.checkIn = checkIn
        self.assento = assento
    
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
        
def main():
    
if __name__ == '__main__':
    main()
        