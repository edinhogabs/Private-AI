from database.banco import BancoDados
from models.atividade import Atividade


class GerenciadorAtividades:
    def __init__(self):
        self.banco = BancoDados()

    def criar_atividade(self, usuario_id, titulo, descricao, prioridade):
        atividade = Atividade(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade,
            usuario_id=usuario_id
        )

        self.banco.cadastrar_atividade(atividade)
        return atividade