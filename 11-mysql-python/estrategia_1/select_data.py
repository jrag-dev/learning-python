from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def select_data():
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    query = "SELECT id, name, branch, age FROM student"

    try:
        cursor.execute(query)

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    select_data()