from adotante import Adotante
from telaAdotante import TelaAdotante
from controleMovimentacao import ControleMovimentacao


class ControleAdotante:
    def __init__(self) -> None:
        self.__tela_adotante = TelaAdotante(self)
        self.__adotantes = []

    def cadastrar_adotante(self, tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco):        
        adotante = Adotante(tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco)
        self.__adotantes.append(adotante)
        
    def alterar_adotante(self):
        pass

    def excluir_adoante(self):
        pass
    
    def animais_disponiveis(self) -> dict:
        pass

    def adotar_animal(self):
        #avalia se todos os critérios para adoção foram respeitados
        pass
    
    def abre_tela_adotante(self):
        while True:
            self.__tela_adotante.mostrar_tela_cadastro()




