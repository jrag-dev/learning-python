"""
    fetchmany se usa cuando el número de filas es relativamente grande, debido a
    que permite un mejor manejo de la memoria utilizada para traer todos los registros
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break

        for row in rows:
            yield row


def select_data_fetchmany():
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    query = "SELECT * FROM student"

    try:
        cursor.execute(query)

        for row in iter_row(cursor, 10):
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    select_data_fetchmany()