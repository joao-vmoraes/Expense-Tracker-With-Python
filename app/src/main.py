from models import Categoria
from models import Compra
from models import Repositorio_compras


r1 = Repositorio_compras.RepositorioCompras()
r1.adicionar_compra(Compra.Compra(3, 'Video game', 200.00))
r1.listar_compras()