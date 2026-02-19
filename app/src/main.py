from models import Categoria
from models import Compra
from models import Repositorio_compras

c1 = Compra.Compra(1, 'Suco', 2.5)
r1 = Repositorio_compras.RepositorioCompras()
r1.adicionar_compra(c1)
r1.listar_compras()