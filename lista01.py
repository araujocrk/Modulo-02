#Questão 01
def par_impar(n):
    return n % 2 == 0

#Questão 02
def area(r):
    PI = 3.14
    return PI * (r ** 2)

def perimetro(r):
    PI = 3.14
    return PI * 2 * r

#Questão 03
def fahrenheit_To_Celsius(f):
    return ((f-32)/9)*5

#Questão 04
def passou_De_Ano(n1, n2):
    media = (n1 + n2) / 2
    if media >= 6:
        return f'Média: {media}\nPARABÉNS! Você foi aprovado!'
    else:
        return f'Média: {media}\nVocê foi reprovado!'

def main():
#Questão 01
#Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
    while True:
        try:
            num = int(input('Digite um número inteiro: '))
            if par_impar(num) == True:
                print('Este número é par!')
            else:
                print('Este número é impar!')
            break
        except:
            print('Número inválido. Tente novamente!')

#Questão 02
#Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área
# do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
# Área = PI * r2; Perímetro = PI * 2 * r;
    while True:
        try:
            raio = float(input('Digite o raio do círculo: '))
            print(area(raio))
            print(perimetro(raio))
            break
        except:
            print('Número inválido. Tente novamente!')

# 3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar
# o valor correspondente em graus Celsius.
# Fórmula: C = ((F-32)/9)*5
    while True:
        try:
            fah = float(input('Digite a temperatura em fahrenheit: '))
            print(f'{fahrenheit_To_Celsius(fah):.2f}')
            break
        except:
            print('Temperatura inválida. Tente Novamente!')

# 4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas
# notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno
# foi aprovado (considere 6.0 a média mínima para aprovação).
    while True:
        try:
            n1 = float(input('Digite sua primeira nota: '))
            n2 = float(input('Digite sua segunda nota: '))
            print(passou_De_Ano(n1, n2))
            break
        except:
            print('Nota inválida. Tente novamente!')

if __name__ == '__main__':
    main()