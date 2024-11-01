from doador import Doador
from telaDoador import TelaDoador
from controleMovimentacao import ControleMovimentacao


class ControleDoador:

    def __init__(self) -> None:
            self.__tela_doador = TelaDoador()
            self.__doadores = []
   
    def cadastrar_doador(self):
        cadastrar_doador = self.__tela_doador
        novo_doador = Doador(cadastrar_doador) #seria uma boa pratica eu verificar se já existe antes de criar?
        if self.buscar_doador(novo_doador.cpf):
            return True
        self.__doadores.append(novo_doador)
        return novo_doador
    
    def buscar_doador(self, cpf: str) -> Doador:
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
            return None
    
    def doar_animal(self, animal: Animal):
         pass
        
    def tela_doador(self):
         doador = self.__tela_doador.mostrar_tela_cadastro
         return doador
         
         
        
         
        
            



    

