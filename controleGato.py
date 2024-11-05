from gato import Gato
from telaGato import TelaGato
from controleMovimentacao import ControleMovimentacao


class ControleGato:
    def __init__(self) -> None:
        self.__tela_gato = TelaGato
        self.__gatos = []

    def cadastrar_gato(self):
        cadastrar_gato = self.__tela_gato.cadastrar_gato
        novo_gato = Gato(cadastrar_gato)
        if self.buscar_gato(novo_gato.numero_chip):
            print('Esse gato já foi cadastrado')
            return True
        self.__gatos.append(novo_gato)
        print('gato cadastrado')
        return novo_gato
    
    def listar_gatos(self) -> str:
        for gato in self.__gatos:
            print(f'Gato nome: {gato.nome} - ID: {gato.numero_chip}')

    def buscar_gato(self, numero_chip: str) -> Gato:
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                return gato
            return 'Gato não localizado'

    def remover_gato(self, numero_chip: str):
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                self.___gatos.pop(gato)
                print('Gato removido da lista de adoção')
        
    def aplicar_vacina(self, numero_chip: str, vacina_aplicada: str, data_aplicacao: str):
        self.gato.aplicar_vacina(numero_chip, vacina_aplicada, data_aplicacao):

    def verificar_vacinas(self):
        pass
