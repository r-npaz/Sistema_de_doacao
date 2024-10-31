from adotante import Adotante
from telaAdotante import TelaAdotante
from controleMovimentacao import ControleMovimentacao


class ControleAdotante:
    def __init__(self) -> None:
        self.__tela_adotante = TelaAdotante(self)
        self.__adotantes = []

    def cadastrar_adotante(self, tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco):        
        adotante = Adotante(tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco)
        self.__adotantes.append(adotante)
        #estou jogando essas informações para uma classe que irá guardar todos os cadastros. Posso add um referencia (bool) para diferenciar um adotante de um doador. 
    
    def buscar_adotante(self, cpf: str) -> Adotante:
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None
        
    def alterar_adotante(self):
        pass

    def excluir_adoante(self):
        pass
    
    def adotar_animal(self):
        #avalia se todos os critérios para adoção foram respeitados
        pass

        #um getter, por definição, pode receber algum parametro?
    def idade_atual(self, data_nascimento: str) -> int:
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade

    
    def abre_tela_adotante(self):
        while True:
            self.__tela_adotante.mostrar_tela_cadastro()