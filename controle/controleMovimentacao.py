from entidade.adocao import Adocao
from entidade.doacao import Doacao
from controle.controleAdotante import ControleAdotante
from controle.controleDoador import ControleDoador
from controle.controleCachorro import ControleCachorro
from controle.controleGato import ControleGato
from limite.telaInicial import TelaInicial
from limite.telaCadastro import TelaCadastro


class ControleMovimentacao:
    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__tela_cadastro = TelaCadastro()
        self.__adotante = ControleAdotante()
        self.__doador = ControleDoador()
        self.__gato = ControleGato()
        self.__cachorro = ControleCachorro()
        self.__doacoes = []
        self.__adocoes = []
    
    def iniciar(self):
        self.abre_tela_inicial()
    
    def finalizar(self):
        print('Encerrando o programa')
        exit()
    
    def cadastrar(self):
        opcao_escolhida = {1: self.__adotante.cadastrar_adotante, 2: self.__doador.cadastrar_doador}
        while True:
            opcao = self.__tela_cadastro.opcao_cadastro()
            funcao_escolhida = opcao_escolhida[opcao]
            funcao_escolhida() 

    def doar(self):
        animal = self.incluir_animal()
        if animal:
            print('Esse animal já foi doado uma vez')
            return self.abre_tela_inicial()
        print('Animal cadastrado com sucesso!')
        doador = self.__doador.cadastrar_doador()

        if doador:
            print('Essa pessoa já possui cadastro')
            return self.abre_tela_inicial()
        print('Cadastro realizado com sucesso!')
        dados_doacao = self.__tela_cadastro.dados_doacao()
        doacao = Doacao(dados_doacao[0], animal, doador, dados_doacao[1])

        if self.buscar_doacao_repetida():
            return f'A doação do animal {animal.numero_chip} já foi feita por {doador.cpf}'

        if self.__doacao.buscar_doacao(animal.numero) == False:
            self.__doacao.inserir_doacao
            return 'Doacao realizada'
        return 'Doação não concluida' 
     
    def buscar_doacao_repetida(self, cpf: str, numero_chip):
        for doacao in self.__doacoes:
            if (doacao.doador.cpf == cpf) and (doacao.animal.numero_chip == numero_chip):
                return True
        return False
    
    @property
    def buscar_doacoes(self) -> list:
        return self.__doacoes
    
    def inserir_doacao(self, doacao: Doacao):
        if not self.buscar_doacao_repetida(doacao.doador.cpf, doacao.animal_doado.numero_chip):
            self.__doacoes.append(doacao)
            return 'Doacção cadastrada com sucesso'

    def adotar(self):
        adotante_cpf = str(input('entre com o seu CPF: '))
        adotante = self.__adotante.buscar_adotante(adotante_cpf)
        if not adotante:
            print('Você não está cadastrado')
            return self.__adotante.cadastrar_adotante()
        
        if not self.__adotante.idade_atual(adotante.data_nascimento) > 18:
            print('Você não pode adotar um animal, é menor de 18 anos')
            return self.abre_tela_inicial()
        
        if self.__doador.buscar_doador(adotante.cpf):
            print('você não pode adptar um animal, pois já doou um animal')
            return self.abre_tela_inicial()
        
        animal_escolhido = self.escolher_animal()
        if isinstance(animal_escolhido, ControleCachorro):
            if (animal_escolhido.porte == 3) and (adotante.tipo_habitacao == 3):
                print('Esse animal não é compativel com o tamanho da sua habitação')
                return self.abre_tela_inicial()
            if not self.__cachorro.verificar_vacinas(animal_escolhido.numero_chip):
                print('O animal escolhido não tomou todas as vacinas')
                return self.abre_tela_inicial()
        else:
            if not self.__gato.verificar_vacinas(animal_escolhido.numero_chip):
                print('O animal escolhido não tomou todas as vacinas')
                return self.abre_tela_inicial()

        if self.__adotante.assinar_termo_responsabilidade(adotante.cpf):
            adocao = Adocao(self.__adotante.data_adocao, animal_escolhido.numero_chip, adotante.cpf, self.__adotante.termo_responsabilidade )
            self.__adocoes.append(adocao)
            self.__cachorro.remover_cachorro(animal_escolhido.numero_chip)
            self.__gato.remover_gato(animal_escolhido.numero_chip)
            print('Adoção concluída com sucesso')
            return True
        print('Adoção não concluída')  
        return False
    
    def escolher_animal(self): #aqui talvez eu poderia add um parametro para não ficar em loop infinito
        tentativas = 3
        while tentativas > 0:
            self.listar_animais_disponiveis()
            animal_escolhido = input('Qual o nome do animal que você quer adotar? ')
            cachorro = self.__cachorro.buscar_cachorro(animal_escolhido)
            if cachorro:
                return cachorro
            gato = self.__gato.buscar_gato(animal_escolhido)
            if gato:
                return gato
            print('Animal não encontrado. Tente novamente.')
            tentativas -= 1
        print('Número máximo de tentativas atingido.')
        return None

    def incluir_animal(self):
        animal_doado = {1: self.__cachorro.cadastrar_cachorro, 2: self.__gato.cadastrar_gato}
        while True:
            opcao = self.__tela_cadastro.opcao_doar
            funcao_escolhida = animal_doado[opcao]
            funcao_escolhida()

    def listar_adotantes(self):
        pass

    def listar_doadores(self):
        pass

    def listar_animais_disponiveis(self):
        self.__cachorro.listar_cachorros()
        self.__gato.listar_gatos()
        
    def listar_animais_adotados(self):
        pass

    def listar_animais_doados(self):
        pass

    def vacinar(self, numero_chip, vacina, data_aplicacao):
        if self.__gato.buscar_gato(numero_chip):
            self.__gato.aplicar_vacina
            return f'Vacina aplicada ao {numero_chip}'
        else:
            if self.__cachorro.buscar_cachorro(numero_chip):
                self.__cachorro.aplicar_vacina
                return f'Vacina aplicada ao {numero_chip}'
        return None
        
    def vacinar_animal(self):
        animal = self.__tela_inicial.tela_vacinar()
        self.vacinar(animal)
    
    def abre_tela_inicial(self):
        opcao_escolhida = {0: self.finalizar, 1: self.cadastrar, 2: self.doar, 3: self.adotar, 4: self.incluir_animal, 
                           5: self.listar_adotantes, 6: self.listar_doadores, 7: self.listar_animais_disponiveis,
                           8: self.listar_animais_adotados, 9: self.vacinar_animal}
        while True:
            opcao = self.__tela_inicial.mostra_tela_opcoes()
            funcao_escolhida = opcao_escolhida[opcao]
            funcao_escolhida()



