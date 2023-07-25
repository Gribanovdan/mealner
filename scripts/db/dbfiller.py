import psycopg2 as pg
from psycopg2 import extensions
import scripts.logs.log_manager as lg
import scripts.db.dblauncher as db
import scripts.entities.main_entities as ent


def create_schema(name: str):
    db.launch()
    conn = db.DBInfo.connection
    cur = conn.cursor()

    try:
        cur.execute('create schema if not exists main;')
        conn.commit()
    except Exception as err:
        lg.log(str(err), 40)
        return None


def create_table(name: str, atr: list[(str, str)]):
    db.launch()
    conn = db.DBInfo.connection
    cur = conn.cursor()

    create_schema('main')

    q = f'create table if not exists main.{name} ('
    i = 0
    for at, cl in atr:
        q += f'{at} {cl}'
        i += 1
        if i != len(atr):
            q += ',\n'
        else:
            q += ');'

    try:
        cur.execute(q)
        conn.commit()
    except Exception as err:
        lg.log(str(err), 40)
        return None
    lg.log(f'table main.{name} created', 20)
    return True


# TODO принимают специальную сущность - блюдо, продукт или набор продуктов
def insert_dish():
    # TODO
    pass


def insert_product(product: ent):
    code = None
    # TODO проверка на совпадение имени в бд

    db.launch()
    conn = db.DBInfo.connection
    cursor = conn.cursor()

    # TODO создать таблицу если нету
    atr = [
        ('id', 'int primary key'),
        ('name', 'varchar(63)'),
        ('price', 'serial'),
        ('kkalories', 'serial'),
        ('protein', 'real'),
        ('fats', 'real'),
        ('carbohydrates', 'real'),
        ('measure', 'varchar(15)')
    ]
    code = create_table('product', atr)

    # TODO найти первый не занятый айди

    find_ind_q = f'select max(id) from main.product;'
    try:
        cursor.execute(find_ind_q)
        res = cursor.fetchall()[0]
        if res[0] is not None:
            id = int(res[0]) + 1
        else:
            id = 0
    except Exception as err:
        lg.log(str(err), 40)
        return None

    lg.log(f'id for new product will be: {id}', 20)

    q = f'insert into main.product values\n'

    q += f"({id}, '{product.name}', {product.cost}, {product.kkalories}, {product.protein}, {product.fats}, {product.carbohydrates}, '{str(product.measure)}');"

    try:
        cursor.execute(q)
    except Exception as err:
        lg.log(str(err), 40)
        return None
    conn.commit()
    return code


def insert(conn: extensions.connection):
    print('wtf')
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
