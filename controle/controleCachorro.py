from entidade.cachorro import Cachorro
from entidade.cachorro import PorteCachorro
from limite.telaCachorro import TelaCachorro


class ControleCachorro:
    def __init__(self) -> None:
        self.__tela_cachorro = TelaCachorro()
        self.__cadastro_cachorros = []
        self.__vacinas_aplicadas = []
        
    def cadastrar_cachorro(self):
        porte, numero_chip, nome, raca, vacinas = self.__tela_cachorro.cadastrar_cachorro()
        porte_cachorro = PorteCachorro(porte)
        cachorro = Cachorro(porte_cachorro, numero_chip, nome, raca)
        if vacinas is not None and len(vacinas) > 0:
            for vacina, data in vacinas.items(): 
                self.vacinar(cachorro, vacina, data)
        
        if self.buscar_cachorro(cachorro.numero_chip) is not None:
            print(f'ALERTA! O cachorro {cachorro.nome} já foi cadastrado uma vez')
            return cachorro
        self.__cadastro_cachorros.append(cachorro)
        print(f'Cachorro {cachorro.nome} cadastrado')
        return cachorro

    def buscar_cachorro(self, numero_chip: str) -> Cachorro:
        for cachorro in self.__cadastro_cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
        return None
        
    def remover_cachorro(self, numero_chip: str):
        for cachorro in self.__cadastro_cachorros:
            if cachorro.numero_chip == numero_chip:
                self.__cadastro_cachorros.remove(cachorro)
                print('Cachorro removido da lista de adoção')
    
    def listar_cachorros(self) -> str:
        return self.__cadastro_cachorros

    def vacinar(self, cachorro: Cachorro, vacina, data_aplicacao):
        vacina_tomada = Cachorro.aplicar_vacina(cachorro, vacina, data_aplicacao)
        self.__vacinas_aplicadas.append(vacina_tomada)

    def historico_vacina(self, numero_chip: str) -> list:
        vacinas = [vacina for vacina in self.__vacinas_aplicadas if vacina.cachorro.numero_chip == numero_chip]
        return vacinas

    def verificar_vacinas(self):
        vacinas_necessarias = ['VacinasNecessarias.raiva', 'VacinasNecessarias.leptospirose', 'VacinasNecessarias.hepatite_infecciosa']
        vacinas = self.historico_vacina()
        aplicadas = 0
        for vacina in vacinas:
            for vacina_necessaria in vacinas_necessarias:
                if vacina == vacina_necessaria:
                    aplicadas += 1
        if aplicadas >= 3: return True 
        return False 



            
        