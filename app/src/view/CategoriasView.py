branco = '\033[97m'
vermelho = '\033[91m'
azul = '\033[94m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'
normal = '\033[0m'


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