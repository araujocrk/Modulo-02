class RadioFM:
    estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}
    def __init__(self, vol_max):
        self.__vol_min = 0
        self.vol = 0
        self.vol_max = vol_max
        self.__freq_min = 88
        self.freq = 0
        self.__freq_max = 108
        self.estacoes = RadioFM.estacoes
        self.estacaoAtual = None
        self.antenaHabilitada = False
        self.ligado = False
        
    @property
    def vol_min(self):
        return self.__vol_min

    @property
    def freq_min(self):
        return self.__freq_min
    
    @property
    def freq_min(self):
        return self.__freq_max
    
    def ligar(self):
        self.ligado = True
        self.vol = self.vol_min
        if self.antenaHabilitada:
            self.freq = next(iter(self.estacoes.keys()))
            self.estacaoAtual = next(iter(self.estacoes.values()))
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
                    raise Exception('Volume inválido. Tente digitar valores numéricos inteiros positivos.')
            else:
                raise Exception('Radio desligado. Tente ligar.')
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
                    raise Exception('Volume inválido. Tente digitar valores numéricos inteiros positivos.')
            else:
                raise Exception('Radio desligado. Tente ligar.')
        except ValueError:
            raise ValueError('Volume inválido. Tente digitar valores numéricos positivos.')
        except TypeError:
            raise TypeError('Volume inválido. Tente digitar valores numéricos positivos.')
    
    def mudarFrequencia(self, nova_freq = 0):
        try:
            chaves = list(self.estacoes.keys())
            if self.ligado and self.antenaHabilitada:
                if nova_freq == 0 and self.freq in chaves or nova_freq >= self.freq_min and nova_freq <= self.freq_max and nova_freq in chaves:
                    if self.freq and self.freq in chaves:
                        indiceInicio = chaves.index(self.freq) + 1
                        chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                        iterador = iter(chaves)
                        self.freq = next(iterador)
                        self.estacaoAtual = self.estacoes[self.freq]
                elif nova_freq == 0 and self.freq not in chaves:
                    nova_freq = self.freqMaisProxima(nova_freq)
                    indiceInicio = chaves.index(self.freq)
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    iterador = iter(chaves)
                    self.freq = next(iterador)
                    self.estacaoAtual = self.estacoes[self.freq]
                elif nova_freq >= self.freq_min and nova_freq <= self.freq_max and nova_freq not in chaves:
                    self.freq = nova_freq
                    self.estacao = 'Estação inexistente'    
        except ValueError:
            raise ValueError('Frequência inválida. Tente digitar valores numéricos positivos.')   

    def freqMaisProxima(self, nova_freq):
        mais_proxima = min(self.estacoes, key=lambda freq: abs(freq - nova_freq))
        return mais_proxima
def main():
    radio1 = RadioFM(10)
    radio1.habilitarAntena()
    radio1.ligar()
    print(radio1.freq)
    #radio1.aumentarVolume()
    radio1.mudarFrequencia()
    print(radio1.freq)
    radio1.mudarFrequencia()
    print(radio1.freq)
    radio1.mudarFrequencia()
    print(radio1.freq)
    radio1.mudarFrequencia()
    print(radio1.freq)

if __name__ == '__main__':
    main()
        