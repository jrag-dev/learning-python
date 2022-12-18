"""
    Actualizar data en una tabla
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def update_book(book_id, title):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    # Se usa %s para evitar injection SQL!!
    query = "UPDATE books SET title = %s WHERE id = %s"
    data = (title, book_id)

    try:
        cursor.execute(query, data)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    update_book(85, "Janetsys Paola Rodriguez Astudillo")