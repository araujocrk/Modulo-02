class RadioFM:
    estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}
    def __init__(self, vol_max):
        self.__vol_min = 0
        self.vol = 0
        self.vol_max = vol_max
        self.__freq_min = 88
        self.freq = None
        self.__freq_max = 108
        self.__estacoes = RadioFM.estacoes
        self.estacaoAtual = None
        self.antenaHabilitada = False
        self.ligado = False
        
    @property
    def vol_min(self):
        return self.__vol_min
    
    @property
    def estacoes(self):
        return self.__estacoes
    
    def ligar(self):
        self.ligado = True
        self.vol = self.vol_min
        if self.antenaHabilitada:
            self.freq = next(iter(self.estacoes.keys))
            self.estacaoAtual = next(iter(self.estacoes.values))
    def desligar(self):
        self.ligado = False
        self.volume = 0
        self.freq = None
        self.estacaoAtual = None
    
    def habilitarAntena(self):
        self.antenaHabilitada = True
    def desabilitarAntena(self):
        self.antenaHabilitada = False
        
    def aumentarVolume(self, aumentar = 1):
        try:
            if self.ligado:
                if aumentar >= 0 and aumentar == int(aumentar):
                    if self.vol + aumentar < self.vol_max:
                        self.vol += aumentar
                    else:
                        self.vol = self.vol_max
                else:
                    raise ValueError('Volume inválido. Tente digitar valores numéricos inteiros positivos.')
            else:
                raise ValueError('Radio desligado. Tente ligar.')
        except ValueError:
            raise ValueError('Volume inválido. Tente digitar valores numéricos positivos.')
        except TypeError:
            raise TypeError('Volume inválido. Tente digitar valores numéricos positivos.')
        
    def diminuirVolume(self, diminuir = 1):
        try:
            if self.ligado:
                if diminuir >= 0 and diminuir == int(diminuir):
                    if self.vol - diminuir > self.vol_min:
                        self.vol -= diminuir
                    else:
                        self.vol = self.vol_min
                else:
                    raise ValueError('Volume inválido. Tente digitar valores numéricos inteiros positivos.')
            else:
                raise ValueError('Radio desligado. Tente ligar.')
        except ValueError:
            raise ValueError('Volume inválido. Tente digitar valores numéricos positivos.')
        except TypeError:
            raise TypeError('Volume inválido. Tente digitar valores numéricos positivos.')
def main():
    radio1 = RadioFM(10)
    radio1.habilitarAntena()
    radio1.ligar()
    radio1.aumentarVolume()
    print(radio1.vol)
    
    
if __name__ == '__main__':
    main()
        