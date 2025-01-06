class Pessoa:
  def __init__(self,nome,idade,peso,altura,sexo,estado="viva",est_civil="solteira",mae=None):
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__altura = altura
    self.__sexo = sexo
    self.__estado = estado
    self.__est_civil = est_civil
    self.__mae = None
    self.__pai = None
    self.__mãe_adotiva = None
    self__pai_adotivo = None
    self.__conjuge = None
    self.filhos = []

  @property
  def nome(self):
    return self.__nome

  @property
  def conjuge(self):
    return self.__conjuge

  @property
  def est_civil(self):
    return self.__est_civil

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

  def casar(self,conjuge):
    # if (self.__est_civil == "solteira" or self.__est_civil == "divorciada" or self.__est_civil == "viúva"):
    #     if type(conjuge)==Pessoa:     
    #         if (conjuge.__est_civil == "solteira" or conjuge.__est_civil == "divorciada" or conjuge.__est_civil == "viúva"):
    #             self.est_civil = "casada"
    #             self.__conjuge = conjuge
    #             self.__conjuge.__est_civil = "casada"
    #             self.__conjuge.__conjuge = self
    #         else:
    #             print("Cônjuge já é casado!")
    #     else: 
    #         print("Cônjuge não é uma pessoa!")
    # else:
    #     print("Você já está casado.")

    if self.__est_civil == "casada":
        print("Você já está casado(a).")
    else:
        if type(conjuge)==Pessoa:
            if conjuge.__est_civil == "casada":
                print("Cônjuge já está casado(a).")
            else:
                self.est_civil = "casada"
                self.__conjuge = conjuge
                self.__conjuge.__est_civil = "casada"
                self.__conjuge.__conjuge = self
        else:
            print("Cônjuge não é uma pessoa!")
        

  def morrer(self):
    pass

  def divorciar(self):
    pass

  def ter_filhos(self,pessoa):
    if self.sexo == "F":
        if type(pessoa)==Pessoa:
            if pessoa.sexo == "M":
                filho = Pessoa(input("Digite o nome do filho(a): "),0,input("Digite o peso do filho(a): "),
                input("Digite a altura do filho(a): "), input("Digite o sexo do filho(a): "), mae = self, pai = pessoa)
                self.filhos.append(filho)
                pessoa.filhos.append(filho)
            else:
                print("Não é possível gerar filhos com essa pessoa.")
        else:
            print("Seu parceiro(a) não é uma pessoa!")
    elif self.sexo == "M":
        if type(pessoa)==Pessoa:
            if pessoa.sexo == "F":
                filho = Pessoa(input("Digite o nome do filho(a): "),0,input("Digite o peso do filho(a): "),
                input("Digite a altura do filho(a): "), input("Digite o sexo do filho(a): "), mae = pessoa, pai = self)
                self.filhos.append(filho)
                pessoa.filhos.append(filho)
            else:
                print("Não é possível gerar filhos com essa pessoa.")
        else:
            print("Seu parceiro(a) não é uma pessoa!")
    else:
        print("Você não pode ter filhos.")
        
  def adotar_filhos(self,criança): #condição: criança ser órfã.
    pass

  def __str__(self):
    pass


####### execução ########

maria = Pessoa("Maria",30,65,1.7,'F', Pessoa("Francisca",65,60,1.6,'F')) # maria -> solteira
joao = Pessoa(...) # joão -> solteiro
maria.casar(joao) # joão e maria -> casado
ana = Pessoa(...)
pedro = joao.ter_filhos(ana)
joao.casar(ana) # não é possivel pois joão já é casado com maria
maria.morrer() # maria para para o estado de morto.
joao.casar(ana) # joao e ana -> casado
joao.ter_filhos(maria) # Erro! maria está morta.
julia = ana.ter_filhos(joao)

#simular processo de adoção