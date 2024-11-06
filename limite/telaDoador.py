

class TelaDoador:

    def mostrar_tela_cadastro(self):
        print(f"{20 * '-'} {'CADASTRO DOADOR'}{20 * '-'}")
        print('Entre com os seus dados para cadastro: ')
        nome = str(input('Nome: ')) #tenho que tratar essa entrada? Toda entrada é um strig por padrão no python! 
        cpf = str(input('Entre com o seu CPF: ')) #tenho que tratar essa entrada?
        data_nascimento = str(input('Entre com a sua data de nascimento: ')) #tenho que tratar essa entrada?
        endereco = str(input('Entre com o seu endereço: ')) #tenho que tratar essa entrada?
        return (nome, cpf, data_nascimento, endereco)
    