class Veiculo:
    def __init__(self, placa, marca, modelo, ano, cor=None, proprietario=None, quilometragem=None):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor if cor is not None else 'Não especificada'
        self.proprietario = proprietario if proprietario is not None else 'Não especificado'
        self.quilometragem = quilometragem if quilometragem is not None else 0

    def atualizarQuilometragem(self):
        try:
            quilometragem = int(input('Qual a nova quilometragem? '))
            if quilometragem >= 0:
                self.quilometragem = quilometragem
            else:
                print('Quilometragem inválida. Tente novamente.')
                return self.atualizarQuilometragem()
        except ValueError:
            print('Quilometragem inválida. Tente novamente.')
            return self.atualizarQuilometragem()
        
    def __str__(self):
        return f'Placa: {self.placa}\nMarca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\nProprietário: {self.proprietario}\nQuilometragem: {self.quilometragem}'

def main():    
    palio = Veiculo('ABC-1234', 'Fiat', 'Palio', 2010, quilometragem=10000)
    # palio = Veiculo(input('Placa: '), input('Marca: '), input('Modelo: '), int(input('Ano: ')), input('Cor: ') or None,
    #                 input('Proprietário: ') or None, input('Quilometragem: ') or None)
    print(str(palio))
    celta = Veiculo('DEF-1234', 'Chevrolet', 'Celta', 2015, 'Branco', 'Maria', 50000)
    # celta = Veiculo(input('Placa: '), input('Marca: '), input('Modelo: '), int(input('Ano: ')), input('Cor: ') or None,
    #                 input('Proprietário: ') or None, input('Quilometragem: ') or None)
    celta.atualizarQuilometragem()
    print(str(celta))
    
if __name__ == '__main__':
    main()
