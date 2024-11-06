

class Doacao:
    def __init__(self, data_doacao: str, animal_doado: str, doador: str, motivo: str) -> None:
        self.__data_doacao = None
        self.__animal_doado = None
        self.__doador = None
        self.__motivo = None
        if isinstance(data_doacao, str):
            self.__data_doacao = data_doacao
        if isinstance(animal_doado, str):
            self.__animal_doado = animal_doado
        if isinstance(doador, str):
            self.__doador = doador
        if isinstance(motivo, str):
            self.__motivo = motivo

    @property
    def data_doacao(self) -> str:
        return  self.__data_doacao
    
    @data_doacao.setter
    def data_doacao(self, data_adocao: str):
        if isinstance(data_adocao, str):
            self.__data_doacao = data_adocao
    
    @property
    def animal_doado(self) -> str:
        return  self.__animal_doado
    
    @animal_doado.setter
    def animal_doado(self, animal_doado: str):
        if isinstance(animal_doado, str):
            self.animal_doado = animal_doado
    
    @property
    def doador(self) -> str:
        return  self.__doador
    
    @doador.setter
    def doado(self, doador: str):
        if isinstance(doador, str):
            self.__doador = doador
    
    @property
    def motivo(self) -> str:
        return  self.__motivo
    
    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo