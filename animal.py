from abc import ABC, abstractmethod
from vacina import Vacina


class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: str, nome: str, raca: str, vacina_aplicada: str = "", data_aplicacao: str = ""):
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None
        self.__vacina_aplicada = None
        self.__data_aplicacao = None
        self.__historico_vacinas = []
        if isinstance(numero_chip, str):
            self.__numero_chip = numero_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca
        if isinstance(vacina_aplicada, str) and isinstance(data_aplicacao, str):
            self.__aplicar_vacina = Vacina(self.__numero_chip, self.__vacina_aplicada, self.__data_aplicacao)
            self.__historico_vacinas.append(self.__aplicar_vacina)

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
    
    def aplicar_vacina(self, numero_chip: str, vacina_aplicada: str, data_aplicacao: str):
        if isinstance(numero_chip, str):
            if isinstance(vacina_aplicada, str):
                if isinstance(data_aplicacao, str):
                    self.__aplicar_vacina = Vacina(numero_chip, vacina_aplicada, data_aplicacao)
                    self.__historico_vacinas.append(self.__aplicar_vacina)
                    return True
        return False
    
    @property
    def historico_vacinas(self, numero_chip: str) -> list:
        his_vacinas = []
        for vacina in self.__historico_vacinas:
            if vacina.numero_chip == numero_chip:
                his_vacinas.append(vacina)
            return his_vacinas
