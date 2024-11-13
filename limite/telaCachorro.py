

class TelaCachorro:

    def cadastrar_cachorro(self) -> list:
        print('Cadastro do cachorro a ser doado')
        nome = str(input('Qual o nome do cachorro: '))
        raca = str(input('Qual a raça do cachorro: '))
        porte = self.porte_cachorro()
        numero_chip = str(input('Qual o número do chip de identificação: '))
        vacinas = self.vacina()
        return porte, numero_chip, nome, raca, vacinas

    def porte_cachorro(self) -> int:
        print('Qual o porte do cachorro?')
        print('1  -  pequeno')
        print('2  -  médio')
        print('3  -  grande')
        opcao = self.le_num_inteiro(('Entre com o número que representa o tamanho do seu cachorro: '), [1, 2, 3])
        return opcao
    
    def vacina (self) -> list:
        vacinas = []
        while True:
            print('Quais as vacinas que seu animal já tomou?')
            print('1  -  Vacina de Raiva')
            print('2  -  Vacina Leptospirose')
            print('3  -  Vacina de Hepatite Infecciosa')
            vacina = self.le_num_inteiro('Qual a vacina aplicada: ', [1, 2, 3])
            data_aplicacao = str(input('Qual a data de aplicação: '))
            vacinas.append((vacina, data_aplicacao))
            continuar = input('Continuar cadastrando vacina? S/N: ').upper()
            if continuar == 'N':
                break

            elif continuar != 'S':
                print('Valor incorreto: Digite S ou N')

        return vacinas

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
