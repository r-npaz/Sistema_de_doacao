from entidade.gato import Gato
from limite.telaGato import TelaGato


class ControleGato:
    def __init__(self) -> None:
        self.__tela_gato = TelaGato()
        self.__gatos = []
        self.__vacinas_aplicadas = []

    def cadastrar_gato(self):
        numero_chip, nome, raca, vacina_aplicada, data_aplicacao = self.__tela_gato.cadastrar_gato()
        novo_gato = Gato(numero_chip, nome, raca, vacina_aplicada, data_aplicacao)
        
        if self.buscar_gato(novo_gato.numero_chip) is not None:
            print('ALERTA: Esse gato já foi cadastrado!')
            return novo_gato
        
        self.__gatos.append(novo_gato)
        print(f'Gato {novo_gato.nome} cadastrado!')
        return novo_gato
    
    def listar_gatos(self) -> str:
        return self.__gatos

    def buscar_gato(self, numero_chip: str) -> Gato:
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                return gato
            return None

    def remover_gato(self, numero_chip: str):
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                self.__gatos.remove(gato)
                print('Gato removido da lista de adoção')
        
    def vacinar(self, numero_chip, vacina, data_aplicacao):
        vacina_tomada = Gato.aplicar_vacina_gato(numero_chip, vacina, data_aplicacao)
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
