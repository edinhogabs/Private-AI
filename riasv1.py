class Pessoa:
    def __init__(self, nome, idade, sexo, profissao, naturalidade, login, senha):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.profissao = profissao
        self.naturalidade = naturalidade
        self.login = login
        self.senha = senha

    def apresentar_dados(self):
        return (
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Sexo: {self.sexo}\n"
            f"Profissão: {self.profissao}\n"
            f"Naturalidade: {self.naturalidade}"
        )


class SistemaLogin:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self):
        print("\n=== CADASTRO DE USUÁRIO ===")
        nome = input("Nome: ").strip()
        idade = int(input("Idade: "))
        sexo = input("Sexo: ").strip()
        profissao = input("Profissão: ").strip()
        naturalidade = input("Naturalidade: ").strip()
        login = input("Crie um login: ").strip()
        senha = input("Crie uma senha: ").strip()

        usuario_existente = self.buscar_usuario(login)
        if usuario_existente is not None:
            print("Esse login já existe.")
            return None

        novo_usuario = Pessoa(nome, idade, sexo, profissao, naturalidade, login, senha)
        self.usuarios.append(novo_usuario)
        print("\nUsuário cadastrado com sucesso!\n")
        return novo_usuario

    def buscar_usuario(self, login):
        for usuario in self.usuarios:
            if usuario.login == login:
                return usuario
        return None

    def autenticar(self):
        print("\n=== LOGIN ===")
        login = input("Login: ").strip()
        senha = input("Senha: ").strip()

        usuario = self.buscar_usuario(login)

        if usuario is not None and usuario.senha == senha:
            print("Login realizado com sucesso!")
            return usuario

        print("Login ou senha inválidos.")
        return None


class RIAS:
    def __init__(self, usuario):
        self.usuario = usuario

    def saudar_usuario(self):
        return f"Olá, {self.usuario.nome}! Eu sou a RIAS, sua assistente virtual."

    def mostrar_ajuda(self):
        return (
            "\nComandos disponíveis:\n"
            "1 - ajuda\n"
            "2 - meu nome\n"
            "3 - minha idade\n"
            "4 - meus dados\n"
            "5 - sair\n"
        )

    def interpretar_comando(self, comando):
        comando = int(comando)

        if comando == 1:
            return f'\n{self.mostrar_ajuda()}\n'
        elif comando == 2:
            return f"\nSeu nome é {self.usuario.nome}.\n"
        elif comando == 3:
            return f"\nVocê tem {self.usuario.idade} anos.\n"
        elif comando == 4:
            return f'\n{self.usuario.apresentar_dados()}\n'
        elif comando == 5:
            return None
        else:
            return "Comando não reconhecido. Digite 'ajuda' para ver as opções."

    def iniciar(self):
        print("\n=== RIAS INICIADA ===")
        print(self.saudar_usuario())

        while True:
            print("\n=== Comandos Disponíveis ===\n")
            print("1 - ajuda")
            print("2 - meu nome")
            print("3 - minha idade")
            print("4 - meus dados")
            print("5 - sair")
            comando = input("\nDigite um comando: \n")
            resposta = self.interpretar_comando(comando)

            if resposta is None:
                print("Encerrando a RIAS...")
                break

            print(resposta)


def menu_principal():
    sistema = SistemaLogin()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                sistema.cadastrar_usuario()

            elif opcao == 2:
                usuario = sistema.autenticar()
                if usuario is not None:
                    assistente = RIAS(usuario)
                    assistente.iniciar()

            elif opcao == 3:
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números válidos.")


menu_principal()