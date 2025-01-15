class Pet:
  def __init__(self,tipo, raca, cor, nome='desconhecido', idade='desconhecida', peso='desconhecido', castrado='não'):
    self.__tipo = tipo
    self.__raca = raca
    self.__cor = cor
    if nome == 'desconhecido':
      self.__nome = 'Desconhecido'
    else:
      self.__nome = nome
    if idade == 'desconhecida':
      self.__idade = 'Desconhecida'
    else:
      self.__idade = idade
    if peso == 'desconhecido':
      self.__peso = 'Desconhecido'
    else:
      self.__peso = peso
    if castrado == 's':
      self.__castrado = 'Sim'
    else:
      self.__castrado = 'Não'
  
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
  
  def __str__(self):
    return f'Tipo: {self.__tipo}\nNome: {self.__nome}\nIdade: {self.__idade}\nPeso: {self.__peso}\nRaca: {self.__raca}\nCor: {self.__cor}\nCastrado: {self.__castrado}\n'

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
  
  def cadastrar_pet(self,pet):
    if type(pet) == Pet:
      self.__meus_pets.append(pet)
    else:
      print('Erro: Você não está cadastrando um pet.')

  def excluir_pet(self, pet):
    if type(pet) == Pet:
      for p in self.__meus_pets:
        if p._Pet__nome == pet._Pet__nome:
          self.__meus_pets.remove(p)
          print('Pet excluido com sucesso.')
          return
      print('Pet não encontrado.')
    else:
      print('Erro: Você não está excluindo um pet.')

  def mostrar_meus_pets(self):
    for pet in self.__meus_pets:
      print(pet)
  
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
    return f'Nome: {self.__nome}\nCpf: {self.__cpf}\nEndereço: {self.__endereco}\nPets: {len(self.__meus_pets)}\n'
  
def criarPessoa():
  nome = input('Nome: ')
  cpf = input('Cpf: ')
  endereco = input('Endereço: ')
  return nome, cpf, endereco

def criarPet():
  tipo = input('Qual o tipo do pet*: ')
  raca = input('Qual a raça do pet*: ')
  cor = input('Qual a cor do pet*: ')
  nome = input('Qual o nome do pet(ou deixe em branco): ') or 'desconhecido'
  idade = input('Qual a idade do pet em anos(ou deixe em branco): ') or 'desconhecida'
  peso = input('Qual o peso do pet em kg(ou deixe em branco): ') or 'desconhecido'
  castrado = input('O pet é castrado(Sim ou Não): ').lower()[0] or 'n'

def main():
  #arthur = Pessoa(*criarPessoa())
  arthur = Pessoa('Arthur', '12345678911', 'Armadillo')
  #tom = Pet(*criarPet())
  prince = Pet('Cavalo', 'Prince', 'Marrom', 'Prince', 10, 90, 'Não')
  arthur.cadastrar_pet(prince)
  penny = Pet('Cachorro', 'Cocker Spaniel', 'Castanho', 'Penny')
  arthur.cadastrar_pet(arthur)
  arthur.excluir_pet(prince)
  arthur.cadastrar_pet(penny)
  print(arthur)
  arthur.mostrar_meus_pets()
  
if __name__ == '__main__':
  main()
