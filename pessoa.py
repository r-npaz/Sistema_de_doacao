from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(data_nascimento, str):
            self.__data_nascimento = data_nascimento
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def data_nascimento(self) -> str:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        if isinstance(data_nascimento, str):
            self.__data_nascimento = data_nascimento

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        if isinstance(endereco, str):
            self.__endereco = endereco