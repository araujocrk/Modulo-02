# Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser 
# usada nas paredes. 
# Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. 
# Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura
# da sala em metros e em seguida imprima:
def main():
    
    class Sala:
        def __init__(self, comprimento, largura, altura):
            self.comprimento = comprimento
            self.largura = largura
            self.altura = altura
        
        def areaPiso(self):
            return self.comprimento * self.largura
        
        def volumeSala(self):
            return self.comprimento * self.largura * self.altura
        
        def areaParedes(self):
            return (2 * self.altura * self.largura) + (2 * self.altura * self.comprimento)
            
    minhaSala = Sala(
        float(input('Qual o comprimento de sua sala? ')),
        float(input('Qual a largura da sua sala? ')),
        float(input('Qual a altura da sua sala? '))
    )
    print(f'A área do piso da sua sala é {minhaSala.areaPiso()}cm²')
    print(f'O volume da sua sala é {minhaSala.volumeSala()}cm³')
    print(f'A área das suas paredes é {minhaSala.areaParedes()}cm²')
    
            
if __name__ == '__main__':
    main()