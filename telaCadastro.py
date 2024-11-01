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
        print('1  -  Adotar')
        print('2  -  Doar')
        opcao = self.le_num_inteiro('Escolha a opção: ', [1, 2])
        return opcao

