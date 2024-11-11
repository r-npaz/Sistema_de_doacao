from entidade.cachorro import Cachorro
from limite.telaCachorro import TelaCachorro


class ControleCachorro:
    def __init__(self) -> None:
        self.__tela_cachorro = TelaCachorro()
        self.__cadastro_cachorros = []
        self.__vacinas_aplicadas = []
        
    def cadastrar_cachorro(self):
        cadastrar_cachorro = self.__tela_cachorro.cadastrar_cachorro()
        novo_cachorro = Cachorro(cadastrar_cachorro[0], cadastrar_cachorro[1], cadastrar_cachorro[2], cadastrar_cachorro[3], cadastrar_cachorro[4], cadastrar_cachorro[5])
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
    
    def listar_cachorros(self) -> str:
        return self.__cadastro_cachorros

    def vacinar(self, numero_chip, vacina, data_aplicacao):
        vacina_tomada = Cachorro.aplicar_vacina_cachorro(numero_chip, vacina, data_aplicacao)
        self.__vacinas_aplicadas.append(vacina_tomada)

    def historico_vacina(self, numero_chip: str) -> list:
        vacinas = [vacina for vacina in self.__vacinas_aplicadas if vacina.numero_chip == numero_chip]
        return vacinas

    def verificar_vacinas(self):
        vacinas_necessarias = ['VacinasNecessarias.raiva', 'VacinasNecessarias.leptospirose', 'VacinasNecessarias.hepatite_infecciosa']
        vacinas = self.historico_vacina()
        aplicadas = 0
        for vacina in vacinas:
            for vacina_necessaria in vacinas_necessarias:
                if vacina == vacina_necessaria:
                    aplicadas += 1
        if aplicadas == 3: return True 
        return False 



            
        