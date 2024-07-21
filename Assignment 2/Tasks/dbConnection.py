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

def db_connection(host_name, user_name, user_password, db_name):
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

def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print("Database connection now closed.")
