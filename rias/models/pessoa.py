class Pessoa:
    def __init__(self, nome, idade, sexo, profissao, naturalidade, login, senha):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.profissao = profissao
        self.naturalidade = naturalidade
        self.login = login
        self.senha = senha

    def apresentar(self):
        if self.login == 'eder.gonzaga':
            return f"Olá, {self.nome}! Me chamo RIAS, o que deseja hoje?."
        else:
            return f'Olá, {self.nome}! Me chamo RIAS, sou a assistente virtual do Eder.'
        
        
    def mostrar_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Sexo: {self.sexo}\n"
            f"Profissão: {self.profissao}\n"
            f"Naturalidade: {self.naturalidade}\n"
            f"Login: {self.login}"
        )