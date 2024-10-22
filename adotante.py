from pessoa import Pessoa


class Adotante(Pessoa):
    def __init__(self, tipo_habitacao: str, porte_habitacao: str, tem_animais: bool):
        super().__init__(nome, cpf, data_nascimento, endereco)
        if isinstance(tipo_habitacao, str):
            self.__tipo_habitacao = tipo_habitacao
        if isinstance(porte_habitacao, str):
            self.__porte_habitacao = porte_habitacao
        if isinstance(tem_animais, bool):
            self.__tem_animais = tem_animais
        self.__termo_responsabilidade = False
        self.__adotantes = []
    @property
    def tipo_habitacao(self) -> str:
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao: str):
        if isinstance(tipo_habitacao, str):
            self.__tipo_habitacao = tipo_habitacao

    @property
    def porte_habitacao(self) -> str:
        return self.__porte_habitacao

    @porte_habitacao.setter
    def porte_habitacao(self, porte_habitacao: str):
        if isinstance(porte_habitacao, str):
            self.__porte_habitacao = porte_habitacao

    @property
    def tem_animais(self) -> str:
        return self.__tem_animais

    @tem_animais.setter
    def tem_animais(self, tem_animais: str):
        if isinstance(tem_animais, str):
            self.__tem_animais = tem_animais

    @property
    def termo_responsabilidade(self) -> bool:
        return self.__termo_responsabilidade

    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade: bool):
        if isinstance(termo_responsabilidade, bool):
            self.__termo_responsabilidade = termo_responsabilidade

    @property
    def listar_adotantes(self) -> list:
        for adotante in self.__adotantes:
            print(adotante)

    @adicionar_adotante.setter
    def adicionar_adotante(self, str):
        self.__adotantes.append(Adotante(tipo_habitacao, porte_habitacao, tem_animais))

