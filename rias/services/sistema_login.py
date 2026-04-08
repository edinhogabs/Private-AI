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
        
        
    def alterar_senha(self, usuario):
        print("\n=== ALTERAÇÃO DE SENHA ===")
        senha_atual = input("Digite sua senha atual: ").strip()

        if senha_atual != usuario.senha:
            print("Senha atual incorreta.")
            return False

        nova_senha = input("Digite a nova senha: ").strip()
        confirmar_senha = input("Confirme a nova senha: ").strip()

        if nova_senha != confirmar_senha:
            print("As senhas não coincidem.")
            return False

        if len(nova_senha) < 4:
            print("A nova senha deve ter pelo menos 4 caracteres.")
            return False

        sucesso = self.banco.atualizar_senha(usuario.login, nova_senha)

        if sucesso:
            usuario.senha = nova_senha
            print("Senha alterada com sucesso!")
            return True

        print("Não foi possível alterar a senha.")
        return False