from utils.colors import *


class CategoriasView:
    def __init__(self) -> None:
        ...
    
    @staticmethod
    def exibir_categorias(categorias):
        for row in categorias:
            _id = row['id']
            nome = row['nome']
            print(f"ID: {azul}{_id}{normal} - Nome: {nome}")
    
    @staticmethod
    def mostrar_mensagem(msg):
        print(msg)

    @staticmethod
    def input(msg):
        return input(f'{amarelo}{msg}{normal}')