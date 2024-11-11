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
        self.__doacoes = []
        self.__adocoes = []
    
    def iniciar(self):
        self.abre_tela_inicial()
    
    def finalizar(self):
        print('Encerrando o programa')
        exit()
    
    def cadastrar(self):
        opcao_escolhida = {1: self.controleAdotante.cadastrar_adotante, 2: self.controleDoador.cadastrar_doador}
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
        doador = self.controleDoador.cadastrar_doador()

        if doador:
            print('Essa pessoa já possui cadastro')
            return self.abre_tela_inicial()
        print('Cadastro realizado com sucesso!')
        dados_doacao = self.__tela_cadastro.dados_doacao()
        doacao = Doacao(dados_doacao[0], animal, doador, dados_doacao[1])

        if  self.__doacoes.inserir_doacao(doacao):
            return 'Doacao realizada'
        return 'Doação não concluida' 
     
    def buscar_doacao_repetida(self, cpf: str, numero_chip):
        for doacao in self.__doacoes:
            if (doacao.doador.cpf == cpf) and (doacao.animal.numero_chip == numero_chip):
                return True
        return False
    
    @property
    def listar_doadores(self) -> str:
        doadores = self.controleDoador.listar_doadores()
        for doador in doadores:
            print(f'Doadores: Nome {doador.nome} - CPF {doador.cpf}')

    @property
    def buscar_doacoes(self) -> list:
        return self.__doacoes
    
    def inserir_doacao(self, doacao: Doacao):
        if not self.buscar_doacao_repetida(doacao.doador.cpf, doacao.animal_doado.numero_chip):
            self.__doacoes.append(doacao)
            print (f'Doação cadastrada com sucesso')
            return True
        return False

    def adotar(self):
        adotante_cpf = str(input('entre com o seu CPF: '))
        adotante = ControleAdotante.buscar_adotante(adotante_cpf)
        if not adotante:
            print('Você não está cadastrado')
            return ControleAdotante.cadastrar_adotante()
        
        if not ControleAdotante.idade_atual(adotante.data_nascimento) > 18:
            print('Você não pode adotar um animal, é menor de 18 anos')
            return self.abre_tela_inicial()
        
        if ControleDoador.buscar_doador(adotante.cpf):
            print('você não pode adotar um animal, pois já doou um animal')
            return self.abre_tela_inicial()
        
        animal_escolhido = self.escolher_animal()
        if isinstance(animal_escolhido, ControleCachorro):
            if (animal_escolhido.porte == 'PorteCachorro.grande') and (adotante.tipo_habitacao == 'TipoHabitacao.apartamento_pequeno'):
                print('Esse animal não é compativel com o tamanho da sua habitação')
                return self.abre_tela_inicial()
            if not ControleCachorro.verificar_vacinas(animal_escolhido.numero_chip):
                print('O animal escolhido não tomou todas as vacinas')
                return self.abre_tela_inicial()
        else:
            if not ControleGato.verificar_vacinas(animal_escolhido.numero_chip):
                print('O animal escolhido não tomou todas as vacinas')
                return self.abre_tela_inicial()

        if self.assinar_termo_responsabilidade(adotante.cpf):
            data_adocao = ControleAdotante.data_adocao
            termo = ControleAdotante.termo_responsabilidade
            adocao = Adocao(data_adocao, animal_escolhido.numero_chip, adotante.cpf, termo)
            self.__adocoes.append(adocao)
            ControleCachorro.remover_cachorro(animal_escolhido.numero_chip)
            ControleGato.remover_gato(animal_escolhido.numero_chip)
            print('Adoção concluída com sucesso')
            return True
        print('Adoção não concluída')  
        return False
    
    def assinar_termo_responsabilidade(self, adotante_cpf):
        adotante = ControleAdotante.assinar_termo_responsabilidade(adotante_cpf)
        return adotante

    def escolher_animal(self):
        tentativas = 3
        while tentativas > 0:
            self.listar_animais_disponiveis()
            animal_escolhido = input('Qual o nome do animal que você quer adotar? ')
            cachorro = ControleCachorro.buscar_cachorro(animal_escolhido)
            if cachorro:
                return cachorro
            gato = ControleGato.buscar_gato(animal_escolhido)
            if gato:
                return gato
            print('Animal não encontrado. Tente novamente.')
            tentativas -= 1
        print('Número máximo de tentativas atingido.')
        return None

    def incluir_animal(self):
        animal_doado = {1: ControleCachorro.cadastrar_cachorro, 2: ControleGato.cadastrar_gato}
        while True:
            opcao = self.__tela_cadastro.opcao_doar()
            funcao_escolhida = animal_doado[opcao]
            funcao_escolhida()
    @property
    def listar_adotantes(self) -> str:
        adotantes = ControleAdotante.listar_adotantes()
        for adotante in adotantes:
            print(f'Adotante = Nome {adotante.nome} - CPF{adotante.cpf}')
        return self.abre_tela_inicial()
    
    @property
    def listar_doadores(self) -> str:
        doadores = ControleDoador.listar_doadores()
        for doador in doadores:
            print(f'Doador = Nome {doador.nome} - CPF{doador.cpf}')
        return self.abre_tela_inicial()

    @property
    def listar_animais_disponiveis(self):
        ControleCachorro.listar_cachorros()
        ControleGato.listar_gatos()

    @property 
    def listar_doacoes(self) -> str:
        inicio, fim= self.__tela_inicial.periodo()
        doacoes = self.__doacoes
        for doacao in doacoes:
            if (doacao.data_doacao >= inicio) and (doacao.data_doacao <= fim):
                print(f'Doação feita em {doacao.data_doacao}, por {doacao.doador}, '
                      f'do animal {doacao.animal_doado} pelo motivo {doacao.motivo}')
    
    @property
    def listar_adocoes(self):
        inicio, fim = self.__tela_inicial.periodo()
        adocoes = self.__adocoes
        for adocao in adocoes:
            if (adocao.data_adocao >= inicio) and (adocao.data_adocao <= fim):
                print(f'Adoção feita em {adocao.data_adocao}, por {adocao.adotante}, '
                      f'do animal {adocao.animal_escolhido}')

    @property            
    def listar_animais_adotados(self) -> str:
        animais_adotados = self.__adocoes
        for animal in animais_adotados:
            print(f'{animal.nome} - {animal.numero_chip}')

    def vacinar(self, numero_chip, vacina, data_aplicacao):
        if ControleGato.buscar_gato(numero_chip):
            self.controleGato.vacinar(numero_chip, vacina, data_aplicacao)
            return f'Vacina aplicada ao {numero_chip}'
        else:
            if self.controleCachorro.buscar_cachorro(numero_chip):
                self.controleCachorro.vacinar(numero_chip, vacina, data_aplicacao)
                return f'Vacina aplicada ao {numero_chip}'
        return None
        
    def vacinar_animal(self):
        animal = self.__tela_inicial.tela_vacinar()
        self.vacinar(animal[0], animal[1], animal[2])
    
    def abre_tela_inicial(self):
        opcao_escolhida = {0: self.finalizar, 1: self.cadastrar, 2: self.doar, 3: self.adotar, 4: self.incluir_animal, 
                           5: self.listar_adotantes, 6: self.listar_doadores, 7: self.listar_animais_disponiveis,
                           8: self.listar_animais_adotados, 9: self.vacinar_animal, 10: self.listar_doacoes,
                           11: self.listar_adocoes}
        while True:
            opcao = self.__tela_inicial.mostra_tela_opcoes()
            funcao_escolhida = opcao_escolhida[opcao]
            funcao_escolhida()
