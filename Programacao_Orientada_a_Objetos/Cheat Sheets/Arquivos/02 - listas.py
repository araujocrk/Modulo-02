"""
Este é um resumo dos métodos e funcionalidades mais comuns para trabalhar com listas em Python.
"""

# Criando uma lista
minha_lista = [1, 2, 3, 4, 5]

# Acessando elementos
primeiro = minha_lista[0]  # Primeiro elemento
ultimo = minha_lista[-1]   # Último elemento

# Fatiamento (slicing)
sublista = minha_lista[1:4]  # Elementos do índice 1 ao 3
passos = minha_lista[::2]    # Elementos com intervalo de 2
reversa = minha_lista[::-1]  # Lista em ordem inversa

# Adicionando elementos
minha_lista.append(6)         # Adiciona 6 ao final
minha_lista.extend([7, 8])    # Adiciona vários elementos
minha_lista.insert(2, "novo") # Insere 'novo' no índice 2

# Removendo elementos
minha_lista.remove("novo")   # Remove a primeira ocorrência de 'novo'
removido = minha_lista.pop() # Remove e retorna o último elemento
removido_index = minha_lista.pop(2)  # Remove e retorna o elemento do índice 2
minha_lista.clear()          # Remove todos os elementos da lista

# Encontrando elementos
indice = minha_lista.index(3)      # Retorna o índice da primeira ocorrência de 3
existe = 4 in minha_lista          # Verifica se 4 está na lista

# Ordenação
minha_lista.sort()                 # Ordena a lista em ordem crescente
minha_lista.sort(reverse=True)     # Ordena a lista em ordem decrescente
lista_ordenada = sorted(minha_lista)  # Retorna uma nova lista ordenada

# Copiando listas
copia_rasa = minha_lista.copy()   # Retorna uma cópia rasa da lista
copia_rasa = minha_lista[:]       # Outra forma de copiar

# Iterando sobre uma lista
for item in minha_lista:          # Itera sobre os itens
    print(item)

# Compreensão de listas
quadrados = [x**2 for x in range(5)]  # Exemplo: [0, 1, 4, 9, 16]

# Funções úteis
tamanho = len(minha_lista)       # Número de elementos na lista
maior = max(minha_lista)         # Maior elemento
menor = min(minha_lista)         # Menor elemento
soma = sum(minha_lista)          # Soma dos elementos (se forem números)
encontrar = minha_lista.count(3) # Conta quantas vezes 3 aparece

# Concatenando listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2  # Combina lista1 e lista2
lista1.extend(lista2)               # Adiciona os elementos de lista2 em lista1

# Desempacotando listas
a, b, c = [1, 2, 3]                 # Atribui 1 a 'a', 2 a 'b' e 3 a 'c'

# Removendo duplicados
lista_unica = list(set(minha_lista))  # Remove duplicados usando um conjunto

print("Fim do cheat sheet!")
