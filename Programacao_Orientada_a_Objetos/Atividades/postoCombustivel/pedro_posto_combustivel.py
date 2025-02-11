# Superclasse
class Combustivel:
    def __init__(self, nome, preco_por_litro):
        self.nome = nome
        if isinstance(preco_por_litro, (float, int)):
            if preco_por_litro > 0:
                self.preco_por_litro = preco_por_litro
            else:
                raise ValueError('Preço por litro deve ser maior que zero.')
        else:
            raise TypeError('Preço por litro deve ser um float ou inteiro.')

    def calcular_valor(self, qtd_litros):
        raise NotImplementedError('Método não implementado na superclasse')
    
# Subclasse
class Gasolina(Combustivel):
    def __init__(self, preco_por_litro, aditivada):
        # Reusa o construtor da superclasse 
        super().__init__('Gasolina', preco_por_litro)
        # Recebe sim ou não e transforma em True ou False
        if aditivada.lower() == 'sim':
            self.aditivada = True
        elif aditivada.lower() == 'não':
            self.aditivada = False
        else:
            raise ValueError('Aditivada deve ser "sim" ou "não".')

    # Recebe quantidade de litros
    def calcular_valor(self, qtd_litros):
        # Retorna o valor total do abastecimento
        return qtd_litros * self.preco_por_litro

class Etanol(Combustivel):
    def __init__(self, preco_por_litro, origem):
        # Reusa o construtor da superclasse 
        super().__init__('Etanol', preco_por_litro)
        # Lista de origens do etanol do posto
        self.lista_origem = ['cana_de_açucar', 'milho']
        # Recebe origem do etanol e verifica se existe na lista de origens
        self.origem = origem

class BombaDeCombustivel:
    def __init__(self, identificador):
        self.identificador = identificador
        self.combustivel = None

    def associar_combustivel(self, combustivel):
        self.combustivel = combustivel

    def abastecer(self, qtd_litros):
        if self.combustivel is None:
            raise ValueError("Bomba sem combustível associado.")
        total_pagar = self.combustivel.calcular_valor(qtd_litros)
        return Abastecimento(self, qtd_litros, total_pagar)

class Abastecimento:
    def __init__(self, bomba, qtd_litros, valor_total):
        self.bomba = bomba
        self.qtd_litros = qtd_litros
        self.valor_total = valor_total

    def __str__(self):
        tipo_combustivel = type(self.bomba.combustivel).__name__
        detalhes = "Aditivada" if isinstance(self.bomba.combustivel, Gasolina) and self.bomba.combustivel.aditivada else self.bomba.combustivel.origem
        return f"Bomba {self.bomba.identificador} ({tipo_combustivel} - {detalhes}): {self.qtd_litros} litros -> R$ {self.valor_total:.2f}"

class PostoDeCombustivel:
    def __init__(self, nome):
        self.nome = nome
        self.bombas = []
    # Adiciona boma de combustivel
    def adicionar_bomba(self, bomba):
        # Recebe bomba e verifica se ela é do tipo BombaDeCombustivel
        self.bombas.append(bomba)

    def listar_bombas(self):
        return [f"Bomba {b.identificador}" for b in self.bombas]
