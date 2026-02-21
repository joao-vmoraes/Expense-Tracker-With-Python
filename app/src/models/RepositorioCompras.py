
from models import Compra
import pymysql
import os
import dotenv

dotenv.load_dotenv()

def conectar_banco():
    return pymysql.connect(
    host= os.getenv("MYSQL_HOST"),
    user= os.getenv("MYSQL_USER"),
    password= os.getenv("MYSQL_PASSWORD"), #type: ignore
    database= os.getenv("MYSQL_DATABASE"),
    cursorclass=pymysql.cursors.DictCursor
    ) #type: ignore


class RepositorioCompras:
    def __init__(self) -> None:
        pass

    def adicionar_compra(self, compra: Compra.Compra) -> None:
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = "INSERT INTO compras (id_categoria, nome, valor) VALUES (%s, %s, %s)"
            cursor.execute(sql, (compra.id_categoria, compra.nome, compra.valor))
            conn.commit()
            cursor.close()
            conn.close()


    def listar_compras(self) -> list:
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                'SELECT  compras.nome as nome, ca.nome AS categoria, '
                'valor, data ,compras.id as id FROM compras '
                'INNER JOIN categorias ca ON compras.id_categoria = ca.id; '
            )
            cursor.execute(sql)
            cursor.close()
            conn.close()
            return cursor.fetchall() # type: ignore

    def listar_todas_compras_por_data(self, ano: int, mes: int) -> None:
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                'SELECT * FROM compras ' \
                'WHERE YEAR(data) = %s AND MONTH(data) = %s '
            ) 
            cursor.execute(sql, (ano, mes))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result # type: ignore
    
    def listar_todas_compras_por_categoria(self) -> list:
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                ' SELECT c.nome as nome, SUM(compras.valor) as total from compras '
                ' INNER JOIN categorias c ON compras.id_categoria = c.id '
                ' GROUP BY id_categoria '
                ' ORDER BY SUM(compras.valor) DESC '
            )
            cursor.execute(sql)
            result = cursor.fetchall() 
            cursor.close()
            conn.close()
            return result # type: ignore
            
    
    def remover_compra(self, id: int) -> None: 
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = "DELETE FROM compras WHERE id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            cursor.close()
            conn.close()

    def listar_compras_por_categoria_e_mes(self, ano: int, mes: int) -> list:
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                ' SELECT c.nome as nome, SUM(compras.valor) as total from compras '
                ' INNER JOIN categorias c ON compras.id_categoria = c.id '
                ' WHERE YEAR(compras.data) = %s AND MONTH(compras.data) = %s '
                ' GROUP BY compras.id_categoria '
                ' ORDER BY SUM(compras.valor) DESC '
            )
            cursor.execute(sql, (ano, mes))
            result = cursor.fetchall() 
            cursor.close()
            conn.close()
            return result # type: ignore
    
    def atualizar_compra(self, _id: int, compra: Compra.Compra) -> None: 
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                'UPDATE compras SET ' \
                'nome = %s , ' \
                'id_categoria = %s , ' \
                'valor = %s  ' \
                'WHERE id = %s'
            )
            cursor.execute(sql, (compra.nome , compra.id_categoria, compra.valor, _id))
            conn.commit()

            cursor.close()
            conn.close()
