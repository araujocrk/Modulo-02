"""
Este cheat sheet resume os conceitos fundamentais sobre tuplas em Python, incluindo como criar, acessar e utilizar métodos comuns.
"""

# Definindo uma tupla
# Uma tupla é uma coleção ordenada e imutável
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)  # Saída: (1, 2, 3, 4, 5)

# Tupla com um único elemento (precisa da vírgula)
tupla2 = (5,)
print(tupla2)  # Saída: (5,)

# Tupla vazia
tupla_vazia = ()
print(tupla_vazia)  # Saída: ()

# Tupla com diferentes tipos de dados
tupla3 = (1, "string", 3.14, True)
print(tupla3)  # Saída: (1, 'string', 3.14, True)

# Acessando elementos de uma tupla (indexação)
print(tupla1[0])  # Saída: 1
print(tupla1[-1])  # Saída: 5 (último elemento)

# Fatiamento de tupla
print(tupla1[1:4])  # Saída: (2, 3, 4)

# Verificando se um valor está na tupla
print(3 in tupla1)  # Saída: True
print(10 in tupla1)  # Saída: False

# Comprimento da tupla
print(len(tupla1))  # Saída: 5

# Iterando sobre uma tupla
for elemento in tupla1:
    print(elemento)

# Concatenando tuplas
tupla4 = (6, 7, 8)
tupla_concatenada = tupla1 + tupla4
print(tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 6, 7, 8)

# Repetindo tuplas
tupla_repetida = tupla1 * 2
print(tupla_repetida)  # Saída: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Desempacotamento de tupla
a, b, c, d, e = tupla1
print(a, b, c, d, e)  # Saída: 1 2 3 4 5

# Contagem de elementos (quantas vezes um valor aparece na tupla)
print(tupla1.count(3))  # Saída: 1 (o valor 3 aparece uma vez)

# Índice de um valor (posição de um valor na tupla)
print(tupla1.index(4))  # Saída: 3 (o valor 4 está no índice 3)

# Tuplas são imutáveis: não podemos alterar diretamente um valor
# tupla1[0] = 10  # Isso causaria um erro TypeError

# Criando uma tupla a partir de uma lista
lista = [1, 2, 3, 4]
tupla_lista = tuple(lista)
print(tupla_lista)  # Saída: (1, 2, 3, 4)

# Criando uma tupla a partir de elementos separados por vírgula (de forma direta)
tupla_direta = 1, 2, 3, 4
print(tupla_direta)  # Saída: (1, 2, 3, 4)

# Operações com tuplas (não modificáveis)
tupla_imutavel = (10, 20, 30)
# tupla_imutavel[0] = 100  # Isso causaria um erro TypeError

print("Fim do cheat sheet!")
