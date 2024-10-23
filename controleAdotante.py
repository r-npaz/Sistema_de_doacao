from adotante import Adotante
from telaAdotante import TelaAdotante
from controleMovimentacao import ControleMovimentacao


class ControleAdotante:
    def __init__(self) -> None:
        self.__tela_adotante = TelaAdotante(self)

    def cadastrar_adotante(self):
        #chamar a tela de adotante para pegar os dados e passar como parametro.
        adotante = self.__tela_adotante.mostra_dados()
        
        pass
    
    def alterar_adotante(self):
        pass

    def excluir_adoante(self):
        pass
    
    def animais_disponiveis(self) -> dict:
        pass

    def adotar_animal(self):
        #avalia se todos os critérios para adoção foram respeitados
        pass





