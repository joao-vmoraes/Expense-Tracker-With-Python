from matplotlib.pylab import normal

from controllers import AppController as AppController
from time import sleep

branco = '\033[97m'
vermelho = '\033[91m'
azul = '\033[94m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'
normal = '\033[0m'


if __name__ == '__main__':
    controlador = AppController.AppController()

    while True:
        sleep(1)
        print(f'{amarelo}======================================')
        print(f'{amarelo}====== ADMINISTRADOR FINANCEIRO ======')
        print(f'{amarelo}======================================')
        print()
        print(f"{verde}1{normal} - Adicionar Compra")
        print(f"{verde}2{normal} - Remover Compra")
        print(f"{verde}3{normal} - Atualziar Compra")
        print(f"{verde}4{normal} - Listar todas as compras")
        print(f"{verde}5{normal} - Listar todas as compras por data")
        print(f"{verde}6{normal} - Listar valor total das compras por categoria")
        print(f"{verde}7{normal} - Sair")

        escolha = int(input("Digite a opção desejada >> "))

        if escolha == 1:
            controlador.adicionar_compra()
        elif escolha == 2:
            controlador.remover_compra()
        elif escolha == 3:
            controlador.atualizar_compra()
        elif escolha == 4:
            controlador.listar_compras()
        elif escolha == 5:
            controlador.listar_compras_por_data()
        elif escolha == 6:
            controlador.listar_todas_compras_por_categoria()
        else:
            print("Dados atualizados! até mais.")
            break