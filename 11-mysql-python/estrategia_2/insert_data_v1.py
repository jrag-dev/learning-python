"""
    El siguiente codigo realiza la inserción de un nuevo libro (book) en la tabla books
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(title, isbn):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    query = "INSERT INTO books (title, isbn) VALUES(%s, %s)"
    args = (title, isbn)

    try:
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last inset id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def main():
    insert_book('A Sudden Light', '1234567891234')


if __name__ == '__main__':
    main()