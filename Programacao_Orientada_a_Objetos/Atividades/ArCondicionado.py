class ArCondicionado:
    def __init__(self, temp_min, temp_max, vel_min, vel_max, ligado = False, modo = 'Automático', 
                 velocidade = 'Não informada', temperatura = 'Não informada'):
        if temp_min > 0 and temp_min < temp_max: 
            self.__temp_min = temp_min
        else:
            raise ValueError('Erro: A temperatura minima deve ser menor que a temperatura maxima e maior que zero.')
        
        if temp_max <= 28:
            self.__temp_max = temp_max
        else:
            raise ValueError('Erro: A temperatura maxima deve ser menor ou igual a 28.')
        
        if vel_min > 0 and vel_min < vel_max:
            self.__vel_min = vel_min
        else:
            raise ValueError('Erro: A velocidade minima deve ser menor que a velocidade maxima e maior que zero.')
        
        if vel_max <= 5:
            self.__vel_max = vel_max
        else:
            raise ValueError('Erro: A velocidade maxima deve ser menor ou igual a 5.')
        
        if ligado == 'ligado':
            self.ligado = True
        elif not ligado or ligado == 'desligado':
            self.ligado = ligado
        else:
            raise ValueError('Erro: Responda com "sim" ou deixe em branco.')
        
        if modo[0] == 'f':
            self.modo = 'Frio'
        elif modo[0] == 'v':
            self.modo = 'Ventilar'
        elif modo[0] == 'a':
            self.modo = 'Automático'
            
        if velocidade >= vel_min and velocidade <= vel_max:
            self.velocidade = velocidade
        elif velocidade == 0:
            self.velocidade = vel_min
        else:
            raise ValueError(f'Erro: A velocidade deve estar entre {vel_min} e {vel_max}.')
        
        if temperatura >= temp_min and temperatura <= temp_max:
            self.temperatura = temperatura
        elif temperatura == 0:
            self.temperatura = temp_min
        else:
            raise ValueError(f'Erro: A temperatura deve estar entre {temp_min} e {temp_max}.')
        
    @property
    def temp_min(self):
        return self.__temp_min
    
    @property
    def temp_max(self):
        return self.__temp_max
    
    @property
    def vel_min(self):
        return self.__vel_min
    
    @property
    def vel_max(self):
        return self.__vel_max
        
    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print('O ar condicionado já está ligado.')
        
    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print('O ar condicionado já está desligado.')
            
    def aumentar_temperatura(self):
        if self.ligado:
            if (self.temperatura + 1) <= self.temp_max:
                self.temperatura += 1
            else:
                print('Temperatura máxima atingida.')
        else:
            print('Ar condicionado está desligado. Tente ligá-lo.')
            
    def diminuir_temperatura(self):
        if self.ligado:
            if (self.temperatura - 1) >= self.temp_min:
                self.temperatura -= 1
            else:
                print('Temperatura mínima atingida.')
        else:
            print('Ar condicionado está desligado. Tente ligá-lo.')
    
    # def aumentar_velocidade(self):
    #     if self.ligado:
    #         if (self.velocidade + 1)
            
        
    def __str__(self):
        #Printar Ligado ou Desligado e Modo formatados
        return f'Configurações atuais do ar condicionado:\nLigado: {self.ligado}\nModo: {self.modo}\nVelocidade: {self.velocidade}\nTemperatura: {self.temperatura}'

def atributosArCondionado():
    print('Iniciando configurações do ar condicionado...')
    temp_min = input('Qual a temperatura mínima*: ')
    temp_max = input('Qual a temperatura máxima*: ')
    vel_min = input('Qual a velocidade mínima*: ')
    vel_max = input('Qual a velocidade máxima*: ')
    ligado = input('O ar condicionado está ligado (ligado ou desligado): ').lower() or False
    modo = input('Qual o modo do ar condicionado (frio, ventilar ou automático): ').lower() or 'a'
    velocidade = input(f'Qual a velocidade do ar condicionado (entre {vel_min} e {vel_max} ou deixe em branco): ') or 0
    temperatura = input(f'Qual a temperatura do ar condicionado (entre {temp_min} e {temp_max} ou deixe em branco): ') or 0
    try:
        temp_min = int(temp_min)
        temp_max = int(temp_max)
        vel_min = int(vel_min)
        vel_max = int(vel_max)
        velocidade = int(velocidade)
        temperatura = int(temperatura)
    except ValueError:
        raise ValueError('Erro: As temperaturas e velocidades devem ser numeros inteiros e positivos.')
    return temp_min, temp_max, vel_min, vel_max, ligado, modo, velocidade, temperatura
    
def main():
    #Entradas obrigatórias: temp_min, temp_max, vel_min, vel_max
    #Entradas opcionais: ligado(true/false), modo(padrão=automático, frio, ventilar)
    #velocidade(entre vel_min e vel_max), temperatura(entre temp_min e temp_max)
    arCondicionado1 = ArCondicionado(*atributosArCondionado())
    print(arCondicionado1)
    arCondicionado1.aumentar_temperatura()
    print(arCondicionado1)
    arCondicionado1.aumentar_temperatura()
    print(arCondicionado1)
if __name__ == '__main__':
    main() 