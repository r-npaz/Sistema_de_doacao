

class PessoasCadastradas:
    def __init__(self, pessoa: Pessoa):
        self.__pessoa = None
        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        self.__cadastrados = []

    @property
    def cadastrados(self) -> list:
        return self.__cadastrados
    
    @cadastrar_pessoa.setter
    def cadastrar_pessoa(self):
        if isinstance(pessoa, Pessoa):
            self.__cadastrados.append(pessoa)



    