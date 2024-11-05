from controleMovimentacao import ControleMovimentacao


class TelaInicial:
    
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
    
    def mostra_tela_opcoes(self):
        print(f"{20 * '-'} {'SISTEMA DE ADOÇÃO/DOAÇÃO'}{20 * '-'}")
        print('Escolha uma opção: ')
        print('1  -  Efetuar Cadastro')
        print('2  -  Doar')
        print('3  -  Adotar')
        print('4  -  Adicionar animal')
        print('5  -  Listar Adotantes')
        print('6  -  Listar Doadores')
        print('7  -  Listar animais disponíveis')
        print('8  -  Listar animais adotados')
        print('9  -  Vacinar animal')
        print('0  -  Sair')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        return opcao
    
    def tela_vacinar(self) -> list:
        print('Hora de vacinar')
        numero_chip = str(input('Qual a ID do animal: '))
        vacina = int(input('Qual a vacina aplicada: ')) #tratar essa entrada do usuário
        data_aplicacao = str(input('Qual a data de aplicação: '))
        return [numero_chip, vacina, data_aplicacao]
        