

class Doacao:
    def __init__(self, data_doacao: str, animal_doado: Animal, doador: Pessoa, motivo: str) -> None:
        self.__data_doacao = None
        self.__animal_doado = None
        self.__doador = None
        self.__motivo = None
        self.__doacoes = []
        if isinstance(data_doacao, str):
            self.__data_doacao = data_doacao
        if isinstance(animal_doado, Animal):
            self.__animal_doado = animal_doado
        if isinstance(doador, Pessoa):
            self.__doador = doador
        if isinstance(motivo, str):
            self.__motivo = motivo

    @property
    def doacoes(self):
        for doacao in self.__doacoes:
            print(doacao)
    
    @property
    def buscar_doador(self, cpf:str) -> str:
        for doacao in self.__doacoes:
            if doacao.doador.cpf == cpf:
                return doacao.doador
        return None
    
    def inserir_doacao(self, doacao: Doacao):
        if isinstance(doacao, Doacao):
            self.__doacoes.append(doacao)
            return 'Doacao acrescentada'
        return False
    
    def buscar_doacao(self, numero_chip: str):
        for doacao in self.__doacoes:
            if doacao.animal_doado.numero_chip == numero_chip:
                return True
        return False