class Bicicleta:
    def __init__(self, velocAtual, alturaSela, pressaoPneus):
        if self.velocValida(velocAtual):
            self.velocAtual = velocAtual
        else:
            raise ValueError('Velocidade inválida. Velocidade permitida até 60 km/h.\n')
        
        if self.alturaValida(alturaSela):
            self.alturaSela = alturaSela
        else:
            raise ValueError('Altura inválida. Altura permitida até 20 cm.\n')

        if self.pressaoValida(pressaoPneus):
            self.pressaoPneus = pressaoPneus
        else:
            raise ValueError('Pressão inválida. Pressão permitida até 50 psi.\n')
    
    def regularSela(self):
        if self.estaParado():
            altura = int(input('Para qual altura deseja colocar a sela (cm): '))
            if self.alturaValida(altura):
                self.alturaSela = altura
                return f'Sela regulada. Posição atual: {self.alturaSela} cm'
            else:
                print('Você tentou regular a sela para um lugar inválido. Tente Novamente!')
                return self.regularSela()
        else:
            return 'Não é possível regular sua sela. Sua bicicleta está em movimento.'
            
    def calibrarPneus(self):
        if self.estaParado():
            pressao = int(input('Qual a pressão que você deseja: '))
            if self.pressaoValida(pressao):
                self.pressaoPneus = pressao
                return f'Pressão alterada. Pressão atual: {self.pressaoPneus} psi'
            else:
                print('Não é possível ou recomendado calibrar a esse nível de pressão. Tente Novamente!')
                return self.calibrarPneus()
        else:
            return 'Não é pssivel calibrar seus pneus. Sua bicicleta está em movimento.'
            
    def estaParado(self):
        return self.velocAtual == 0
    
    def velocValida(self, velocidade):
        return 0 <= velocidade <= 60 
    
    def alturaValida(self, altura):
        return 0 <= altura <= 20
    
    def pressaoValida(self, pressao):
        return 0 <= pressao <= 50
            
def main():
    try:
        minhaBiclicleta = Bicicleta(int(input('Informe a velocidade atual em que você se encontra (km/h): ')),
                                    int(input('Informe a altura em que sua sela está posicionada (cm): ')),
                                    int(input('Informe a pressão dos pneus (psi): ')))
        print(minhaBiclicleta.regularSela())
        
        minhaBiclicleta2 = Bicicleta(int(input('Informe a velocidade atual em que você se encontra (km/h): ')),
                                    int(input('Informe a altura em que sua sela está posicionada (cm): ')),
                                    int(input('Informe a pressão dos pneus (psi): ')))
        print(minhaBiclicleta2.calibrarPneus())
        
    except ValueError as e:
        if 'invalid literal' in str(e):
            print(f'Erro: Tente usar valores numéricos inteiros.')
        elif 'inválida' in str(e):
            print(f'Erro: {e}')
        else:
            print('Erro desconhecido.')
    
main()