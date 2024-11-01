from controleAdotante import ControleAdotante


class TelaDoador:

    def mostrar_tela_cadastro(self):
        print(f"{20 * '-'} {'CADASTRO DOADOR'}{20 * '-'}")
        print('Entre com os seus dados para cadastro: ')
        nome = str(input('Nome: ')) #tenho que tratar essa entrada
        cpf = str(input('Entre com o seu CPF: ')) #tenho que tratar essa entrada
        data_nascimento = str(input('Entre com a sua data de nascimento: ')) #tenho que tratar essa entrada
        endereco = str(input('Entre com o seu endereço: ')) #tenho que tratar essa entrada
        return (nome, cpf, data_nascimento, endereco)

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
