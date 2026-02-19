from models import Compra
import pymysql
import os
import dotenv
import cryptography

dotenv.load_dotenv()

def conectar_banco():
    conn = pymysql.connect(
    host= os.getenv("MYSQL_HOST"),
    user= os.getenv("MYSQL_USER"),
    password= os.getenv("MYSQL_PASSWORD"), #type: ignore
    database= os.getenv("MYSQL_DATABASE"),
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
    ) #type: ignore
    return conn

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

    def listar_compras(self) -> None:
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                'SELECT * FROM compras '
            )
            cursor.execute(sql)
            for row in cursor.fetchall():
                print(row)
            cursor.close()
            conn.close()
    
    def remover_compra(self, id: int) -> None: 
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = "DELETE FROM compras WHERE id = %s"
            cursor.execute(sql, (id,))
            conn.commit()
            cursor.close()
            conn.close()
    
    def atualizar_compra(self, _id: int, compra: Compra.Compra) -> None: 
        conn = conectar_banco()
        with conn.cursor() as cursor:
            sql = (
                'UPDATE compras SET ' \
                'nome = %s ' \
                'id_categoria = %s ' \
                'valor = %s ' \
                f'WHERE id = {_id}'
            )
            cursor.execute(sql, (compra.nome , compra.id_categoria, compra.valor))
            conn.commit()

            cursor.close()
            conn.close()
