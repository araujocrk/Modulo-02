class RadioFM:
    estacoes = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}
    def __init__(self, vol_max):
        self.__vol_min = 0
        self.vol = 0
        self.__vol_max = vol_max
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
    def vol_max(self):
        return self.__vol_max

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
        self.freq = 0
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
                # 1. Usuário não passou argumento e frequência atual está no dicionário ex: 89.5
                if (nova_freq == 0) and (self.freq in chaves):
                    # 1. Indice vai ser o próximo após a frequencia atual ex: 1
                    indiceInicio = chaves.index(self.freq) + 1
                    # 1. Próxima frequencia vai ser o primeiro da lista ex: 91.5, 94.1, 99.1, 89.5
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    # 1. Cria um iterador
                    iterador = iter(chaves)
                    # 1. Frequencia atual recebe o primeiro da lista ex: 91.5
                    self.freq = next(iterador)
                    # 1. Estacao atual recebe a estacao da frequencia atual ex: Mix
                    self.estacaoAtual = self.estacoes[self.freq]
                # 2. Usuário passou argumento e a frequência está no dicionário ex: 94.1  
                elif (nova_freq >= self.freq_min) and (nova_freq <= self.freq_max) and (nova_freq in chaves):
                    # 2. Indice vai ser o da frequencia passada pelo usuário ex: 99.1
                    indiceInicio = chaves.index(nova_freq)
                    # 2. ex: 99.1, 89.5, 91.5, 94.1
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    # 2. Cria um iterador
                    iterador = iter(chaves)
                    # 2. Frequencia atual recebe o primeiro da lista ex: 99.1
                    self.freq = next(iterador)
                    # 2. Estacao atual recebe a estacao da frequencia atual ex: Clube
                    self.estacaoAtual = self.estacoes[self.freq]
                # 3. Usuário passou argumento e a frequência não está no dicionário
                elif (nova_freq >= self.freq_min) and (nova_freq <= self.freq_max) and (nova_freq not in chaves):
                        # 3. Frequencia atual recebe a frequencia passada ex: 95.0
                        self.freq = nova_freq
                        # 3. Estacao atual recebe 'Estação inexistente'
                        self.estacaoAtual = 'Estação inexistente'
                # 4. Usuário não passou argumento e a frequência atual não está no dicionário
                elif (nova_freq == 0) and (self.freq not in chaves):
                    # 4. Frequencia e estação atual recebem a frequencia mais próxima da digitada pelo usuário ex: 94.1
                    freqMaisProxima = self.freqMaisProxima(self.freq)
                    indiceInicio = chaves.index(freqMaisProxima)
                    chaves = chaves[indiceInicio:] + chaves[:indiceInicio]
                    iterador = iter(chaves)
                    self.freq = next(iterador)
                    self.estacaoAtual = self.estacoes[self.freq]
                else:
                    raise Exception('Frequência inválida. Tente uma frequência entre {self.freq_min} e {self.freq_max}.')
            else:
                raise Exception('Radio desligado ou antena desabilitada. Tente ligar o radio ou habilitar a antena.')
        except ValueError:
            raise ValueError('Frequência inválida. Tente digitar valores numéricos.')   

    def freqMaisProxima(self, nova_freq):
        # Verifica qual é o menor valor absoluto entre as frequencias do dicionário e a nova frequencia
        maisProxima = min(self.estacoes, key=lambda freq: abs(freq - nova_freq))
        # E retorna a frequência mais proxima
        return maisProxima
    
    def __str__(self):
        return f'Frequência: {self.freq}\nEstação: {self.estacaoAtual}\nVolume: {self.vol}'
    
def main():
    radio1 = RadioFM(10)
    radio1.ligar()
    radio1.habilitarAntena()
    radio1.mudarFrequencia()
    radio1.aumentarVolume(5)
    print(radio1)
    radio1.desligar()
    
    radio2 = RadioFM(20)
    radio2.ligar()
    radio2.aumentarVolume(15)
    radio2.habilitarAntena()
    radio2.mudarFrequencia(94.1)
    radio2.diminuirVolume(5)
    print(radio2)
    radio2.desabilitarAntena()
    radio2.desligar()
    
    radio3 = RadioFM(30)
    radio3.habilitarAntena()
    radio3.ligar()
    radio3.aumentarVolume(25)
    radio3.mudarFrequencia(92)
    radio3.diminuirVolume(10)
    print(radio3)
    radio3.mudarFrequencia()
    print(radio3)
    radio3.desabilitarAntena()
    radio3.desligar()

if __name__ == '__main__':
    main()
        