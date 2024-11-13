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
        self.__cachorro = ControleCachorro()
        self.__gato = ControleGato()
        self.__doacoes = []
        self.__adocoes = []
    
    def iniciar(self):
        self.abre_tela_inicial()
    
    def finalizar(self):
        print('Encerrando o programa')
        exit()
    
    def cadastrar(self):
        opcao_escolhida = {1: self.__adotante.cadastrar_adotante, 2: self.__doador.cadastrar_doador}
        opcao = self.__tela_cadastro.opcao_cadastro()
        funcao_escolhida = opcao_escolhida[opcao]
        return funcao_escolhida() 

    def doar(self):
        animal = self.incluir_animal()
        doador = self.__doador.cadastrar_doador()
        data, motivo = self.__tela_cadastro.dados_doacao()
        doacao = Doacao(data, animal.numero_chip, doador.cpf, motivo)

        if self.buscar_doacao_repetida(doacao.doador, doacao.animal_doado):
            print(f'Doacao {doacao.doador} - {doacao.animal_doado} já realizada')
            return self.abre_tela_inicial
        
        self.__doacoes.append(doacao)
        print(f'Doacao {doacao.doador} - {doacao.animal_doado} concluida')
        return self.abre_tela_inicial 
     
    def buscar_doacao_repetida(self, cpf: str, numero_chip):
        for doacao in self.__doacoes:
            if (doacao.doador == cpf) and (doacao.animal_doado == numero_chip):
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
        adotante = self.__adotante.buscar_adotante(adotante_cpf)
        if adotante is None:
            print('Você não está cadastrado')
            adotante = self.__adotante.cadastrar_adotante()
        
        if not self.__adotante.idade_atual(adotante.data_nascimento) > 18:
            print('Você não pode adotar um animal, é menor de 18 anos')
            return self.abre_tela_inicial()
        
        if self.__doador.buscar_doador(adotante.cpf) != None:
            print('você não pode adotar um animal, pois já doou um animal')
            return self.abre_tela_inicial()
        
        animal_escolhido = self.escolher_animal()
        if animal_escolhido == None:
            print('Nenhum animal foi escolhido.')
            return self.abre_tela_inicial()
        
        if isinstance(animal_escolhido, ControleCachorro):
            if (animal_escolhido.porte == 'PorteCachorro.grande') and (adotante.tipo_habitacao == 'TipoHabitacao.apartamento_pequeno'):
                print('Esse animal não é compativel com o tamanho da sua habitação')
                return self.abre_tela_inicial()
            if not self.__cachorro.verificar_vacinas(animal_escolhido.numero_chip):
                print('O animal escolhido não tomou todas as vacinas')
                return self.abre_tela_inicial()
        else:
            if not self.__gato.verificar_vacinas(animal_escolhido.numero_chip):
                print('O animal escolhido não tomou todas as vacinas')
                return self.abre_tela_inicial()

        if self.assinar_termo_responsabilidade(adotante.cpf):
            data_adocao = self.__adotante.data_adocao
            termo = self.__adotante.termo_responsabilidade
            adocao = Adocao(data_adocao, animal_escolhido.numero_chip, adotante.cpf, termo)
            self.__adocoes.append(adocao)
            self.__cachorro.remover_cachorro(animal_escolhido.numero_chip)
            self.__gato.remover_gato(animal_escolhido.numero_chip)
            print('Adoção concluída com sucesso')
            return True
        print('Adoção não concluída')  
        return False
    
    def assinar_termo_responsabilidade(self, adotante_cpf):
        adotante = self.__adotante.assinar_termo_responsabilidade(adotante_cpf)
        return adotante

    def escolher_animal(self):
        cachorros, gatos = self.listar_animais_disponiveis()
        if (len(cachorros) == 0) and (len(gatos) == 0):
            print('Não há animais para serem adotados')
            return self.abre_tela_inicial()
        
        tentativas = 3
        while tentativas > 0:
            try:
                animal_escolhido = input('Qual o número de ID do animal que você quer adotar? ')
                if not animal_escolhido.isdigit():
                    print('Por favor, insira um ID numérico válido.')
                    continue 

                cachorro = self.__cachorro.buscar_cachorro(animal_escolhido)
                if cachorro:
                    return cachorro 

                gato = self.__gato.buscar_gato(animal_escolhido)
                if gato:
                    return gato 
                
                print('Animal não encontrado. Tente novamente.')

            except Exception as e:
                print(f'Ocorreu um erro: {e}')
                print('Tente novamente.')

            tentativas -= 1

        print('Número máximo de tentativas atingido.')
        return None  

    def incluir_animal(self):
        animal_doado = {1: self.__cachorro.cadastrar_cachorro, 2: self.__gato.cadastrar_gato}
        opcao = self.__tela_cadastro.opcao_doar()
        funcao_escolhida = animal_doado[opcao]
        return funcao_escolhida()
        
    def listar_adotantes(self) -> str:
        adotantes = self.__adotante.listar_adotantes()
        for adotante in adotantes:
            print(f'Adotante = Nome {adotante.nome} - CPF{adotante.cpf}')
        return self.abre_tela_inicial()
    
    
    def listar_doadores(self) -> str:
        doadores = self.__doador.listar_doadores()
        for doador in doadores:
            print(f'Doador = Nome {doador.nome} - CPF{doador.cpf}')
        return self.abre_tela_inicial()

    
    def listar_animais_disponiveis(self):
        cachorros = self.__cachorro.listar_cachorros()
        gatos = self.__gato.listar_gatos()

        if cachorros is not None and len(cachorros) > 0:
            print(f'Cachorros disponíveis:')
            for cachorro in cachorros:
                print(f'Nome: {cachorro.nome}, ID: {cachorro.numero_chip}')
        else:
            print('Não há cachorros disponíveis.')

        if gatos is not None and len(gatos) > 0:
            print(f'Gatos disponíveis:')
            for gato in gatos:
                print(f'Nome: {gato.nome}, ID: {gato.numero_chip}')
        else:
            print('Não há gatos disponíveis.')

        return cachorros, gatos   

    def listar_doacoes(self) -> str:
        inicio, fim= self.__tela_inicial.periodo()
        doacoes = self.__doacoes
        for doacao in doacoes:
            if (doacao.data_doacao >= inicio) and (doacao.data_doacao <= fim):
                print(f'Doação feita em {doacao.data_doacao}, por {doacao.doador}, '
                      f'do animal {doacao.animal_doado} pelo motivo {doacao.motivo}')
    
    def listar_adocoes(self):
        inicio, fim = self.__tela_inicial.periodo()
        adocoes = self.__adocoes
        for adocao in adocoes:
            if (adocao.data_adocao >= inicio) and (adocao.data_adocao <= fim):
                print(f'Adoção feita em {adocao.data_adocao}, por {adocao.adotante}, '
                      f'do animal {adocao.animal_escolhido}')

    def buscar_animal(self, numero_chip):
        animal = self.__cachorro.buscar_cachorro(numero_chip)
        if animal is not None:
            return animal
        animal = self.__gato.buscar_gato(numero_chip)
        return animal
               
    def listar_animais_adotados(self) -> str:
        animais_adotados = self.__adocoes
        for animal in animais_adotados:
            print(f'{animal.nome} - {animal.numero_chip}')

    def vacinar(self):
        numero_chip, vacina, data_aplicacao  = self.__tela_inicial.tela_vacinar()
        gato = self.__gato.buscar_gato(numero_chip)
        if gato is not None:
            self.__gato.vacinar(gato, vacina, data_aplicacao)
            return f'Animal {gato.nome}, foi vacinado para {vacina}'
        else:
            cachorro = self.__cachorro.buscar_cachorro(numero_chip)
            if cachorro is not None:
                self.__cachorro.vacinar(cachorro, vacina, data_aplicacao)
                return f'Animal {cachorro.nome}, foi vacinado para {vacina}'
        return None
    
    def abre_tela_inicial(self):
        opcao_escolhida = {0: self.finalizar, 1: self.cadastrar, 2: self.doar, 3: self.adotar, 4: self.incluir_animal, 
                           5: self.listar_adotantes, 6: self.listar_doadores, 7: self.listar_animais_disponiveis,
                           8: self.listar_animais_adotados, 9: self.vacinar, 10: self.listar_doacoes,
                           11: self.listar_adocoes}
        while True:
            opcao = self.__tela_inicial.mostra_tela_opcoes()
            funcao_escolhida = opcao_escolhida[opcao]
            funcao_escolhida()
