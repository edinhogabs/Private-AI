from services.sistema_login import SistemaLogin
from services.rias import RIAS


def main():
    sistema_login = SistemaLogin()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                sistema_login.cadastrar_usuario()

            elif opcao == 2:
                usuario = sistema_login.autenticar()

                if usuario is not None:
                    assistente = RIAS(usuario, sistema_login)
                    assistente.iniciar()

            elif opcao == 3:
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite apenas números válidos.")


if __name__ == "__main__":
    main()