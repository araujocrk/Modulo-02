class Veiculo:
    def __init__(self, chassi, marca, modelo, ano, placa=None, cor=None, proprietario=None, quilometragem=None):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        try:
            self.ano = int(ano)
        except ValueError:
            raise ValueError('Ano inválido. Tente Novamente!')
        if placa is not None:
            self.placa = placa
        else:
            self.placa = 'Não possui placa'
        if cor is not None:
            self.cor = cor
        else:
            self.cor = 'Não especificada'
        if proprietario is not None:
            self.proprietario = proprietario
        else:
            self.proprietario = 'Não especificado'
        if quilometragem is not None:
            try:
                self.quilometragem = int(quilometragem)
            except ValueError:
                raise ValueError('Quilometragem inválida. Tente Novamente!')
        else:
            self.quilometragem = 0

    def atualizarQuilometragem(self):
        #quilometragem = input('Digite a nova quilometragem: ')
        quilometragem = 15000
        try:
            self.quilometragem = int(quilometragem)
        except ValueError:
            print('Quilometragem inválida. Tente novamente.')
            return self.atualizarQuilometragem()
        
    def __str__(self):
        return f'Chassi: {self.chassi}\nMarca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nPlaca: {self.placa}\nCor: {self.cor}\nProprietário: {self.proprietario}\nQuilometragem: {self.quilometragem}'

def main():
    palio = Veiculo('1HGCM82633A123456', 'Fiat', 'Palio', 2010, cor='Vermelho')
    #palio = Veiculo(input('Chassi: '), input('Marca: '), input('Modelo: '), input('Ano: '), 
                    #input('Placa: ') or None, input('Cor: ') or None, input('Proprietário: ') or None,
                    #input('Quilometragem: ') or None)
    print(str(palio))
    celta = Veiculo('1HGCM82633A123458', 'Chevrolet', 'Celta', 2012, 'ABC-1234', 'Prata', 'João', 10000)
    #celta = Veiculo(input('Chassi: '), input('Marca: '), input('Modelo: '), input('Ano: '), 
                    #input('Placa: ') or None, input('Cor: ') or None, input('Proprietário: ') or None,
                    #input('Quilometragem: ') or None)
    celta.atualizarQuilometragem()
    print(str(celta))
    
if __name__ == '__main__':
    main()
