from utils.colors import *

class ComprasView:
    def __init__(self):
        pass

    @staticmethod
    def exibir_compras(compras):
        for row in compras:
            for key, value in row.items():
                print(f"{key}: {verde}{value}{normal} | ", end="")
            print() # newline after each row

    
    @staticmethod
    def mostrar_mensagem(msg):
        print(msg)

    @staticmethod
    def input(msg):
        return input(f'{amarelo}{msg}{normal}')