from services.gerenciador_atividades import GerenciadorAtividades

class RIAS:
    def __init__(self, usuario, sistema_login):
        self.usuario = usuario
        self.sistema_login = sistema_login
        self.ativa = True
        self.gerenciador_atividades = GerenciadorAtividades()

    def saudar_usuario(self):
        if self.usuario.nome == "Eder Gabriel Batista Gonzaga":
            return f"Olá, {self.usuario.nome}! Eu sou a RIAS, o que deseja hoje?"
        else:
            return f"Olá, {self.usuario.nome}! Eu sou a RIAS, assistente virtual do Eder."

    def mostrar_ajuda(self):
        return (
            "\n=== COMANDOS DISPONÍVEIS ===\n"
            "1 - Meus Dados\n"
            "2 - Alterar Senha do Login\n"
            "3 - Criar Atividade\n"
            "4 - minha naturalidade\n"
            "5 - Encerrar Sessão\n"
        )

    def interpretar_comando(self, comando):
        try:
            comando = int(comando)
        except:
            return "Digite somente o número do comando."

        if comando == 1:
            return f"Seus dados são:\n{self.usuario.mostrar_dados()}."

        elif comando == 2:
            self.sistema_login.alterar_senha(self.usuario)
            return "Operação Finalizada"

        elif comando == 3:
            self.criar_atividade()
            return "Operação Finalizada"

        elif comando == 4:
            return f"Você é natural de {self.usuario.naturalidade}."

        elif comando == 5:
            self.ativa = False
            return "Encerrando atendimento da RIAS..."

        else:
            return "Comando não reconhecido. Digite 'ajuda' para ver os comandos disponíveis."

    def iniciar(self):
        print("\n=== RIAS INICIADA ===")
        print(self.saudar_usuario())
        print(self.mostrar_ajuda())

        while self.ativa:
            comando = input("\nDigite um comando para a RIAS: \n")
            resposta = self.interpretar_comando(comando)
            print(resposta)

    def criar_atividade(self):
        print("\n=== CRIAR ATIVIDADE ===")
        titulo = input("Título da atividade: ").strip()
        descricao = input("Descrição da atividade: ").strip()
        prioridade = input("Prioridade (baixa/media/alta): ").strip().lower()

        if not titulo:
            print("O título não pode ficar vazio.")
            return

        if prioridade not in ["baixa", "media", "alta"]:
            print("Prioridade inválida.")
            return

        atividade = self.gerenciador_atividades.criar_atividade(
            self.usuario.id,
            titulo,
            descricao,
            prioridade
        )

        print(f"Atividade criada com sucesso! ID: {atividade.id}")

