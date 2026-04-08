class Atividade:
    def __init__(self, titulo, descricao, prioridade, usuario_id, status="pendente", id=None):
        self.id = id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status