import datetime

class Compra:
    def __init__(self,
        id_categoria: int, #type: ignore
        nome: str,
        valor: float,
        data: datetime.datetime| None= None,
        _id: int|None = None) -> None:

        self.id = _id
        self.id_categoria = id_categoria
        self.nome = nome
        self.valor = valor
        self.data = data