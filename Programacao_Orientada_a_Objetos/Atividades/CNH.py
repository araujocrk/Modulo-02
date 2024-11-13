class CarteiraDeHabilitacao:
    def __init__ (self, nome, orgaoEmissor, cpf, dataNascimento, filiacao, permissao, acc, categoria, numeroRegistro, validade, primeiraCNH, local, dataEmissao, assinaturaPortador, assinaturaEmissor, observacoes=None):
        self.nome = nome
        self.orgaoEmissor = orgaoEmissor
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.filiacao = filiacao
        self.permissao = permissao
        self.acc = acc
        self.categoria = categoria
        self.numeroRegistro = numeroRegistro
        self.validade = validade
        self.primeiraCNH = primeiraCNH
        self.local = local
        self.dataEmissao = dataEmissao
        self.assinaturaPortador = assinaturaPortador
        self.assinaturaEmissor = assinaturaEmissor
        self.observacoes = observacoes

def main():
    ryanCNH = CarteiraDeHabilitacao(
        input('Nome: '), input('Orgão Emissor: '), input('CPF (somente numeros): '), input('Data de Nascimento ddmmaaaa: '), 
        input('Nome do pai: '), input('Nome da mãe: '), input('Permissão: '), input('ACC: '), 
        input('Categoria: '), input('Número de Registro: '), input('Validade: '), input('Data da primeira CNH: '),
        input('Local: '), input('Data de Emissão: '),
        input('Assinatura do Portador: '), input('Assinatura do Emissor: '),
        input('Observações: ') or None
    )
if __name__ == '__main__':
    main()
