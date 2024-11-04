from pessoa import Pessoa
from enum import Enum
from datetime import datetime


class TipoHabitacao(Enum):
        casa_pequena = 1
        casa_grande = 2
        apartamento_pequeno = 3
        apartamento_grande = 4
        outro = 5

class Adotante(Pessoa):
    def __init__(self, tipo_habitacao: TipoHabitacao, tem_animais: bool, 
                 nome: str, cpf: str, data_nascimento: str, endereco: str,):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.__tipo_habitacao = None
        self.__tem_animais = None
        if isinstance(tipo_habitacao, TipoHabitacao):
            self.__tipo_habitacao = tipo_habitacao
        if isinstance(tem_animais, bool):
            self.__tem_animais = tem_animais
        self.__termo_responsabilidade = False
        self.__data_termo_assinado = None

    @property
    def tipo_habitacao(self) -> TipoHabitacao:
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao: TipoHabitacao):
        if isinstance(tipo_habitacao, TipoHabitacao):
            self.__tipo_habitacao = tipo_habitacao

    @property
    def tem_animais(self) -> bool:
        return self.__tem_animais

    @tem_animais.setter
    def tem_animais(self, tem_animais: bool):
        if isinstance(tem_animais, bool):
            self.__tem_animais = tem_animais

    @property
    def termo_responsabilidade(self) -> bool:
        return self.__termo_responsabilidade

    @termo_responsabilidade.setter
    def assinar_termo_responsabilidade(self):
        if self.__termo_responsabilidade != False:
            self.__termo_responsabilidade = True
            self.__data_termo_assinado = datetime.now()

    @property
    def data_assinatura(self) -> str:
        return self.__data_termo_assinado
