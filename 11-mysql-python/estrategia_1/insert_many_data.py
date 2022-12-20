from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_many_data(students):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()

    query = "INSERT INTO student (name, branch, roll, section, age) VALUES (%s, %s, %s, %s, %s)"

    try:
        cursor.executemany(query, students)

        conn.commit()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def main():
    students = [
        ("Nikhil", "CSE", "98", "A", "18"),
        ("Nisha", "CSE", "99", "A", "18"),
        ("Rohan", "MAE", "43", "B", "20"),
        ("Amit", "ECE", "24", "A", "21"),
        ("Anil", "MAE", "45", "B", "20"),
        ("Megha", "ECE", "55", "A", "22"),
        ("Sita", "CSE", "95", "A", "19")
    ]
    insert_many_data(students)


if __name__ == '__main__':
    main()