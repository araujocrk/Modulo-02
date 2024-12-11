"""
Este cheat sheet resume as principais operações e métodos utilizados com strings em Python.
"""

# 1. **Criação de Strings**
# Strings podem ser criadas com aspas simples, duplas ou triplas.

# Exemplo de string simples
s = 'Olá, Mundo!'

# Exemplo de string com aspas duplas
s2 = "Olá, Mundo!"

# Exemplo de string multilinha com aspas triplas
s3 = '''Esta é uma string
que ocupa várias linhas.'''

# 2. **Operações com Strings**
# Concatenando Strings
s1 = "Olá"
s2 = "Mundo"
s = s1 + " " + s2  # Resultado: 'Olá Mundo'

# Repetindo Strings
s = "Olá " * 3  # Resultado: 'Olá Olá Olá '

# Acessando Caracteres
s = "Python"
print(s[0])  # Saída: 'P'  # Acessando o primeiro caractere
print(s[-1])  # Saída: 'n'  # Acessando o último caractere

# Fatiamento de Strings
s = "Python"
print(s[0:3])  # Saída: 'Pyt'  # Fatiando de 0 até 3
print(s[::2])   # Saída: 'Pto'  # Pegando caracteres alternados
print(s[::-1])  # Saída: 'nohtyP'  # Revertendo a string

# 3. **Métodos Comuns para Strings**

# Convertendo para minúsculas e maiúsculas
s = "Olá Mundo!"
print(s.lower())  # Saída: 'olá mundo!'
print(s.upper())  # Saída: 'OLÁ MUNDO!'

# Capitalizando a primeira letra
s = "olá mundo"
print(s.capitalize())  # Saída: 'Olá mundo'

# Convertendo para título (primeira letra de cada palavra em maiúscula)
s = "olá mundo de python"
print(s.title())  # Saída: 'Olá Mundo De Python'

# Removendo espaços extras
s = "   Olá Mundo!   "
print(s.strip())  # Saída: 'Olá Mundo!'

# Removendo espaços à esquerda ou à direita
s = "   Olá Mundo!   "
print(s.lstrip())  # Saída: 'Olá Mundo!   '
print(s.rstrip())  # Saída: '   Olá Mundo!'

# Substituindo partes da string
s = "Olá Mundo!"
print(s.replace("Mundo", "Python"))  # Saída: 'Olá Python!'

# Dividindo uma string
s = "Python, Java, C++"
print(s.split(", "))  # Saída: ['Python', 'Java', 'C++']

# Contando ocorrências de um caractere ou substring
s = "banana"
print(s.count("a"))  # Saída: 3

# Verificando se uma string começa ou termina com uma substring
s = "Python"
print(s.startswith("Py"))  # Saída: True
print(s.endswith("on"))    # Saída: True

# Encontrando a posição de uma substring
s = "Python"
print(s.find("th"))  # Saída: 2  # Retorna o índice da substring, ou -1 se não encontrar

# 4. **Formatação de Strings**

# Usando f-strings (Python 3.6+)
nome = "Hiromi"
idade = 25
s = f"Meu nome é {nome} e eu tenho {idade} anos."
print(s)  # Saída: 'Meu nome é Hiromi e eu tenho 25 anos.'

# Usando método format()
s = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(s)  # Saída: 'Meu nome é Hiromi e eu tenho 25 anos.'

# 5. **Outros Métodos Importantes**

# Verificando se uma string contém apenas dígitos
s = "12345"
print(s.isdigit())  # Saída: True

# Verificando se uma string contém apenas letras
s = "Python"
print(s.isalpha())  # Saída: True

# Verificando se uma string contém apenas letras e números
s = "Python3"
print(s.isalnum())  # Saída: True

# Verificando se a string contém espaços
s = "Python é ótimo!"
print(s.isspace())  # Saída: False

# Convertendo para maiúsculas o primeiro caractere de cada palavra
s = "python é ótimo"
print(s.title())  # Saída: 'Python É Ótimo'

# 6. **Comparação de Strings**

# Comparando duas strings
s1 = "Python"
s2 = "python"
print(s1 == s2)  # Saída: False  # Diferença de maiúsculas/minúsculas

# Comparando sem levar em conta maiúsculas/minúsculas
print(s1.lower() == s2.lower())  # Saída: True

# 7. **Checando Caracteres**

# Verificando se um caractere está presente na string
s = "Python"
print("P" in s)  # Saída: True
print("p" in s)  # Saída: False

# Verificando se um caractere não está presente
print("z" not in s)  # Saída: True

# 8. **Join - Unindo Strings**
# Unindo uma lista de strings com um delimitador
palavras = ["Python", "é", "ótimo"]
s = " ".join(palavras)  # Resultado: 'Python é ótimo'
print(s)

# 9. **Raw Strings**
# Raw strings são usadas para evitar que caracteres de escape sejam interpretados
s = r"C:\Users\Nome\Desktop"  # Não interpreta \ como escape
print(s)  # Saída: C:\Users\Nome\Desktop

# 10. **Strings Multilinha**
# Usando aspas triplas para criar strings multilinha
s = """Esta é uma string
que ocupa várias linhas."""
print(s)

# Fim do Cheat Sheet
