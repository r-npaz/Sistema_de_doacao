from adotante import Adotante
from telaAdotante import TelaAdotante
from controleMovimentacao import ControleMovimentacao


class ControleAdotante:
    def __init__(self) -> None:
        self.__tela_adotante = TelaAdotante(self)
        self.__adotantes = []

    def cadastrar_adotante(self, tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco):  
        #na hora que eu passo essa lista, estando na ordem correta, os paramentros serão associados?       
        novo_adotante = Adotante(tipo_habitacao, tem_animais, nome, cpf, data_nascimento, endereco)
        if self.buscar_adotante(novo_adotante.cpf):
            return 'Essa pessoa já tem cadastro'
        self.__adotantes.append(novo_adotante)
        return 'Cadastro realizado com sucesso!'
    
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