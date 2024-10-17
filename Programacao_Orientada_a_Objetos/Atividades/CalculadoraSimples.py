def main():
    class CalculadoraSimples:
        n1 = 0
        n2 = 0
        operacao = None
            
        def operacoes(self, n1, n2, operacao):
            self.n1 = n1
            self.n2 = n2
            self.operacao = operacao
            
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
    
    minhaCalculadora = CalculadoraSimples()
    while True:
        try:
            numero1 = float(input('Digite o primeiro número: '))
            numero2 = float(input('Digite o segundo número: '))
            operacao = input('Escolha a operação (+, -, *, /) ou "s" para sair: ')
            if operacao == 's':
                print('Encerrando a calculadora...')
                break
            resultado = minhaCalculadora.operacoes(numero1, numero2, operacao)
            print(f'{minhaCalculadora.n1} {minhaCalculadora.operacao} {minhaCalculadora.n2} = {resultado}')
            vaiContinuar = input('Deseja continuar? (S/N): ')
            if vaiContinuar.upper() == 'N':
                break
        except ValueError:
            print('Por favor, digite valores numéricos válidos.')
            
if __name__ == '__main__':
    main()