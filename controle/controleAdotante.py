from entidade.adotante import Adotante
from entidade.adotante import TipoHabitacao
from limite.telaAdotante import TelaAdotante
from datetime import datetime


class ControleAdotante:
    def __init__(self) -> None:
        self.__tela_adotante = TelaAdotante()
        self.__adotantes = []

    def cadastrar_adotante(self):
        cadastrar_adotante = self.abre_tela_adotante()
        tipo_habitacao = TipoHabitacao(cadastrar_adotante[0])
        tem_animais = True if cadastrar_adotante[1] == 'S' else False  
        novo_adotante = Adotante(tipo_habitacao, tem_animais, cadastrar_adotante[2], 
                                 cadastrar_adotante[3], cadastrar_adotante[4], cadastrar_adotante[5])
        
        if self.buscar_adotante(novo_adotante.cpf) is not None:
            print('Essa pessoa já tem cadastro')
            return None
        
        self.__adotantes.append(novo_adotante)
        print(f"Adotante {novo_adotante.nome} cadastrado com sucesso!")
        return novo_adotante

    def buscar_adotante(self, cpf: str) -> Adotante:
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None
    
    @property
    def listar_adotantes(self) -> list:
        return self.__adotantes

    def excluir_adoante(self, cpf: str):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                self.__adotantes.remove(adotante)
                return f'Adotante: {adotante.cpf} - {adotante.nome} removido!' 
        return False 

    def assinar_termo_responsabilidade(self, cpf: str):
        adotante = self.buscar_adotante(cpf)
        if adotante:
            termo = self.__tela_adotante.termo_adocao()
            adotante.assinar_termo_responsabilidade(termo)
            return True
        return False

    def termo_responsabilidade(self, cpf: str):
        adotante = self.buscar_adotante(cpf)
        if adotante:
            return adotante.termo_responsabilidade()
    
    
    def data_adocao(self, cpf:str):
        adotante = self.buscar_adotante(cpf)
        if adotante:
            return adotante.data_assinatura()
    
    def idade_atual(self, data_nascimento: str) -> int:
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year
        if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
            idade -= 1
        return idade

    def tela_termo(self):
        termo = self.__tela_adotante.termo_adocao()
        return termo

    def abre_tela_adotante(self):
        adotante = self.__tela_adotante.mostrar_tela_cadastro()
        print(adotante)
        return adotante
    

