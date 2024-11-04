from controleMovimentacao import ControleMovimentacao


class TelaCadastro:

    def le_num_inteiro(self, mensagem: str = '', inteiros_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError ('Número não permitido')
                return inteiro
            except ValueError:
                print('Valor incorreto: Digite um valor numerico inteiro válido')
                if inteiros_validos:
                    print('Valores válidos: ', inteiros_validos)

    def opcao_cadastro(self):
        print('Escolha um das opções para realizar o seu cadastro')
        print('1  -  Adotar')
        print('2  -  Doar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [1, 2])
        return opcao
    
    def opcao_doar(self):
        print('Qual animal você quer doar?')
        print('1  -  Para doar um cachorro')
        print('2  -  Para doar um gato')
        opcao = self.le_num_inteiro('Escolha uma opção: ', [1, 2])
        return opcao
    
    def dados_doacao(self, data_doacao: str, motivo_doacao: str) -> list:
        print('Finalizando a doação')
        data_doacao = str(input('Entre com a data da doação: '))
        motivo_doacao = str(input('Entre com o motivo da doação: '))
        return (data_doacao, motivo_doacao)



