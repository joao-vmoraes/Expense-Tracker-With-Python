import models.Compra as Compra
import models.RepositorioCompras as RepositorioCompras
import view.ComprasView as ComprasView
import models.RepositorioCategorias as RepositorioCategorias
import view.CategoriasView as CategoriasView
from utils.colors import *

class AppController:

    def __init__(self) -> None:
        self.repositorio_compras = RepositorioCompras.RepositorioCompras()
        self.view = ComprasView.ComprasView()
        self.repositorio_categorias = RepositorioCategorias.RepositorioCategorias()
        self.view_categorias = CategoriasView.CategoriasView()
    

    def adicionar_compra(self) -> None:
        try:
            compra_texto = self.view.input("Digite a nova compra (ex: 49.90 pizza de frango)\n >>  ").strip()

            categorias = self.repositorio_categorias.listar_categorias()
            self.view_categorias.exibir_categorias(categorias)
            categoria = int(self.view.input("Digite o ID da categoria da sua compra >> "))

            valor, nome = compra_texto.split(' ', 1)
            valor = float(valor)

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
            ano = int(self.view.input('>>'))
            self.view.mostrar_mensagem("Digite o mês (MM): ")
            mes = int(self.view.input('>>'))

            compras = self.repositorio_compras.listar_todas_compras_por_data(ano, mes)
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Ocorreu um erro ao listar compras por data: {e}{normal}")


    def listar_todas_compras_por_categoria(self) -> None:
        try:
            compras = self.repositorio_compras.listar_todas_compras_por_categoria()
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Ocorreu um erro ao listar compras por categoria: {e}{normal}")

    def listar_compras_por_categoria_e_mes(self) -> None:
        try:
            self.view.mostrar_mensagem("Digite o ano (YYYY): ")
            ano = int(self.view.input('>>'))
            self.view.mostrar_mensagem("Digite o mês (MM): ")
            mes = int(self.view.input('>>'))

            compras = self.repositorio_compras.listar_compras_por_categoria_e_mes(ano, mes)
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Ocorreu um erro ao listar compras por categoria e mês: {e}{normal}")


    def atualizar_compra(self):
        try:
            _id = int(self.view.input(f"{amarelo}Digite o id da compra que voce quer alterar >> {normal}"))
            compra_texto = self.view.input(f"{amarelo}Digite a nova compra (ex: 49.90 hamburguer) {normal}").strip()

            self.view_categorias.mostrar_mensagem("Categorias disponíveis:")
            categorias = self.repositorio_categorias.listar_categorias()
            self.view_categorias.exibir_categorias(categorias)

            nova_categoria = int(self.view.input(f"{amarelo}Digite o ID da nova categoria >> {normal}"))

            valor, nome = compra_texto.split(' ', 1)
            valor = float(valor)

            compra_atualizada = Compra.Compra(nova_categoria, nome, valor)
            self.repositorio_compras.atualizar_compra(_id, compra_atualizada)
            self.view.mostrar_mensagem(f"{verde}Compra atualizada com sucesso!{normal}")
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Erro ao atualizar compra: {e}{normal}")

    def remover_compra(self):
        try:
            _id = int(self.view.input('Digite o id da compra que voce quer remover >> '))
            self.repositorio_compras.remover_compra(_id)
            self.view.mostrar_mensagem(f"{verde}Compra removida com sucesso!{normal}")
        except Exception as e:
            self.view.mostrar_mensagem(f"{vermelho}Erro ao remover compra: {e}{normal}")
