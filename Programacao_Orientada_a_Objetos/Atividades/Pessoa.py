class Pessoa:
  contadorId = 0 
  def __init__(self,nome,idade,peso,altura,sexo,estado="viva",est_civil="solteira",mae=None, pai=None):
    self.__id = Pessoa.contadorId
    Pessoa.contadorId += 1
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__altura = altura
    self.__sexo = sexo
    self.__estado = estado
    self.__est_civil = est_civil
    self.__mae = mae
    self.__pai = pai
    self.__mae_adotiva = None
    self.__pai_adotivo = None
    self.__conjuge = None
    self.filhos = []

  @property
  def id(self):
    return self.__id
  
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
  def peso(self):
    return self.__peso
  
  @property
  def altura(self):
    return self.__altura

  @property
  def sexo(self):
    return self.__sexo
  
  @property
  def estado(self):
    return self.__estado
  
  @property
  def est_civil(self):
    return self.__est_civil
  
  @property
  def mae(self):
    return self.__mae
  
  @property
  def pai(self):
    return self.__pai
  
  @property
  def mae_adotiva(self):
    return self.__mae_adotiva
  
  @property
  def pai_adotivo(self):
    return self.__pai_adotivo
  
  @property
  def conjuge(self):
    return self.__conjuge

  @nome.setter
  def nome(self,valor):
    if self.__est_civil == "casado":
      nome_antigo = self.__nome.split(" ")
      nome_conjuge = self.__conjuge.nome.split(" ")
      novo_nome = valor.split(" ")
      for i in novo_nome:
        if (i not in nome_antigo) and (i not in nome_conjuge):
           print("nome inválido!")
           return
      self.__nome = valor
      print ("Alteração efetuada com sucesso!")
      
  @mae_adotiva.setter
  def mae_adotiva(self, mae):
    if type(mae) == Pessoa:
      self.__mae_adotiva = mae
    else:
      print("Erro: Mãe adotiva não é uma Pessoa")
      
  @pai_adotivo.setter
  def pai_adotivo(self, pai):
    if type(pai) == Pessoa:
      self.__pai_adotivo = pai
    else:
      print("Erro: Pai adotivo não é uma Pessoa")

  # Validar que uma Pessoa não pode se casar com ela mesma
  def casar(self,conjuge):
    if self.__est_civil != "casada":
      if type(conjuge) == Pessoa:
        if self.__id != conjuge.__id:
          if conjuge.__est_civil != "casada":
            self.__est_civil = "casada"
            self.__conjuge = conjuge
            self.__conjuge.__est_civil = "casada"
            self.__conjuge.__conjuge = self
          else:
            print("Cônjuge já está casado(a).")
        else:
          print("Você não pode casar consigo mesmo.")
      else:
        print("Cônjuge não é uma pessoa!")
    else:
       print("Você já está casado(a).")
        
  #Alterar o estado / verificar se a pessoa que morreu era casada e alterar o conjuge para viuvo
  def morrer(self):
    if self.__estado == "viva":
      self.__estado = "morta"
      if type(self.__conjuge) == Pessoa:
        if self.__conjuge.__sexo == "F":
          self.__conjuge.__est_civil = "viúva"
        elif self.__conjuge.__sexo == "M":
          self.__conjuge.__est_civil = "viúvo"
      self.__conjuge.__conjuge = None
      self.__conjuge = None
    else:
      print("Erro: Essa pessoa já faleceu.")
      
  #Mudar o estado civil das pessoas para "divorciado"
  def divorciar(self):
    if type(self.__conjuge) == Pessoa:
      self.__conjuge.__est_civil = "divorciada"
      self.__conjuge.__conjuge = None
      self.__conjuge = None
      self.__est_civil = "divorciada"
    else:
      print("Você não possui um cônjuge.")

  # Adicionar condição para que não possa ter filho com uma pessoa falecida
  def ter_filhos(self,pessoa):
    if self.sexo == "F":
        if type(pessoa)==Pessoa:
            if pessoa.sexo == "M":
              if pessoa.__estado == "viva":
                  filho = Pessoa(input("Digite o nome do filho(a): "),0,input("Digite o peso do filho(a): "),
                  input("Digite a altura do filho(a): "), input("Digite o sexo do filho(a): "), mae = self, pai = pessoa)
                  self.filhos.append(filho)
                  pessoa.filhos.append(filho)
              else:
                print("Essa pessoa já faleceu.")
            else:
                print("Não é possível gerar filhos com essa pessoa.")
        else:
            print("Seu parceiro(a) não é uma pessoa!")
    elif self.sexo == "M":
        if type(pessoa)==Pessoa:
            if pessoa.sexo == "F":
              if pessoa.__estado == "viva":
                  filho = Pessoa(input("Digite o nome do filho(a): "),0,input("Digite o peso do filho(a): "),
                  input("Digite a altura do filho(a): "), input("Digite o sexo do filho(a): "), mae = pessoa, pai = self)
                  self.filhos.append(filho)
                  pessoa.filhos.append(filho)
                  return filho
              else:
                print("Essa pessoa já faleceu.")
            else:
                print("Não é possível gerar filhos com essa pessoa.")
        else:
            print("Seu parceiro(a) não é uma pessoa!")
    else:
        print("Você não pode ter filhos.")
        
  def adotar_filhos(self,crianca): #condição: criança ser órfã.
    if crianca.__id != self.__id:
      if crianca.__mae is None and crianca.__pai is None:
        self.filhos.append(crianca)
        if self.__sexo == "F":
          crianca.__mae_adotiva = self
        elif self.__sexo == "M":
          crianca.__pai_adotivo = self
      else:
        print("Essa criança possui pais.")
    else:
      print("Você não pode se adotar!")

  def __str__(self):
    sexo = ""
    if self.__sexo == "F":
      sexo = "Feminino"
    elif self.__sexo == "M":
      sexo = "Masculino"
    
    mae = ""
    pai = ""
    conjuge = ""
    if type(self.__mae) == Pessoa:
      mae = f"Mãe: {self.__mae.__nome}"
    elif type(self.__mae_adotiva) == Pessoa:
      mae = f"Mãe adotiva: {self.__mae_adotiva.__nome}"
    else:
      mae = "Mãe: Não informada"
      
    if type(self.__pai) == Pessoa:
      pai = f"Pai: {self.__pai.__nome}"
    elif type(self.__pai_adotivo) == Pessoa:
      pai = f"Pai adotivo: {self.__pai_adotivo.__nome}"
    else:
      pai = "Pai: Não informado"
      
    if self.__conjuge is None:
      conjuge = f"Não possui"
    else:
      conjuge = f"{self.__conjuge.__nome}"
      
    return (
            f"""
Identificador: {self.__id}
Nome: {self.__nome}
Idade: {self.__idade} anos
Altura: {self.__altura} m
Peso: {self.__peso} kg
Sexo: {sexo}
Estado: {self.__estado}
Estado civil: {self.__est_civil}
{mae}
{pai}
Cônjuge: {conjuge}
Filhos: {len(self.filhos)}"""
            )

####### execução ########
def main():
  maria = Pessoa("Maria",30,65,1.7,'F', mae = Pessoa("Francisca",65,60,1.6,'F'))
  joao = Pessoa("João",35,75,1.8,"M")
  joao.casar(maria)
  print(maria)
  print(joao)
  ana = Pessoa("Ana",25,65,1.75,"F")
  pedro = joao.ter_filhos(ana)
  joao.casar(ana)
  maria.morrer()
  joao.casar(ana)
  cassio = joao.ter_filhos(maria)
  print(maria)
  print(joao)
  print(pedro)
  print(ana)
  
  alan = Pessoa("Alan", 18, 73, 1.78, "M")
  sabrina = Pessoa("Sabrina", 30, 65, 1.7, "F")
  alexandre = Pessoa("Alexandre", 5, 35, 0.95, "M")
  alan.casar(sabrina)
  print(alan)
  print(sabrina)
  alan.divorciar()
  alan.adotar_filhos(alexandre)
  print(sabrina)
  print(alan)
  print(alexandre)
  
if __name__ == "__main__":
  main()
