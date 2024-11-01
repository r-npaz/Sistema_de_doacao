from animal import Animal
from enum import Enum 

class PorteCachorro(Enum):
    pequeno = 1
    medio = 2
    grande = 3

class Cachorro(Animal):
    def __init__(self, porte: str, 
                 numero_chip: str, 
                 nome: str, 
                 raca: str, 
                 vacina_aplicada: str, 
                 data_aplicacao: str):
        super().__init__(numero_chip, nome, raca, vacina_aplicada, data_aplicacao)
        self.__porte = None
        if isinstance(porte, str):
            self.__porte = porte

    @property
    def porte(self) -> str:
        return self.__porte
    
    @porte.setter
    def porte(self, porte: str):
        if isinstance(porte, str):
            self.__porte = porte
    
    def raca(self):
        pass
    