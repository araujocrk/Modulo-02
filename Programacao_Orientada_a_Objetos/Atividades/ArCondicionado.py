class ArCondicionado:
    def __init__(self, temp_min, temp_max, vel_min, vel_max, ligado = False, modo = 'Automático', velocidade = 0, temperatura = 0):
        self.__temp_min = temp_min
        self.__temp_max = temp_max
        self.__vel_min = vel_min
        self.__vel_max = vel_max
        self.ligado = ligado
        self.modo = modo
        self.velocidade = velocidade
        self.temperatura = temperatura
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            self.modo = 'Automático'
        

def main():
    arCondicionado1 = ArCondicionado(16, 30, 1, 5)
if __name__ == '__main__':
    main()
        