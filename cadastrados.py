

class PessoasCadastradas:
    def __init__(self, pessoa: Pessoa):
        self.__pessoa = None
        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        self.__cadastrados = []

    @property
    def lista_cadastrados(self) -> list:
        return self.__cadastrados
    
    def buscar_cadastrado(self, cpf: str):
        for pessoa in self.__cadastrados:
            if pessoa.cpf == cpf:
                return pessoa
        print('Cadastro não encontrada')
        return None

    def cadastrar_pessoa (self):
        if isinstance(pessoa, Pessoa):
            self.__cadastrados.append(pessoa)
            #verificar se a pessoa já está na lista antes de cadastrar, para evitar cadastros duplos. 
    