from abc import ABC, abstractmethod
from entidade.vacina import Vacina


class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: str, nome: str, raca: str, vacina_aplicada: str = "", data_aplicacao: str = ""):
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None
        self.__vacina = None
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca
        if vacina_aplicada and data_aplicacao:
            if isinstance(vacina_aplicada, str) and isinstance(data_aplicacao, str):
                self.__vacina = Vacina(numero_chip, vacina_aplicada, data_aplicacao)

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
    def vacina(self) -> Vacina:
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina: Vacina):
        if isinstance(vacina, Vacina):
            self.__vacina = vacina

    @property
    def raca(self):
        return self.__raca

    def aplicar_vacina(self, animal, vacina_aplicada: int, data_aplicacao: str):
        if isinstance(animal, Animal) and isinstance(vacina_aplicada, int) and isinstance(data_aplicacao, str):
            self.__vacina = Vacina(animal, vacina_aplicada, data_aplicacao)
            return self.__vacina
        return None
