import random
class Jogo:
    escolhaComputador = None
    escolhaUsuario = None
    opcoes = ['pedra', 'papel', 'tesoura']
    
    def obterEscolhaUsuarioAndComputador(self):
        self.escolhaUsuario = input('Escolha Pedra, Papel ou Tesoura: ').strip().lower()
        self.escolhaComputador = random.choice(self.opcoes)
        if self.escolhaUsuario in self.opcoes:
            return self.escolhaUsuario
        else:
            print('Escolha inválida. Tente novamente!')
            return self.obterEscolhaUsuario()

    def obterResultado(self):
        if self.escolhaComputador == self.escolhaUsuario:
            return 'Empate!'
        elif (self.escolhaUsuario == 'pedra' and self.escolhaComputador == 'tesoura') or \
             (self.escolhaUsuario == 'papel' and self.escolhaComputador == 'pedra') or \
             (self.escolhaUsuario == 'tesoura' and self.escolhaComputador == 'papel'):
            return 'Você venceu!'
        else:
            return 'Você perdeu!'    

def main():
    print('Bem-vindo ao jogo Pedra, Papel e Tesoura!')
    meuJogo = Jogo()
    while True:
        meuJogo.obterEscolhaUsuarioAndComputador()
        print(f'Computador escolheu {meuJogo.escolhaComputador}')
        print(meuJogo.obterResultado())
        vaiContinuar = input('Jogar Novamente? (S/N): ').strip().lower()
        if vaiContinuar[0] == 'n':
            print('Encerrando o jogo...')
            break
        elif vaiContinuar[0] == 's':
            pass
        else:
            print('Opção inválida! Jogo reiniciado.')

if __name__ == '__main__':
    main()