from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def query_with_fetchall():
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM books")
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
    query_with_fetchall()
