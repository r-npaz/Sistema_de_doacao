from adocao import Adocao
from doacao import Doacao
from controleAdotante import ControleAdotante
from controleDoador import ControleDoador
from controleCachorro import ControleCachorro
from controleGato import ControleGato
from telaInicial import TelaInicial
from telaCadastro import TelaCadastro
from telaAdotante import TelaAdotante
from telaDoador import TelaDoador


class ControleMovimentacao:
    def __init__(self):
        self.__tela_inicial = TelaInicial(self)
        self.__tela_cadastro = TelaCadastro(self)
        self.__tela_adotante = TelaAdotante(self) # isso não deveria estar aqui, pertence ao controleAdotante
        self.__tela_doador = TelaDoador(self) # mesma coisa do de cima
        self.__adotante = ControleAdotante(self)
        self.__doador = ControleDoador(self)

        #Não consegui compreender o real necessidade de inicializar a tela aqui e pq não funciona 
        #se eu chamar o metodo mostra_opcao_tela no metodo abre_tela_inicial
 
    
    def iniciar(self):
        self.abre_tela_inicial()
    
    def finalizar(self):
        print('Encerrando o programa')
        exit()
    
    def cadastrar(self):
        opcao_escolhida = {1: self.cadastrar_adotante, 2: self.cadastrar_doador}
        while True:
            opcao = self.__tela_cadastro.opcao_cadastro()
            funcao_escolhida = opcao_escolhida[opcao]
            funcao_escolhida() 

    def cadastrar_adotante(self):
        adotante = self.__tela_adotante.mostrar_tela_cadastro()
        self.__adotante.cadastrar_adotante(adotante)

    def cadastrar_doador(self):
        doador = self.__tela_doador.mostrar_tela_cadastro()
        self.__doador.cadastra_doador(doador)

    def doar(self):
        pass

    def adotar(self):
        adotante_cpf = int(input('entre com o seu CPF: '))
        #aqui tem que tratar a entrada do usuário 
        adotante = self.pessoasCadastradas.buscar_cadastrado(adotante_cpf)
        if not adotante:
            print('Você não está cadastrado')
            return self.abre_tela_inicial
        
        if self.controleAdotante.idade_atual(adotante.data_nascimento) < 18:
            return f'Você não pode adotar um animal'
        
        if adotante.doador == True:
            return f'Você NÃO pode adotar um animal, visto que já doou um animal'

        animal_escolhido = self.escolher_animal()
        

        '''
        1. Somente podem adotar animais as pessoas com mais de 18 anos completos.
        2. Pessoas que doaram um animal não podem adotar um animal. 
        3. Somente podem ser adotados os animais que já receberam as vacinas: raiva, 
        leptospirose e hepatite infecciosa.
        4. Cães de porte grande não podem ser adotados por pessoas que moram em 
        apartamento pequeno.
        
        '''
    def escolher_animal(self): #aqui talvez eu poderia add um parametro para não ficar em loop infinito
        self.listar_animais_disponiveis()
        animal_escolhido = (str(input('Qual o nome do animal que você quer adotar? ')))
        #aqui tem que tratar essa entrada do usuário
        cachorro = self.controleCachorro.buscar_cachorro(animal_escolhido)
        if cachorro:
            return cachorro.nome

        gato = self.controleGato.buscar_gato(animal_escolhido)
        if gato:
            return gato.nome
        
        print('Não existe esse animal para adotar')
        return self.escolher_animal()

    def incluir_animal(self):
        pass

    def listar_adotantes(self):
        pass

    def listar_doadores(self):
        pass

    def listar_animais_disponiveis(self):
        self.controleCachorro.listar_cachorros_disponiveis
        self.controleGato.listar_gatos_disponiveis
        
    def listar_animais_adotados(self):
        pass
    
    def abre_tela_inicial(self):
        opcao_escolhida = {0: self.finalizar, 1: self.cadastrar, 2: self.doar, 3: self.adotar, 4: self.incluir_animal, 
                           5: self.listar_adotantes, 6: self.listar_doadores, 7: self.listar_animais_disponiveis,
                           8: self.listar_animais_adotados}
        while True:
            opcao = self.__tela_inicial.mostra_tela_opcoes()
            funcacao_escolhida = opcao_escolhida[opcao]
            funcacao_escolhida()



