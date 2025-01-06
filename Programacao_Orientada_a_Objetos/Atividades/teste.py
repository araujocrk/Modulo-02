class ArCondicionado:
    def __init__(self, velocidade = 'Não informada'):
        if velocidade >= 16 and velocidade <= 28:
            self.velocidade = velocidade
        elif velocidade == 0:
            self.velocidade = 'Nao informada'
        else:
            raise ValueError(f'Erro: A velocidade deve estar entre 16 e 28.')
    
    def __str__(self):
        return f'Configurações atuais do ar condicionado:\nVelocidade: {self.velocidade}'
    
def atributosArCondionado():
    print('Iniciando configurações do ar condicionado...')
    velocidade = input(f'Qual a velocidade do ar condicionado (entre 16 e 26 ou deixe em branco): ') or 0
    velocidade = int(velocidade)
    return velocidade

def main():
    arCondicionado1 = ArCondicionado(atributosArCondionado())
    print(arCondicionado1)
if __name__ == '__main__':
    main()