from controle.controleCachorro import ControleCachorro


class TelaCachorro:

    def cadastrar_cachorro(self) -> list:
        print('Cadastro do cachorro a ser doado')
        nome = str(input('Qual o nome do cachorro: '))
        raca = str(input('Qual a raça do cachorro: '))
        porte = self.porte_cachorro
        numero_chip = str(input('Qual o número do chip de identificação: '))
        vacina_aplicada = str(input('Quais vacinas o seu cachorro já recebeu: '))
        data_aplicacao = str(input('Quais as datas da aplicação das vacinas: '))
        return [porte, numero_chip, nome, raca, vacina_aplicada, data_aplicacao]

    def porte_cachorro(self) -> int:
        print('Qual o porte do cachorro?')
        print('1  -  pequeno')
        print('2  -  médio')
        print('3  -  grande')
        opcao = self.le_num_inteiro(input('Entre com o número que representa o tamanho do seu cachorro: '), [1, 2, 3])
        return opcao

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

