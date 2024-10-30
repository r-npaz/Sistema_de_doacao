from controleTelaInicial import ControleTelaInicial


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
        print('1  -  Doar')
        print('2  -  Adotar')
        print('3  -  Adicionar animal')
        print('4  -  Listar Adotantes')
        print('5  -  Listar Doadores')
        print('6  -  Listar animais disponíveis')
        print('7  -  Listar animais adotados')
        print('0  -  Sair')
        opcao = self.le_num_inteiro('Escolha a opção: ', [0, 1, 2, 3, 4, 5, 6, 7])
        return opcao