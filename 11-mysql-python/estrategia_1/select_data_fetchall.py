"""
    Se usa si el número de filas en la tabla es pequeño
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def select_data_fetchall():
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    query = "SELECT * FROM student"

    try:
        cursor.execute(query)
        rows = cursor.fetchall()

        print("Total Row(s): ", cursor.rowcount)

        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    select_data_fetchall()