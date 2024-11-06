

class TelaGato:

    def cadastrar_gato(self) -> list:
        print('Cadastro do gato a ser doado')
        nome = str(input('Qual o nome do gato: '))
        raca = str(input('Qual a raça do gato: '))
        numero_chip = str(input('Qual o número do chip de identificação: '))
        vacina_aplicada = str(input('Quais vacinas o seu gato já recebeu: '))
        data_aplicacao = str(input('Quais as datas da aplicação das vacinas: '))
        return [numero_chip, nome, raca, vacina_aplicada, data_aplicacao]
