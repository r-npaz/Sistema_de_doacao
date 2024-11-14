from entidade.animal import Animal
from enum import Enum 

class PorteCachorro(Enum):
    pequeno = 1
    medio = 2
    grande = 3

class Cachorro(Animal):
    def __init__(self, porte: int, numero_chip: str, nome: str, raca: str, 
                 vacina_aplicada: int = "", data_aplicacao: str = ""):
        super().__init__(numero_chip, nome, raca, vacina_aplicada, data_aplicacao)
        self.__porte = PorteCachorro(porte) if porte in PorteCachorro._value2member_map_ else None

    @property
    def porte(self) -> PorteCachorro:
        return self.__porte
    
    @porte.setter
    def porte(self, porte: int):
        if isinstance(porte, int) and porte in PorteCachorro._value2member_map_:
            self.__porte = PorteCachorro(porte)
   
    def aplicar_vacina(self, animal: Animal, vacina_aplicada: int, data_aplicacao: str):
        return super().aplicar_vacina(animal, vacina_aplicada, data_aplicacao)
        