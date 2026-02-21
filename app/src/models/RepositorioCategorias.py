from models import RepositorioCompras

class RepositorioCategorias:
    def __init__(self):
        pass

    def listar_categorias(self) -> list:
        conn = RepositorioCompras.conectar_banco()
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM categorias'
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result # type: ignore