import psycopg2 as pg
from psycopg2 import extensions
import scripts.logs.log_manager as lg


# TODO принимают специальную сущность - блюдо, продукт или набор продуктов
def insert_dish():
    # TODO
    pass


def insert_product():
    # TODO
    pass


def insert(conn: extensions.connection):
    try:
        cursor = conn.cursor()
        cursor.execute('create schema if not exists main;')
        cursor.execute('create table main.test1 (id int, cost int);')
        cursor.execute('insert into main.test1 (id, cost) values (1, 100), (2, 200);')
        cursor.execute('select * from main.test1')
        res = cursor.fetchall()
        conn.commit()
    except Exception as err:
        lg.log(str(err), 40)
        return

