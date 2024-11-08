from abc import ABC, abstractmethod
from entidade.vacina import Vacina


class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: str, nome: str, raca: str, vacina_aplicada: str = "", data_aplicacao: str = ""):
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None
        self.__vacina_aplicada = None
        self.__data_aplicacao = None
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca
        if isinstance(vacina_aplicada, str):
            self.__vacina_aplicada = vacina_aplicada
        if isinstance(data_aplicacao, str):
            self.__data_aplicacao = data_aplicacao

    @property
    def numero_chip(self) -> str:
        return self.__numero_chip

    @numero_chip.setter
    def numero_chip(self, numero_chip: str):
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    def aplicar_vacina(self, numero_chip: str, vacina_aplicada: int, data_aplicacao: str):
        if isinstance(numero_chip, str):
            if isinstance(vacina_aplicada, int):
                if isinstance(data_aplicacao, str):
                    vacina = Vacina(numero_chip, vacina_aplicada, data_aplicacao)
                    return vacina
        return False
