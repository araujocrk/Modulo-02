from datetime import *
import random
class CartaoEmbarque:
    # Assentos totais
    assentos = ['A1', 'B1', 'C1', 'D1', 'A2', 'B2', 'C2', 'D2', 'A3', 'B3', 'C3', 'D3', 'A4', 'B4', 'C4', 'D4', 'A5', 'B5', 'C5', 'D5', 'A6', 'B6', 'C6', 'D6', 'A7', 'B7', 'C7', 'D7', 'A8', 'B8', 'C8', 'D8', 'A9', 'B9', 'C9', 'D9', 'A10', 'B10', 'C10', 'D10']
    # Assentos disponíveis
    assentosDisponiveis = ['A1', 'B1', 'C1', 'D1', 'A2', 'B2', 'C2', 'D2', 'A3', 'B3', 'C3', 'D3', 'A4', 'B4', 'C4', 'D4', 'A5', 'B5', 'C5', 'D5', 'A6', 'B6', 'C6', 'D6', 'A7', 'B7', 'C7', 'D7', 'A8', 'B8', 'C8', 'D8', 'A9', 'B9', 'C9', 'D9', 'A10', 'B10', 'C10', 'D10']
    # Assentos ocupados
    assentosOcupados = []
    def __init__ (self, nome, numeroVoo, codigoDaReserva, data, horario, checkIn = 'Não realizado', assento = 'Não informado'):
        self.nome = nome
        self.numeroVoo = numeroVoo
        self.codigoDaReserva = self.validarCodigoDaReserva(codigoDaReserva)
        self.dataHoraEmbarque = self.validarDataHora(data, horario)
        # Se o usuário não informar o check-in, será marcado como "não realizado"
        if checkIn == 'Realizado':
            self.checkIn = 'Realizado'
            if assento is None:
                self.assento = self.assentoEstahDisponivel(random.choice(CartaoEmbarque.assentosDisponiveis))
            else:
                self.assento = self.assentoEstahDisponivel(assento)
        else:
            self.checkIn = 'Não realizado'
            self.assento = 'Não informado'
        
    
    def validarDataHora(self, dataStr, horario):
        # Tenta converter a data no formato string em variáveis dia, mes e ano no formato inteiro, caso falhe, lança um ValueError
        try:
            dia = int(dataStr[:2])
            mes = int(dataStr[2:4])
            ano = int(dataStr[4:])
        except ValueError:
            raise ValueError('Data inválida! Digite números válidos no formato ddmmaaaa')
         # Tenta converter o horário no formato string em variáveis hora e minuto no formato inteiro, caso falhe, lança um ValueError
        try:
            hora = int(horario[:2])
            minuto = int(horario[2:])
        except ValueError:
            raise ValueError('Horário inválido! Digite números válidos no formato hhmm')
        horaAtual = datetime.now()
        horaEmbarque = datetime(ano, mes, dia, hora, minuto)
        if horaEmbarque > horaAtual:
            print('Horário válido para embarque.')
            return horaEmbarque
        else:
            raise ValueError('Horário inválido! O horário informado deve ser posterior ao horário atual.')
    
    def validarCodigoDaReserva(self, codigoDaReserva):
        # Se o código da reserva for alfabetico e tiver 6 caracteres, retorna o código da reserva, se não, lança um ValueError
        if codigoDaReserva.isalnum() and len(codigoDaReserva) == 6:
            return codigoDaReserva
        else:
            raise ValueError('Código da reserva inválido!')
            
    def assentoEstahDisponivel(self, assento):
        # Se o assento estiver na lista de assentos e não estiver ocupado, ele será removido da lista de assentos disponíveis
        # e será adicionado na lista de assentos ocupados e retorna o assento, se nao, lanca um ValueError
        if assento in CartaoEmbarque.assentos:
            if assento in CartaoEmbarque.assentosDisponiveis:
                CartaoEmbarque.assentosDisponiveis.remove(assento)
                CartaoEmbarque.assentosOcupados.append(assento)
                print('Assento escolhido com sucesso!')
                return assento
            # Se o assento estiver ocupado, ele será escolhido aleatoriamente
            else:
                print('Este assento já está ocupado.')
                print('Procurando assento disponível...')
                return self.assentoEstahDisponivel(random.choice(CartaoEmbarque.assentosDisponiveis))
        else:
            raise ValueError('Assento inválido.')
        
    def realizarCheckIn(self):
        # Verifica se o check-in já foi realizado, se não, ele será realizado e o assento será escolhido aleatoriamente
        if self.checkIn[0] == 'N':
            self.checkIn = 'Realizado'
            # Se o assento for nulo, ele será escolhido aleatoriamente
            self.assento = self.assentoEstahDisponivel(random.choice(CartaoEmbarque.assentosDisponiveis))
        else:
            print('Check=in já foi realizado.')
        
    def alterarAssento(self, assento):
        # Se o check-in foi realizado, remove o assento da lista de assentos ocupados e solicita ao usuário qual assento ele deseja e verifica se ele estaá disponível
        if self.checkIn[0] == 'R':
            CartaoEmbarque.assentosOcupados.remove(self.assento)
            #assento = input('Para qual assento deseja mudar? ')
            self.assentoEstahDisponivel(assento)
        else:
            print('Check-in ainda não foi realizado.')
        
    def __str__(self):
        return f'Nome: {self.nome}\nNúmero do Voo: {self.numeroVoo}\nCódigo da Reserva: {self.codigoDaReserva} \
        \nData e Hora do Embarque: {self.dataHoraEmbarque}\nCheck-in: {self.checkIn}\nAssento: {self.assento}'
    
def atributosCartaoEmbarque():
    nome = input('Nome: ')
    numeroVoo = input('Número do Voo: ')
    codigoDaReserva = input('Código da Reserva: ')
    data = input('Data (ddmmaaaa): ')
    horario = input('Horário (hhmm): ')
    checkIn = input('Check-in (realizado ou deixe em branco): ').upper() or None
    assento = input('Assento (ou deixe em branco): ') or None
    return nome, numeroVoo, codigoDaReserva, data, horario, checkIn, assento
        
def main():
    #cartao1 = CartaoEmbarque(*atributosCartaoEmbarque())
    #print(cartao1)
    cartao1 = CartaoEmbarque('Ryan da Silva Araújo', '2311', 'AB12CD', '22112024', '1800', None, None)
    cartao1.realizarCheckIn()
    cartao1.alterarAssento('A7')
    print(cartao1)
    cartao2 = CartaoEmbarque('Ramon da Silva Araújo', '2311', 'AB13CD', '22112024', '1800', None, None)
    cartao2.realizarCheckIn()
    cartao2.alterarAssento('B7')
    print(cartao2)
    cartao3 = CartaoEmbarque('Fernando Godoi', '2311', 'AB14CD', '22112024', '1800', 'Realizado', 'A8')
    print(cartao3)
    
    
    
    
if __name__ == '__main__':
    main()
        