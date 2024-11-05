

class Vacina:
    def __init__(self, numero_chip: str, vacina_aplicada: str, data_aplicacao: str,):

        self.__numero_chip = None
        self.__vacina_aplicada = None
        self.__data_aplicacao = None
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip
        if isinstance(vacina_aplicada, str):
            self.__vacina_aplicada = vacina_aplicada
        if isinstance(data_aplicacao, str):
            self.__data_aplicacao = data_aplicacao   
 