from controleAdotante import ControleAdotante


class TelaAdotante:


    def mostrar_tela_cadastro(self):
        print(f"{20 * '-'} {'CADASTRO ADOTANTE'}{20 * '-'}")
        print('Entre com os seus dados para cadastro: ')
        nome = str(input('Nome: '))
        cpf = str(input('Entre com o seu CPF: '))
        data_nascimento = str(input('Entre com a sua data de nascimento: '))
        endereço = str(input('Entre com o seu endereço: '))
        tem_animais = str(input('Tem animais: S/N '))
        porte_habitacao = self.porte_habitacao()
    
    def porte_habitacao(self) -> int:
        print('1 - casa pequena')
        print('2 - casa grande')
        print('3 - apartamento pequeno')
        print('4 - apartamento grande')
        print('5 - outros')
        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5])
        return opcao
    
    def le_num_inteiro(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            