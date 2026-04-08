class Pessoa:
    def __init__(self, nome, idade, sexo, profissao, naturalidade, login, senha, id=None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.profissao = profissao
        self.naturalidade = naturalidade
        self.login = login
        self.senha = senha
        self.id = id

    def mostrar_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Sexo: {self.sexo}\n"
            f"Profissão: {self.profissao}\n"
            f"Naturalidade: {self.naturalidade}\n"
            f"Login: {self.login}"
        )