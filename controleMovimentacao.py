from adocao import Adocao
from doacao import Doacao
from controleAdotante import ControleAdotante
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

        animal_escolhido = self.listar_animais_disponiveis

        '''
        1. Somente podem adotar animais as pessoas com mais de 18 anos completos.
        2. Pessoas que doaram um animal não podem adotar um animal. 
        3. Somente podem ser adotados os animais que já receberam as vacinas: raiva, 
        leptospirose e hepatite infecciosa.
        4. Cães de porte grande não podem ser adotados por pessoas que moram em 
        apartamento pequeno.
        
        '''
    def escolher_animal(self):
        pass

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



