from entidade.doador import Doador
from limite.telaDoador import TelaDoador


class ControleDoador:

    def __init__(self) -> None:
            self.__tela_doador = TelaDoador()
            self.__doadores = []
   
    def cadastrar_doador(self):
        cadastrar_doador = self.__tela_doador
        novo_doador = Doador(cadastrar_doador[0], cadastrar_doador[1], cadastrar_doador[2], cadastrar_doador[3]) #seria uma boa pratica eu verificar se já existe antes de criar?
        if self.buscar_doador(novo_doador.cpf):
            return True
        self.__doadores.append(novo_doador)
        return novo_doador
    
    def buscar_doador(self, cpf: str) -> Doador:
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
            return None
    
    @property
    def listar_doadores(self) -> list:
        return self.__doadores
    
    def excluir_adotante(self, cpf: str):
        for doador in self.__doadores:
            if doador.cpf == cpf:
                self.__doadores.remove(doador)
                return f'Doador: {doador.cpf} - {doador.nome} excluido!'
        return False
        
    def tela_doador(self):
         doador = self.__tela_doador.mostrar_tela_cadastro()
         return doador
         
         
        
         
        
            



    

