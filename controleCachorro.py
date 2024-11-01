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

    def vacinar(self):
        pass

    def verificar_vacinas(self):
        pass
