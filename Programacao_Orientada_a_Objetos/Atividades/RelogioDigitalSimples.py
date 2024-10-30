class RelogioDigitalSimples:
    def __init__ (self, hora, minuto):
        if 0 <= hora < 24 and 0 <= minuto < 60:
            self.hora = hora
            self.minuto = minuto
        #if 0 <= segundo < 60:
            #self.segundo = segundo
        #else:

    # Usei o parâmetro quantidade para não ter que usar vários métodos no main.
    def passarTempo(self, quantidade):
        #self.segundo += 1
        #if self.segundo == 60:
            #self.segundo = 0
        self.minuto += quantidade
        if self.minuto == 60:
            self.minuto = 0
            self.hora += 1
            if self.hora == 24:
                self.hora = 0
        
    def configurarHoraio(self):
        print('Configurações do relógio:')
        self.hora = int(input('Digite a hora: '))
        self.minuto = int(input('Digite o minuto: '))
        #self.segundo = int(input('Digite o segundo: '))
    
def main():
    try:
        relogio1 = RelogioDigitalSimples(int(input('Digite a hora: ')),
                                         int(input('Digite o minuto: ')))
        relogio1.passarTempo(int(input('Quantos minutos deseja avançar? ')))
        relogio1.passarTempo(int(input('Quantos minutos deseja avançar? ')))
        
        relogio2 = RelogioDigitalSimples(int(input('Digite a hora: ')),
                                         int(input('Digite o minuto: ')))
        relogio2.configurarHoraio()
        relogio2.passarTempo(int(input('Quantos minutos deseja avançar? ')))
        
        print(f'{relogio1.hora}:{relogio1.minuto}')
        print(f'{relogio2.hora}:{relogio2.minuto}')
    except ValueError:
        print('Horário inválido! Por favor, digite valores numéricos.')
    except AttributeError:
            print('Horário inválida! Por favor, digite valores entre 0 e 23; e entre 0 e 59.')

main()