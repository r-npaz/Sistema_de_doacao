from pessoa import Pessoa


class Doador(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str):
        super().__init__(nome, cpf, data_nascimento, endereco)

    def registrar_doacao(self):
        pass

    def historico_doacoes(self) -> list:
        pass
    
