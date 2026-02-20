import models.Compra as Compra
import models.RepositorioCompras as RepositorioCompras
import view.ComprasView as ComprasView

class ComprasController:

    def __init__(self) -> None:
        self.repositorio = RepositorioCompras.RepositorioCompras()
        self.view = ComprasView.ComprasView()

    def adicionar_compra(self, id_categoria: int, nome: str, valor: float) -> None:
        try:
            compra = Compra.Compra(id_categoria, nome, valor)
            self.repositorio.adicionar_compra(compra)
            self.view.mostrar_mensagem("Compra adicionada com sucesso!")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao adicionar compra: {e}")

    def listar_compras(self) -> None:
        try:
            compras = self.repositorio.listar_compras()
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro ao listar compras: {e}")

    def listar_compras_por_data(self) -> None:
        try:
            self.view.mostrar_mensagem("Digite o ano (YYYY): ")
            ano = int(input('>>'))
            self.view.mostrar_mensagem("Digite o mês (MM): ")
            mes = int(input('>>'))

            compras = self.repositorio.listar_todas_compras_por_data(ano, mes)
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro ao listar compras por data: {e}")

    def listar_todas_compras_por_categoria(self) -> None:
        try:
            compras = self.repositorio.listar_todas_compras_por_categoria()
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro ao listar compras por categoria: {e}")
    
    def listar_compras_por_categoria(self) -> None:
        try:
            compras = self.repositorio.listar_todas_compras_por_categoria()
            self.view.exibir_compras(compras)
        except Exception as e:
            self.view.mostrar_mensagem(f"Ocorreu um erro ao listar compras por categoria: {e}")

    # def atualizar_compra(self):
    #     try:
    #         _id = int(input('Digite o id da compra que voce quer alterar >> '))
    #         compra = input("Digite a nova compra (ex: 49.90 hamburguer) ").strip()
    #         limite = compra.find(' ')
    #         valor = float(compra[:limite])
    #         nome = compra[limite + 1:]
    #         self.repositorio.atualizar_compra(_id, Compra.Compra())
    #     except Exception as e:
    #         self.view.mostrar_mensagem(f"Erro ao atualizar compra: {e}")

