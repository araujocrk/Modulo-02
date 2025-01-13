class Pet:
  def __init__(self,tipo,nome,idade,peso,raca,cor,castrado=False):
    self.__tipo = tipo
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__raca = raca
    self.__cor = cor
    self.__castrado = castrado
  
  @property
  def tipo(self):
    return self.__tipo
  @property
  def nome(self):
    return self.__nome
  @property
  def idade(self):
    return self.__idade
  @property
  def peso(self):
    return self.__peso
  @property
  def raca(self):
    return self.__raca
  @property
  def cor(self):
    return self.__cor
  @property
  def castrado(self):
    return self.__castrado

class Pessoa:
  def __init__(self,nome,cpf,endereco):
    self.__nome = nome
    if self.validarCpf(cpf):
      self.__cpf = cpf
    self.__endereco = endereco
    self.__meus_pets = []

  @property
  def nome(self):
    return self.__nome
  
  @property
  def cpf(self):
    return self.__cpf
  
  @property
  def endereco(self):
    return self.__endereco
  
  @property
  def meus_pets(self):
    return self.__meus_pets
  
  @meus_pets.setter
  def meus_pets(self, pet):
    if type(pet) == Pet:
      self.__meus_pets.append(pet)
    else:
      print('Erro: Você não está cadastrando um pet.')

  def cadastrar_pet(self,pet):
    self.__meus_pets = pet

  def excluir_pet(self,nome):
    pass

  def mostrar_meus_pets(self):
    pass
  
  def validarCpf(self, cpf):
    if len(cpf) == 11:
      try:
        int(cpf)
        return True
      except ValueError:
        raise ValueError('Erro: Cpf deve possuir apenas números')
    else:
      raise ValueError('Erro: Cpf deve possuir 11 números.')
    
  def __str__(self):
    return f'Nome: {self.__nome}\nCpf: {self.__cpf}\nEndereço: {self.__endereco}'
  
def criarPessoa():
  nome = input('Nome: ')
  cpf = input('Cpf: ')
  endereco = input('Endereço: ')
  return nome, cpf, endereco

def main():
  arthur = Pessoa(*criarPessoa())
  arthur.cadastrar_pet()
  
if __name__ == '__main__':
  main()