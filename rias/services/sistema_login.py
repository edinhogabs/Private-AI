from models.pessoa import Pessoa
from database.banco import BancoDados


class SistemaLogin:
    def __init__(self):
        self.banco = BancoDados()

    def cadastrar_usuario(self):
        print("\n=== CADASTRO ===")
        nome = input("Nome: ").strip()
        idade = int(input("Idade: "))
        sexo = input("Sexo: ").strip()
        profissao = input("Profissão: ").strip()
        naturalidade = input("Naturalidade: ").strip()
        login = input("Crie um login: ").strip()
        senha = input("Crie uma senha: ").strip()

        pessoa = Pessoa(nome, idade, sexo, profissao, naturalidade, login, senha)

        sucesso = self.banco.cadastrar_usuario(pessoa)

        if sucesso:
            print("\nUsuário cadastrado com sucesso!\n")
            return pessoa
        else:
            print("\nEsse login já existe.\n")
            return None

    def autenticar(self):
        print("\n=== LOGIN ===")
        login = input("Login: ").strip()
        senha = input("Senha: ").strip()

        dados_usuario = self.banco.autenticar_usuario(login, senha)

        if dados_usuario:
            pessoa = Pessoa(*dados_usuario)
            print("\nLogin realizado com sucesso!\n")
            return pessoa
        else:
            print("\nLogin ou senha inválidos.\n")
            return None