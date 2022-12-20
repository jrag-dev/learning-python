from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def create_table():
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    try:
        studentRecord = """
        CREATE TABLE student (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(20) NOT NULL,
            branch VARCHAR(50),
            roll INT NOT NULL,
            section VARCHAR(5),
            age INT)
        """
        cursor.execute(studentRecord)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    create_table()