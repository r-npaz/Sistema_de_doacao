

class Adocao:
    def __init__(self, data_adocao: str, animal_escolhido: str, adotante: str, termo_responsabilidade: bool):
        self.__data_adocao = None
        self.__animal_escolhido = None
        self.__adotante = None
        self.__termo_responsabilidade = None
        if isinstance(data_adocao, str):
            self.__data_adocao = data_adocao
        if isinstance(animal_escolhido, str):
            self.__animal_escolhido = animal_escolhido
        if isinstance(adotante, str):
            self.__adotante = adotante
        if isinstance(termo_responsabilidade, bool):
            self.__termo_responsabilidade = termo_responsabilidade
        
    @property
    def data_adocao(self) -> str:
        return self.__data_adocao
        
    @data_adocao.setter
    def data_adocao(self, data_adocao: str):
        if isinstance(data_adocao, str):
            self.__data_adocao = data_adocao
        
    @property
    def animal_escolhido(self) -> str:
        return self.__animal_escolhido
        
    @animal_escolhido.setter
    def animal_escolhido(self, animal_escolhido: str):
        if isinstance(animal_escolhido, str):
            self.__animal_escolhido = animal_escolhido
        
    @property
    def adotante(self) -> str:
        return self.__adotante
        
    @adotante.setter
    def adotante(self, adotante: str):
        if isinstance(adotante, str):
            self.__adotante = adotante
                
    @property
    def termo_responsabilidade(self) -> str:
        return self.__termo_responsabilidade
        
    @termo_responsabilidade.setter
    def termo_responsabilidade(self, termo_responsabilidade: str):
        if isinstance(termo_responsabilidade, str):
            self.__termo_responsabilidade = termo_responsabilidade
