"""
Este cheat sheet resume as principais funcionalidades e práticas recomendadas para o tratamento de exceções em Python.
"""

# 1. **Estrutura Básica de Tratamento de Exceções**
# O Python usa `try`, `except`, `else`, e `finally` para capturar e tratar exceções.

try:
    # Código que pode gerar uma exceção
    x = 10 / 0  # Exceção de divisão por zero
except ZeroDivisionError:
    # Código para tratar a exceção
    print("Erro: Não é possível dividir por zero.")
else:
    # Código que será executado se não ocorrer nenhuma exceção
    print("Operação realizada com sucesso.")
finally:
    # Código que será sempre executado, independentemente de exceções
    print("Fim da execução.")

# 2. **Tipos de Exceções Comuns**

# Exemplo 1: Capturando uma exceção de divisão por zero
try:
    y = 10 / 0
except ZeroDivisionError as e:
    print(f"Erro: {e}")  # Saída: Erro: division by zero

# Exemplo 2: Capturando erro de tipo
try:
    valor = int("abc")  # Tentando converter uma string não numérica
except ValueError as e:
    print(f"Erro: {e}")  # Saída: Erro: invalid literal for int() with base 10: 'abc'

# Exemplo 3: Capturando erro de índice em listas
try:
    lista = [1, 2, 3]
    print(lista[5])  # Índice fora do intervalo
except IndexError as e:
    print(f"Erro: {e}")  # Saída: Erro: list index out of range

# 3. **Capturando Exceções Genéricas**
# É possível capturar qualquer tipo de exceção com a exceção genérica `Exception`.

try:
    num = 10 / 0
except Exception as e:  # Captura qualquer exceção
    print(f"Erro genérico: {e}")

# 4. **Usando `else` em Exceções**
# O bloco `else` é executado apenas quando não ocorre nenhuma exceção no `try`.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print(f"Resultado da divisão: {result}")  # Saída: Resultado da divisão: 5.0

# 5. **Usando `finally`**
# O bloco `finally` é executado independentemente de exceções, sendo útil para limpeza de recursos, como fechar arquivos ou conexões.

try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError as e:
    print(f"Erro: {e}")
finally:
    print("Tentativa de ler o arquivo concluída.")
    # O arquivo será fechado se aberto
    if 'arquivo' in locals():
        arquivo.close()

# 6. **Criando Exceções Personalizadas**
# Podemos criar nossas próprias exceções definindo uma classe que herda de `Exception`.

class MinhaExcecao(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise MinhaExcecao("Erro personalizado!")
except MinhaExcecao as e:
    print(f"Erro personalizado: {e}")  # Saída: Erro personalizado: Erro personalizado!

# 7. **Capturando múltiplas exceções**
# É possível capturar diferentes exceções em blocos separados ou no mesmo bloco `except`.

try:
    num = int("abc")
    result = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print(f"Erro: {e}")  # Saída: Erro: invalid literal for int() with base 10: 'abc'

# 8. **Usando `assert`**
# O `assert` é uma forma de verificar uma condição durante a execução e lançar uma exceção se a condição for falsa.

x = -1
assert x >= 0, "O valor de x não pode ser negativo!"  # Levanta uma exceção AssertionError se x for negativo

# 9. **Obtendo informações sobre a exceção**
# Podemos usar o módulo `traceback` para obter mais detalhes sobre a exceção.

import traceback

try:
    num = 10 / 0
except ZeroDivisionError as e:
    print("Detalhes da exceção:")
    traceback.print_exc()

# 10. **Usando exceções em contexto com `with`**
# Exceções podem ser usadas em conjunto com o `with` para garantir o tratamento adequado de recursos, como arquivos.

class MyFileHandler:
    def __enter__(self):
        print("Abrindo o arquivo...")
        return open("arquivo.txt", "r")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando o arquivo...")
        if exc_type:
            print(f"Ocorreu um erro: {exc_val}")
        return True  # Impede que a exceção seja propagada

with MyFileHandler() as file:
    conteúdo = file.read()
    print(conteúdo)

# 11. **Raising Exceções**
# Você pode lançar exceções manualmente com `raise`.

def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero!")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(f"Erro: {e}")  # Saída: Erro: O divisor não pode ser zero!

# Fim do Cheat Sheet
