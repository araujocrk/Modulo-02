class RadioFM:
    estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}
    def __init__(self):
        self.__freq_min = 88
        self.freq = 89.5
        self.__freq_max = 108
        self.estacoes = RadioFM.estacoes
        self.estacaoAtual = 'Cocais'
        self.ligado = True
        self.antenaHabilitada = True

    @property
    def freq_min(self):
        return self.__freq_min
    
    @property
    def freq_max(self):
        return self.__freq_max
    
    def mudarFrequencia(self, nova_freq = 0):
        chaves = list(self.estacoes.keys())
        if self.ligado and self.antenaHabilitada:
            if (nova_freq == 0) and (self.freq in chaves):
                indiceInicio = chaves.index(self.freq) + 1
                chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                iterador = iter(chaves)
                self.freq = next(iterador)
                self.estacaoAtual = self.estacoes[self.freq]
                
            elif (nova_freq >= self.freq_min) and (nova_freq <= self.freq_max) and (nova_freq in chaves):
                indiceInicio = chaves.index(nova_freq)
                chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                iterador = iter(chaves)
                self.freq = next(iterador)
                self.estacaoAtual = self.estacoes[self.freq]
            elif (nova_freq >= self.freq_min) and (nova_freq <= self.freq_max) and (nova_freq not in chaves):
                    self.freq = nova_freq
                    self.estacaoAtual = 'Estação inexistente'
            elif (nova_freq == 0) and (self.freq not in chaves):
                freqMaisProxima = self.freqMaisProxima(self.freq)
                indiceInicio = chaves.index(freqMaisProxima)
                chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                iterador = iter(chaves)
                self.freq = next(iterador)
                self.estacaoAtual = self.estacoes[self.freq]
            else:
                print('erro')
        
    def freqMaisProxima(self, nova_freq):
        mais_proxima = min(self.estacoes, key=lambda freq: abs(freq - nova_freq))
        return mais_proxima
    
def main():
    radio1 = RadioFM()
    print(radio1.freq)
    print(radio1.estacaoAtual)
    radio1.mudarFrequencia()
    print(radio1.freq)
    print(radio1.estacaoAtual)
    radio1.mudarFrequencia(95.0)
    print(radio1.freq)
    print(radio1.estacaoAtual)
    radio1.mudarFrequencia()
    print(radio1.freq)
    print(radio1.estacaoAtual)
    


    
if __name__ == '__main__':
    main()