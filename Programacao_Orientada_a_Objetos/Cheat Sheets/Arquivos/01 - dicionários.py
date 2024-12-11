
"""
Este é um resumo dos métodos e funcionalidades mais comuns para trabalhar com dicionários em Python.
"""

# Criando um dicionário
meu_dict = {"chave1": "valor1", "chave2": "valor2"}

# Acessando valores
valor = meu_dict["chave1"]  # Acessa o valor da chave 'chave1'

# Adicionando ou atualizando itens
meu_dict["chave3"] = "novo_valor"  # Adiciona ou atualiza a chave 'chave3'

# Removendo itens
del meu_dict["chave2"]  # Remove a chave 'chave2' e seu valor
valor_removido = meu_dict.pop("chave3", "valor_padrão")  # Remove a chave 'chave3' e retorna seu valor (ou um valor padrão se não existir)

# Métodos úteis
meu_dict.clear()           # Remove todos os itens do dicionário
meu_dict.copy()            # Retorna uma cópia rasa do dicionário
len(meu_dict)              # Retorna o número de itens no dicionário
"chave1" in meu_dict       # Verifica se 'chave1' está no dicionário (retorna True ou False)
meu_dict.get("chave1", "valor_padrão")  # Retorna o valor de 'chave1' ou 'valor_padrão' se não existir

# Iterando sobre um dicionário
for chave in meu_dict:               # Itera sobre as chaves
    print(chave)

for valor in meu_dict.values():      # Itera sobre os valores
    print(valor)

for chave, valor in meu_dict.items():  # Itera sobre as chaves e valores
    print(chave, valor)

# Métodos específicos
meu_dict.keys()        # Retorna um objeto com todas as chaves do dicionário
meu_dict.values()      # Retorna um objeto com todos os valores do dicionário
meu_dict.items()       # Retorna um objeto com todos os pares (chave, valor)

# Atualizando dicionários
outro_dict = {"chave4": "valor4"}
meu_dict.update(outro_dict)  # Atualiza 'meu_dict' com os itens de 'outro_dict'

# Compreensão de dicionários
quadrados = {x: x**2 for x in range(5)}  # Exemplo: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Funções úteis
max_key = max(meu_dict)        # Retorna a maior chave (com base na ordem padrão)
min_key = min(meu_dict)        # Retorna a menor chave
sorted_keys = sorted(meu_dict)  # Retorna uma lista das chaves em ordem crescente

# Criando dicionários com valores padrão
novo_dict = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# Trabalhando com valores padrão ao inserir
from collections import defaultdict
meu_dict = defaultdict(int)  # Valores padrão serão inteiros (0)

# Exemplo de uso
meu_dict["nova_chave"] += 1   # Se 'nova_chave' não existir, será criada com valor 0 e incrementada para 1

# Dicionários imutáveis (a partir do Python 3.9)
from types import MappingProxyType
imutavel = MappingProxyType(meu_dict)  # Cria uma visão somente leitura de 'meu_dict'

print("Fim do cheat sheet!")
