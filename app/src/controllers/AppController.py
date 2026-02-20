import models.Compra as Compra
import models.RepositorioCompras as RepositorioCompras
import view.ComprasView as ComprasView
import models.RepositorioCategorias as RepositorioCategorias
import view.CategoriasView as CategoriasView

branco = '\033[97m'
vermelho = '\033[91m'
azul = '\033[94m'
verde = '\033[92m'
amarelo = '\033[93m'
ciano = '\033[96m'
normal = '\033[0m'

class AppController:

    def __init__(self) -> None:
        self.repositorio_compras = RepositorioCompras.RepositorioCompras()
        self.view = ComprasView.ComprasView()
        self.repositorio_categorias = RepositorioCategorias.RepositorioCategorias()
        self.view_categorias = CategoriasView.CategoriasView()

    def adicionar_compra(self) -> None:
        try:
            compra_texto = input("Digite a nova compra (ex: 49.90 hamburguer) ").strip()
            categorias = self.repositorio_categorias.listar_categorias()
            self.view_categorias.exibir_categorias(categorias)
            categoria = int(input("Digite o ID da categoria da sua compra >> "))

            limite = compra_texto.find(' ')
            valor = float(compra_texto[:limite])
            nome = compra_texto[limite + 1:]

            compra = Compra.Compra(categoria, nome, valor)
            self.repositorio_compras.adicionar_compra(compra)
            self.view.mostrar_mensagem(f"{verde}Compra adicionada com sucesso!{normal}")
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Erro ao adicionar compra: {e}{normal}")

    def listar_compras(self) -> None:
        try:
            compras = self.repositorio_compras.listar_compras()
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Ocorreu um erro ao listar compras: {e}{normal}")

    def listar_compras_por_data(self) -> None:
        try:
            self.view.mostrar_mensagem("Digite o ano (YYYY): ")
            ano = int(input('>>'))
            self.view.mostrar_mensagem("Digite o mês (MM): ")
            mes = int(input('>>'))

            compras = self.repositorio_compras.listar_todas_compras_por_data(ano, mes)
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro ao listar compras por data: {e}")


    def listar_todas_compras_por_categoria(self) -> None:
        try:
            compras = self.repositorio_compras.listar_todas_compras_por_categoria()
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro ao listar compras por categoria: {e}")
    

    def atualizar_compra(self):
        try:
            _id = int(input('Digite o id da compra que voce quer alterar >> '))
            compra = input("Digite a nova compra (ex: 49.90 hamburguer) ").strip()
            self.view_categorias.mostrar_mensagem("Categorias disponíveis:")
            categorias = self.repositorio_categorias.listar_categorias()
            self.view_categorias.exibir_categorias(categorias)

            nova_categoria = int(input("Digite o ID da nova categoria >> "))

            limite = compra.find(' ')
            valor = float(compra[:limite])
            nome = compra[limite + 1:]

            compra_atualizada = Compra.Compra(nova_categoria, nome, valor)
            self.repositorio_compras.atualizar_compra(_id, compra_atualizada)
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao atualizar compra: {e}")

    def remover_compra(self):
        try:
            _id = int(input('Digite o id da compra que voce quer remover >> '))
            self.repositorio_compras.remover_compra(_id)
            self.view.mostrar_mensagem("Compra removida com sucesso!")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao remover compra: {e}")
