

from app.src.models.Categoria import categoria


class ComprasView:
    def __init__(self):
        pass

    @staticmethod
    def exibir_compras(compras):
        for row in compras:
            print(row)

    @staticmethod
    def exibir_categoria(categorias):
        for row in categorias:
            _id, nome = row
            print(f"ID: {_id} - Nome: {nome}")
    
    @staticmethod
    def mostrar_mensagem(msg):
        print(msg)