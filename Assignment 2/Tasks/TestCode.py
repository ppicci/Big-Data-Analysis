import mysql.connector
from mysql.connector import Error


def server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}");
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"Connected to MySQL database {db_name}")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def check_and_create_database(host, user, password, database_name):
    server_conn = server_connection(host, user, password)
    if server_conn:
        create_database(server_conn, database_name)
        server_conn.close()


def show_databases(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES;")
    print("Available Databases:")
    for (database,) in cursor:
        print(database.decode("utf-8"))
    cursor.close()


def check_database_connection(host, user, password, database_name):
    db_conn = create_db_connection(host, user, password, database_name)
    if db_conn:
        show_databases(db_conn)
        db_conn.close()


if __name__ == "__main__":
    host = "34.121.116.155"  # Add here your host IP address from the GCP
    user = "root"
    password = 'Z"#JrsP*;3@]Bhgz'  # Add here your password
    database_name = "mininet_db"

    check_and_create_database(host, user, password, database_name)

    check_database_connection(host, user, password, database_name)
