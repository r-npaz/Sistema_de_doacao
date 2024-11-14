from entidade.animal import Animal


class Gato(Animal):
    def __init__(self, numero_chip: str, nome: str, raca: str, vacina_aplicada: int = "", data_aplicacao: str = ""):
        super().__init__(numero_chip, nome, raca, vacina_aplicada, data_aplicacao)

    def aplicar_vacina(self, vacina_aplicada: str, data_aplicacao: str):
        vacina = (self, vacina_aplicada, data_aplicacao)  # A vacina agora "sabe" qual gato a recebeu
        return vacina