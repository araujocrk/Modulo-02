from datetime import *
class CarteiraDeHabilitacao:
    def __init__(self, nome, orgaoEmissor, cpf, dataNascimento, pai, mae, permissao, acc, categoria, numeroRegistro, validade, primeiraCNH, local, dataEmissao, assinaturaPortador, assinaturaEmissor, observacoes='SEM OBSERVAÇÃO;'):
        
        self.nome = nome
        self.orgaoEmissor = orgaoEmissor
        if len(cpf) == 11:
            self.cpf = cpf
        else:
            raise Exception('Quantidade inválida. Digite apenas os 11 números do CPF')
        self.dataNascimento = self.validarData(dataNascimento)
        self.filiacao = pai, mae
        self.permissao = permissao
        self.acc = acc
        if categoria in ['A', 'B', 'C', 'D', 'E', 'AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']:
            self.categoria = categoria
        else:
            raise ValueError('Categoria inválida! Informe uma categoria válida.')
        if len(numeroRegistro) == 11:
            self.numeroRegistro = numeroRegistro
        else:
            raise Exception('Quantidade inválida. Digite apenas os 11 números do Registro')
        self.validade = self.validarData(self.validarValidade(validade, dataEmissao))
        self.primeiraCNH = self.validarData(primeiraCNH)
        self.local = local
        self.dataEmissao = self.validarData(dataEmissao)
        self.assinaturaPortador = assinaturaPortador
        self.assinaturaEmissor = assinaturaEmissor
        self.observacoes = observacoes
        
    def validarData(self, dataStr):
        try:
            dia = int(dataStr[:2])
            mes = int(dataStr[2:4])
            ano = int(dataStr[4:])
            dataInt = date(ano, mes, dia)
            if dataInt:
                return dataInt.strftime(""'%d/%m/%Y')
        except ValueError:
            raise ValueError('Data inválida! Digite uma data existente.')
    
    def validarValidade(self, validade, dataEmissao):
        if validade > dataEmissao:
            return validade
        else:
            raise ValueError('Data inválida! A data de validade deve ser maior que a data de emissão.')
    
    def __str__(self):
        return (f'Nome: {self.nome}\nOrgão Emissor: {self.orgaoEmissor}\nCPF: {self.cpf}\nData de Nascimento: {self.dataNascimento}\nFiliação: {self.filiacao[0]} / {self.filiacao[1]}\nPermissão: {self.permissao}\nACC: {self.acc}\nCategoria: {self.categoria}\nNº do Registro: {self.numeroRegistro}\nValidade: {self.validade}\n1ª Habilitação: {self.primeiraCNH}\nObservações: {self.observacoes}\nAssinatura do Portador: {self.assinaturaPortador}\nLocal: {self.local}\nData de Emissão: {self.dataEmissao}\nAssinatura do Emissor: {self.assinaturaEmissor}')

def main():
    ryanCNH = CarteiraDeHabilitacao('Ryan da Silva Araújo', 'Detran', '12345678912', '02042004', 'Francisco', 'Francinete', 'PERMISSÃO', 'Sim', 'B', '32165498721', '13112030', '13112024', 'Detran', '13112024', 'Ryan da Silva Araújo', 'José Freitas Soares')
    print(ryanCNH)
    
if __name__ == '__main__':
    main()
