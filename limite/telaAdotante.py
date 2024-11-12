import re

class TelaAdotante:

    def mostrar_tela_cadastro(self):
        print(f"{20 * '-'} {'CADASTRO ADOTANTE'}{20 * '-'}")
        print('Entre com os seus dados para cadastro: ')

        nome = self.le_nome()
        cpf = self.le_cpf()
        data_nascimento = self.le_data_nascimento()
        endereco = self.le_endereco()
        tem_animais = self.le_tem_animais()
        tipo_habitacao = self.tipo_habitacao()

        print('Cadastro completo!')
        print(f'{tipo_habitacao}, {tem_animais}, {nome}, {cpf}, {data_nascimento}, {endereco}')
        
        return [tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco]

    def le_nome(self):
        while True:
            nome = input('Nome: ').strip()
            if not nome:
                print("O nome não pode ser vazio. Tente novamente.")
            else:
                return nome

    def le_cpf(self):
        while True:
            cpf = input('Entre com o seu CPF: ').strip()
            if not self.validar_cpf(cpf):
                print("CPF inválido. Por favor, insira um CPF válido.")
            else:
                return cpf

    def le_data_nascimento(self):
        while True:
            data_nascimento = input('Entre com a sua data de nascimento (DD/MM/AAAA): ').strip()
            if not self.validar_data_nascimento(data_nascimento):
                print("Data inválida. Por favor, insira no formato DD/MM/AAAA.")
            else:
                return data_nascimento

    def le_endereco(self):
        while True:
            endereco = input('Entre com o seu endereço: ').strip()
            if not endereco:
                print("O endereço não pode ser vazio. Tente novamente.")
            else:
                return endereco

    def le_tem_animais(self):
        while True:
            tem_animais = input('Tem animais: S/N ').strip().upper()
            if tem_animais not in ['S', 'N']:
                print("Entrada inválida. Por favor, insira 'S' para sim ou 'N' para não.")
            else:
                return tem_animais

    def tipo_habitacao(self) -> int:
        print('1 - casa pequena')
        print('2 - casa grande')
        print('3 - apartamento pequeno')
        print('4 - apartamento grande')
        print('5 - outros')
        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5])

    def termo_adocao(self) -> bool:
        print('Está na hora de assinarmos o Termo de Adoção')
        cont = 0
        while cont < 3:
            try:
                termo = input('Você assina o termo de adoção? S/N: ').upper()
                if termo not in ['S', 'N']:
                    raise ValueError("Entrada inválida! Por favor, digite 'S' ou 'N'.")
                break
            except ValueError as e:
                print(e)
                cont += 1
        return termo == 'S'

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

    def validar_cpf(self, cpf: str) -> bool:
        return bool(re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf) or re.match(r'^\d{11}$', cpf))

    def validar_data_nascimento(self, data: str) -> bool:
        return bool(re.match(r'^\d{2}/\d{2}/\d{4}$', data))
