from entidade.animal import Animal


class Gato(Animal):
    def __init__(self, numero_chip: str, nome: str, raca: str, vacina_aplicada: str, data_aplicacao: str):
        super().__init__(numero_chip, nome, raca, vacina_aplicada, data_aplicacao)
