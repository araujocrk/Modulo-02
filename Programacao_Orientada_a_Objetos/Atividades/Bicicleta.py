class Bicicleta:
    def __init__(self, velocAtual, alturaSela, pressaoPneus):
        if self.velocValida(velocAtual):
            self.velocAtual = velocAtual
        else:
            print('Velocidade não correspondida pelas métricas de nosso sistema. Tente Novamente!')
            main()
        if self.alturaValida(alturaSela):
            self.alturaSela = alturaSela
        else:
            print('Altura não correspondida pelas métricas de nosso sistema. Tente Novamente!')
            main()
        if self.calibragemValida(pressaoPneus):
            self.pressaoPneus = pressaoPneus
        else:
            print('Calibragem não correspondida pelas métricas de nosso sistema. Tente Novamente!')
            main()
    
    def regularSela(self):
        if self.estaParado(self):
            altura = int(input('Para qual altura deseja colocar a sela: '))
            if self.alturaValida(self, altura):
                self.alturaSela = altura
            else:
                print('Você tentou regular a sela para um lugar inválido. Tente Novamente!')
                return self.regularSela(self)
        else:
            print('Não é possível regular sua sela. Sua bicicleta está em movimento.')
            
    def calibrarPneus(self):
        if self.estaParado(self):
            pressao = int(input('Qual a pressão que você deseja: '))
            if self.calibragemValida(self, pressao):
                self.pressaoPneus = pressao
            else:
                print('Não é possível ou recomendado calibrar a esse nível de pressão. Tente Novamente!')
                return self.calibrarPneus(self)
        else:
            print('Não é pssivel calibrar seus pneus. Sua bicicleta está em movimento.')
            
    def estaParado(self):
        return self.velocAtual == 0
    
    def velocValida(self, velocidade):
        return 0 <= velocidade <= 60 
    
    def alturaValida(self, altura):
        return 0 <= altura <= 20
    
    def calibragemValida(self, pressao):
        return 0 <= pressao <= 50
            
def main():
    try:
        minhaBiclicleta = Bicicleta(int(input('Informe a velocidade atual em que você se encontra (km/h): ')),
                                    int(input('Informe a altura em que sua sela está posicionada (cm): ')),
                                    int(input('Informe a calibragem dos pneus (psi): ')))
        
        minhaBiclicleta.regularSela()
    except ValueError:
        print('Erro! Tente usar valores numéricos inteiros.')
    
main()