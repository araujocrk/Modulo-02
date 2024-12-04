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
    def freq_max(self):
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
                # 1. Usuário não passou argumento e frequência atual está no dicionário ex: 91.5
                if (nova_freq == 0) and (self.freq in chaves):
                    # 1. Indice vai ser o próximo após a frequencia atual ex: 94.1
                    indiceInicio = chaves.index(self.freq) + 1
                    # 1. Próxima frequencia vai ser o primeiro da lista ex: 94.1, 99.1, 89.5, 91.5 
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    # 1. Cria um iterador
                    iterador = iter(chaves)
                    # 1. Frequencia atual recebe o primeiro da lista ex: 94.1
                    self.freq = next(iterador)
                    # 1. Estacao atual recebe a estacao da frequencia atual ex: Boa
                    self.estacaoAtual = self.estacoes[self.freq]
                    
                # 3. Usuário passou argumento e a frequência está no dicionário ex: 94.1
                elif (nova_freq >= self.freq_min) and (nova_freq <= self.freq_max) and (nova_freq in chaves):
                    # 3. Indice vai ser o próximo após a frequencia atual ex: 99.1
                    indiceInicio = chaves.index(self.freq)
                    # 3. Próxima frequencia vai ser o primeiro da lista ex: 99.1, 89.5, 91.5, 94.1
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    # 3. Cria um iterador
                    iterador = iter(chaves)
                    # 3. Frequencia atual recebe o primeiro da lista ex: 99.1
                    self.freq = next(iterador)
                    # 3. Estacao atual recebe a estacao da frequencia atual ex: Clube
                    self.freq = next(iterador)
                    
                # 4. Usuário passou argumento e a frequência não está no dicionário
                elif (nova_freq >= self.freq_min) and (nova_freq <= self.freq_max) and (nova_freq not in chaves):
                    self.freq = nova_freq
                    self.estacaoAtual = 'Estação inexistente'
                
                # 2. Usuário não passou argumento e a frequência atual não está no dicionário
                elif (nova_freq == 0) and (self.freq not in chaves):
                    # 2. A frequência vai ser mudada para a frequência mais próxima da atual
                    freqMaisProxima = self.freqMaisProxima(self.freq)
                    indiceInicio = chaves.index(freqMaisProxima)
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    iterador = iter(chaves)
                    self.freq = next(iterador)
                    self.estacaoAtual = self.estacoes[self.freq]
                
                else:
                    raise Exception(f'Frequência inválida. Tente digitar uma frequência entre {self.freq_min} e {self.freq_max}.')
            else:
                raise Exception('Radio desligado ou antena desabilitada. Tente ligar o rádio ou habilitar a antena.')
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
    print(radio1.estacaoAtual)
    # radio1.mudarFrequencia()
    # print(radio1.freq)
    # print(radio1.estacaoAtual)
    # radio1.mudarFrequencia(89.5)
    # print(radio1.freq)
    # print(radio1.estacaoAtual)
    
    # 4 entradas válidas possíveis: não passar o argumento mas estar ou não no dicionario(1,2), passar o argumento e estar no dicionário(3), passar o argumento e não está no dicionario(4)

if __name__ == '__main__':
    main()
        