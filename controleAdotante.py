from adotante import Adotante
from telaAdotante import TelaAdotante
from controleMovimentacao import ControleMovimentacao
from datetime import datetime


class ControleAdotante:
    def __init__(self) -> None:
        self.__tela_adotante = TelaAdotante(self)
        self.__adotante = Adotante(self)
        self.__adotantes = []

    def cadastrar_adotante(self): 
        cadastrar_adotante = self.abre_tela_adotante
        #na hora que eu passo essa lista, estando na ordem correta, os paramentros serão associados?       
        novo_adotante = Adotante(cadastrar_adotante)
        if self.buscar_adotante(novo_adotante.cpf):
            return 'Essa pessoa já tem cadastro'
        self.__adotantes.append(novo_adotante)
        return 'Cadastro realizado com sucesso!'

    def buscar_adotante(self, cpf: str) -> Adotante:
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None

    def excluir_adoante(self, cpf: str):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                self.__adotantes.pop(adotante)
                return f'Adotante: {adotante.cpf} - {adotante.nome} removido!' 
        return False 

    def assinar_termo_responsabilidade(self, cpf):
        adotante = self.buscar_adotante(cpf)
        if adotante:
            adotante.assinar_termo_responsabilidade()
            print('Termo assinado')
        else:
            print('Adotante não localizado')

    def termo_responsabilidade(self) -> bool:
        return self.__adotante.termo_responsabilidade()
    
    def data_adocao(self) -> str:
        return self.__adotante.data_assinatura
    
        #um getter, por definição, pode receber algum parametro?
    def idade_atual(self, data_nascimento: str) -> int:
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade
    
    def abre_tela_adotante(self):
        adotante = self.__tela_adotante.mostrar_tela_cadastro()
        return adotante
