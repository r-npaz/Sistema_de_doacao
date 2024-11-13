from datetime import datetime


class TelaInicial:

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
        print('10 -  Listar doações por período')
        print('11 -  Listar adoções por período')
        print('0  -  Sair')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        return opcao

    def tela_vacinar(self) -> list:
        print('Hora de vacinar')
        print('1  -  Vacina de Raiva')
        print('2  -  Vacina Leptospirose')
        print('3  -  Vacina de Hepatite Infecciosa')
        vacina = self.le_num_inteiro('Qual a vacina aplicada: ', [1, 2, 3])
        numero_chip = str(input('Qual a ID do animal: '))
        data_aplicacao = str(input('Qual a data de aplicação: '))
        return numero_chip, vacina, data_aplicacao

    def periodo(self) -> str:
        while True:
            try:
                data_inicio_str = input("Digite a data de início (dd/mm/yyyy): ")
                data_fim_str = input("Digite a data de fim (dd/mm/yyyy): ")
                data_inicio = datetime.strptime(data_inicio_str, "%d/%m/%Y")
                data_fim = datetime.strptime(data_fim_str, "%d/%m/%Y")
                if data_inicio > data_fim:
                    print("A data de início não pode ser posterior à data de fim. Tente novamente.")
                else:
                    print(f"Período selecionado: de {data_inicio.strftime('%d/%m/%Y')} até {data_fim.strftime('%d/%m/%Y')}")
                    return data_inicio, data_fim 
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato dd/mm/yyyy.")