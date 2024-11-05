from cachorro import Cachorro
from telaCachorro import TelaCachorro
from controleMovimentacao import ControleMovimentacao


class ControleCachorro:
    def __init__(self) -> None:
        self.__tela_cachorro = TelaCachorro(self)
        self.__cadastro_cachorros = []
        
    def cadastrar_cachorro(self):
        cadastrar_cachorro = self.__tela_cachorro.cadastrar_cachorro
        novo_cachorro = Cachorro(cadastrar_cachorro)
        if self.buscar_cachorro(novo_cachorro.numero_chip):
            print('Esse cachorro já foi cadastrado')
            return True
        self.__cadastro_cachorros.append(novo_cachorro)
        print('Cachorro cadastrado')
        return novo_cachorro

    def buscar_cachorro(self, numero_chip: str) -> Cachorro:
        for cachorro in self.__cadastro_cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
            return 'Cachorro não localizado'
        
    def remover_cachorro(self, numero_chip: str):
        for cachorro in self.__cadastro_cachorros:
            if cachorro.numero_chip == numero_chip:
                self.__cadastro_cachorros.pop(cachorro)
                print('Cachorro removido da lista de adoção')
    
    def listar_cachorros(self) -> list:
        for cachorro in self.__cadastros_cachorros:
            print(f'Cachorro nome: {cachorro.nome} - ID: {cachorro.numero_chip}')

    def vacinar(self):
        self.cachorro.aplicar_vacina(numero_chip, vacina, data_aplicacao)
    
    def historico_vacina(self) -> list:
        return self.cachorro.historico_vacinas()

    def verificar_vacinas(self):
        vacinas_necessarias = ['raiva', 'leptospirose', 'hepatite_infecciosa']
        vacinas = self.historico_vacinas()
        for vacina in vacinas:
            if

