from adocao import Adocao
from doacao import Doacao
from controleAdocao import ControleAdotante
from controleDoador import ControleDoador
from controleCachorro import ControleCachorro
from controleGato import ControleGato
from telaInicial import TelaInicial
from cadastrados import PessoasCadastradas


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
    
    def cadastrar(self):
        pass

    def doar(self):
        pass

    def adotar(self):
        cadastrados = self.pessoasCadastradas.cadastrados()
        adotante = int(input('entre com o seu CPF: '))
        #aqui tem que tratar a entrada do usuário 
        if adotante not in cadastrados.cpf:
            return 'Faça o cadastro'
        animal = self.controleAdotante.escolher_animal()
        porte_residencia = self.controleAdotante.porte_residencia
        if 
        '''
        1. Somente podem adotar animais as pessoas com mais de 18 anos completos.
        2. Pessoas que doaram um animal não podem adotar um animal. 
        3. Somente podem ser adotados os animais que já receberam as vacinas: raiva, 
        leptospirose e hepatite infecciosa.
        4. Cães de porte grande não podem ser adotados por pessoas que moram em 
        apartamento pequeno.
        
        '''

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
        opcao_escolhida = {0: self.finalizar, 1: self.cadastrar, 2: self.doar, 3: self.adotar, 4: self.incluir_animal, 
                           5: self.listar_adotantes, 6: self.listar_doadores, 7: self.listar_animais_disponiveis,
                           8: self.listar_animais_adotados}
        while True:
            opcao = self.__tela_inicial.mostra_tela_opcoes()
            funcacao_escolhida = opcao_escolhida[opcao]
            funcacao_escolhida()



