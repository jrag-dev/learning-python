"""
    Insertando data en la base de datos
"""

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_data(data):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    query = "INSERT INTO student(name, branch, roll, section, age) VALUES (%s, %s, %s, %s, %s)"

    try:
        cursor.execute(query, data)

        if cursor.lastrowid:
            print("last insert id", cursor.lastrowid)
        else:
            print("last insert id not found")

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def main():
    datos = ("José alvarado", "CSE", "85", "A", "21")
    insert_data(datos)


if __name__ == '__main__':
    main()