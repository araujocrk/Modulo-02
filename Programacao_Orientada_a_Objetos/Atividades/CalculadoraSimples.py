class CalculadoraSimples:
    n1 = 0
    n2 = 0
    operacao = None
            
    def operacoes(self):
        if self.operacao == '+':
            return self.n1 + self.n2
        elif self.operacao == '-':
            return self.n1 - self.n2
        elif self.operacao == '*':
            return self.n1 * self.n2
        elif self.operacao == '/':
            if self.n2 == 0:
                return 'Erro: Divisão por zero'
            else:
                return self.n1 / self.n2
        else:
            return 'Operação inválida'
def main():
    minhaCalculadora = CalculadoraSimples()
    while True:
        try:
            minhaCalculadora.n1 = float(input('Digite o primeiro número: '))
            minhaCalculadora.operacao = input('Escolha a operação (+, -, *, /): ')
            minhaCalculadora.n2 = float(input('Digite o segundo número: '))
            resultado = minhaCalculadora.operacoes()
            print(f'{minhaCalculadora.n1} {minhaCalculadora.operacao} {minhaCalculadora.n2} = {resultado}')
            vaiContinuar = input('Deseja continuar? (S/N) ').upper()
            if vaiContinuar[0] == 'N':
                print('Encerrando a calculadora...')
                break
        except ValueError:
            print('Por favor, digite valores numéricos válidos.')
            
if __name__ == '__main__':
    main()