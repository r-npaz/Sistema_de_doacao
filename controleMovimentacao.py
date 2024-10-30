from adocao import Adocao
from doacao import Doacao
from controleAdocao import ControleAdotante
from controleDoador import ControleDoador
from controleCachorro import ControleCachorro
from controleGato import ControleGato
from telaInicial import TelaInicial


class ControleMovimentacao:
    def __init__(self):
        self.__tela_inicial = TelaInicial(self) 
        #Não consegui compreender o real necessidade de inicializar a tela aqui e pq não funciona 
        #se eu chamar o metodo mostra_opcao_tela no metodo abre_tela_inicial
    
    def iniciar(self):
        self.abre_tela_inicial()
    
    def finalizar(self):
        print('Encerrando o programa')
        exit()

    def doar(self):
        pass

    def adotar(self):
        pass

    def incluir_animal(self):
        pass

    def listar_adotantes(self):
        pass

    def listar_doadores(self):
        pass

    def listar_animais_disponiveis(self):
        pass

    def listar_animais_adotados(self):
        pass
    
    def abre_tela_inicial(self):
        opcao_escolhida = {0: self.finalizar, 1: self.doar, 2: self.adotar, 3: self.incluir_animal, 
                           4: self.listar_adotantes, 5: self.listar_doadores, 6: self.listar_animais_disponiveis,
                           7: self.listar_animais_adotados}
        while True:
            opcao = self.__tela_inicial.mostra_tela_opcoes()
            funcacao_escolhida = opcao_escolhida[opcao]
            funcacao_escolhida()



