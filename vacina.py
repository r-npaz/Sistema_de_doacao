from enum import Enum


class VacinasNecessarias(Enum):
    raiva = 1
    leptospirose = 2
    hepatite_infecciosa = 3

class Vacina:
    def __init__(self, numero_chip: str, vacina_aplicada: int, data_aplicacao: str,):

        self.__numero_chip = None
        self.__vacina_aplicada = None
        self.__data_aplicacao = None
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip
        if isinstance(data_aplicacao, str):
            self.__data_aplicacao = data_aplicacao 
        if isinstance(vacina_aplicada, int):
            self.__vacina_aplicada = VacinasNecessarias(vacina_aplicada) if vacina_aplicada in VacinasNecessarias._value2member_map_ else None
 
    @property
    def numero_chip(self) -> str:
        return self.__numero_chip
    
    @numero_chip.setter
    def numero_chip(self, numero_chip: str):
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip
    
    @property
    def vacina_aplicada(self) -> VacinasNecessarias:
        return self.__vacina_aplicada
    
    @vacina_aplicada.setter
    def vacina_aplicada(self, vacina_aplicada: int):
        if isinstance(vacina_aplicada, int) and vacina_aplicada in VacinasNecessarias._value2member_map_:
            self.__vacina_aplicada = VacinasNecessarias(vacina_aplicada)

    @property
    def data_aplicacao(self) -> str:
        return self.__data_aplicacao
    
    @data_aplicacao.setter
    def data_aplicacao(self, data_aplicacao: str):
        if isinstance(data_aplicacao, str):
            self.__data_aplicacao = data_aplicacao
