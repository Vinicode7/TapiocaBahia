class Cardapio:
    def __init__(self, id, descricao, preco:float):
        self.id = id
        self.descricao = descricao
        self.preco = preco

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "preco": self.preco,
        }