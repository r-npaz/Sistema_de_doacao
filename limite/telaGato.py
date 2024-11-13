

class TelaGato:

    def cadastrar_gato(self) -> list:
        print('Cadastro do gato a ser doado')
        nome = str(input('Qual o nome do gato: '))
        raca = str(input('Qual a raça do gato: '))
        numero_chip = str(input('Qual o número do chip de identificação: '))
        vacinas = self.vacina()
        return numero_chip, nome, raca, vacinas
    
    def vacina (self) -> list:
        vacinas = []
        while True:
            print('Quais as vacinas que seu animal já tomou?')
            print('1  -  Vacina de Raiva')
            print('2  -  Vacina Leptospirose')
            print('3  -  Vacina de Hepatite Infecciosa')
            print('0  -  Nenhuma')
            vacina = self.le_num_inteiro('Qual a vacina aplicada: ', [1, 2, 3, 0])
            if vacina == 0:
                return vacinas
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
                    raise ValueError('Número não permitido')
                return inteiro
            except ValueError:
                print('Valor incorreto: Digite um valor numérico inteiro válido')
                if inteiros_validos:
                    print('Valores válidos: ', inteiros_validos)