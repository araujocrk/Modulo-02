from datetime import date
class CarteiraDeHabilitacao:
    def __init__(self, nome, orgaoEmissor, cpf, dataNascimento, pai, mae, permissao, acc, categoria, numeroRegistro, validade, primeiraCNH, local, dataEmissao, assinaturaPortador, assinaturaEmissor, observacoes=None):
        if len(nome) < 40:
            self.nome = nome
        else:
            print('Quantidade inválida. Tente abreviar seu Nome')
        self.orgaoEmissor = orgaoEmissor
        if len(cpf) == 11:
            self.cpf = cpf
        else:
            print('Quantidade inválida. Digite apenas os 11 números do CPF')

        self.dataNascimento = dataNascimento
        self.filiacao = pai, mae
        self.permissao = permissao
        self.acc = acc
        self.categoria = categoria if categoria in ['A', 'B', 'C', 'D', 'E', 'AB', 'AC', 'AD', 'AE'] else raise ValueError('Categoria Inválida')
        #Expressão ternária não funciona raise
        self.numeroRegistro = numeroRegistro
        self.validade = validade
        self.primeiraCNH = primeiraCNH
        self.local = local
        self.dataEmissao = dataEmissao
        self.assinaturaPortador = assinaturaPortador
        self.assinaturaEmissor = assinaturaEmissor
        self.observacoes = observacoes

def main():
    ryanCNH = CarteiraDeHabilitacao('Ryan da Silva Araújo', 'Detran', '12345678912', '02042004', 'Francisco', 'Francinete', 'PERMISSÃO', 'Sim', 'B', '32165498721', '13112030', '13112024', 'Detran', '13112024', 'Ryan da Silva Araújo', 'José Freitas Soares')

if __name__ == '__main__':
    main()
