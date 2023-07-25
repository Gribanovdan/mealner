import psycopg2 as pg
import psycopg2.extensions

import scripts.config.env_loader as el
import scripts.logs.log_manager as lg
import os


class DBInfo:
    connection: psycopg2.extensions.connection = None

    el.load_env()
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    db = os.environ.get('POSTGRES_DB')
    host = 'localhost'
    port = '8080'


def launch():
    if DBInfo.connection is not None:
        lg.log('DB connection already exists', 30)
        return
    try:
        conn = pg.connect(
            database=DBInfo.db,
            user=DBInfo.user,
            password=DBInfo.password,
            host=DBInfo.host,
            port=DBInfo.port
        )
        cursor = conn.cursor()

    except Exception as err:
        lg.log(str(err), 40)
        return

    DBInfo.connection = conn
    lg.log('DB launched successfully!', 20)