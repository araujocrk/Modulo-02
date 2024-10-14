def main():
    class CalculadoraSimples:
        def __init__(self):
            self.resultado = None
        
        def operacoes(self, n1, simbolo, n2):
            if simbolo == '+':
                self.resultado = n1 + n2
            elif simbolo == '-':
                self.resultado = n1 - n2
            elif simbolo == '*':
                self.resultado = n1 * n2
            elif simbolo == '/':
                if n2 == 0:
                    self.resultado = 'Erro: Divisão por 0'
                else:
                    self.resultado = n1 / n2
            return self.resultado
    
    minhaCalculadora = CalculadoraSimples()
    minhaCalculadora.operacoes(
        float(input('Digite o primeiro número: ')), 
        input('Digite se você deseja somar(+), subtrair(-), multiplicar(*) ou dividir(/): '), 
        float(input('Digite o segundo número: '))
        )
    print(minhaCalculadora.resultado)
if __name__ == '__main__':
    main()