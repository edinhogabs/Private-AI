import sqlite3


class BancoDados:
    def __init__(self, caminho_banco="data/rias.db"):
        self.caminho_banco = caminho_banco
        self.criar_tabela_usuarios()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela_usuarios(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                sexo TEXT NOT NULL,
                profissao TEXT NOT NULL,
                naturalidade TEXT NOT NULL,
                login TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        """)

        conexao.commit()
        conexao.close()

    def cadastrar_usuario(self, pessoa):
        try:
            conexao = self.conectar()
            cursor = conexao.cursor()

            cursor.execute("""
                INSERT INTO usuarios (nome, idade, sexo, profissao, naturalidade, login, senha)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                pessoa.nome,
                pessoa.idade,
                pessoa.sexo,
                pessoa.profissao,
                pessoa.naturalidade,
                pessoa.login,
                pessoa.senha
            ))

            conexao.commit()
            return True

        except sqlite3.IntegrityError:
            return False

        finally:
            conexao.close()

    def buscar_usuario_por_login(self, login):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT nome, idade, sexo, profissao, naturalidade, login, senha
            FROM usuarios
            WHERE login = ?
        """, (login,))

        usuario = cursor.fetchone()
        conexao.close()
        return usuario

    def autenticar_usuario(self, login, senha):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT nome, idade, sexo, profissao, naturalidade, login, senha
            FROM usuarios
            WHERE login = ? AND senha = ?
        """, (login, senha))

        usuario = cursor.fetchone()
        conexao.close()
        return usuario