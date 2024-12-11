"""
Este cheat sheet resume os conceitos e sintaxes de loops em Python, abordando os tipos principais de loops e exemplos práticos.
"""

# 1. **Laço de Repetição "for"**

# O "for" é usado para iterar sobre sequências (listas, tuplas, strings, dicionários, etc.)

# Exemplo 1: Iterando sobre uma lista
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)  # Saída: 1, 2, 3, 4, 5

# Exemplo 2: Iterando sobre uma string
string = "Python"
for char in string:
    print(char)  # Saída: P, y, t, h, o, n

# Exemplo 3: Usando a função range() para criar um intervalo de números
for i in range(5):  # range(5) gera [0, 1, 2, 3, 4]
    print(i)  # Saída: 0, 1, 2, 3, 4

# Exemplo 4: Iterando com "range" e criando um intervalo personalizado
for i in range(2, 10, 2):  # range(2, 10, 2) gera [2, 4, 6, 8]
    print(i)  # Saída: 2, 4, 6, 8

# 2. **Laço de Repetição "while"**

# O "while" continua executando enquanto a condição for verdadeira

# Exemplo 1: Simples loop while
contador = 0
while contador < 5:
    print(contador)  # Saída: 0, 1, 2, 3, 4
    contador += 1  # Incrementando o contador

# Exemplo 2: Loop com condição de parada
numero = 10
while numero > 0:
    print(numero)  # Saída: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    numero -= 1  # Decrementando o número

# 3. **Controle de Fluxo no Loop**

# Exemplo 1: "break" - Interrompe o loop imediatamente
for i in range(10):
    if i == 5:
        break  # O loop é interrompido quando i é 5
    print(i)  # Saída: 0, 1, 2, 3, 4

# Exemplo 2: "continue" - Pula para a próxima iteração
for i in range(5):
    if i == 3:
        continue  # Pula a iteração quando i é 3
    print(i)  # Saída: 0, 1, 2, 4

# Exemplo 3: "else" com "for" e "while"
# O bloco else após um loop será executado quando o loop terminar sem interrupção (sem um "break")

# "for" com else
for i in range(5):
    print(i)
else:
    print("Fim do loop for")  # Saída: 0, 1, 2, 3, 4, "Fim do loop for"

# "while" com else
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Fim do loop while")  # Saída: 0, 1, 2, 3, 4, "Fim do loop while"

# 4. **Compreensões de Lista**

# List comprehensions são uma forma compacta e eficiente de criar listas

# Exemplo 1: Criando uma lista com quadrados de números
quadrados = [x ** 2 for x in range(5)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16]

# Exemplo 2: Filtrando elementos de uma lista (exemplo com números pares)
numeros = [1, 2, 3, 4, 5, 6]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Saída: [2, 4, 6]

# Exemplo 3: Compreensão de dicionário
dicionario = {x: x ** 2 for x in range(5)}
print(dicionario)  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 5. **Nested Loops (Loops Aninhados)**

# Exemplo 1: Loop aninhado para imprimir uma matriz
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")  # Saída: (0, 0) (0, 1) (0, 2) (1, 0) (1, 1) (1, 2) (2, 0) (2, 1) (2, 2)
    print()  # Para pular para a próxima linha

# Exemplo 2: Usando loops aninhados para multiplicar listas (matriz 2x2)
matriz = [[1, 2], [3, 4]]
for linha in matriz:
    for elemento in linha:
        print(elemento)  # Saída: 1, 2, 3, 4

# 6. **Loops com Enumerate**

# A função `enumerate()` adiciona um contador a um iterável e retorna os valores como tuplas (índice, valor)

# Exemplo 1: Usando enumerate para iterar com índices
frutas = ['maçã', 'banana', 'laranja']
for index, fruta in enumerate(frutas):
    print(f"Índice {index}: {fruta}")  
    # Saída:
    # Índice 0: maçã
    # Índice 1: banana
    # Índice 2: laranja

# Exemplo 2: Começando a enumeração a partir de um número específico
for index, fruta in enumerate(frutas, start=1):
    print(f"Índice {index}: {fruta}")  
    # Saída:
    # Índice 1: maçã
    # Índice 2: banana
    # Índice 3: laranja

# Fim do Cheat Sheet
