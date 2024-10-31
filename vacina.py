

class Vacina:
    def __init__(self, animal_vacinado: str, vacina_aplicada: str, data_aplicacao: str,):

        self.__animal_vacinado = None
        self.__vacina_aplicada = None
        self.__data_aplicacao = None
        if isinstance(animal_vacinado, str):
            self.__animal_vacinado = animal_vacinado
        if isinstance(vacina_aplicada, str):
            self.__vacina_aplicada = vacina_aplicada
        if isinstance(data_aplicacao, str):
            self.__data_aplicacao = data_aplicacao    
    
    
    #aqui talvez poderia ter um historico das vacinas aplicadas, não sei
    