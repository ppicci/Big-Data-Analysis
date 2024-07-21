from dbConnection import db_connection, close_connection
#from dbOperations import drop_database, show_databases
from dbOperations import show_databases
from mysql.connector import Error

def drop_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
        connection.commit()
        print(f"Database {db_name} dropped successfully.")
    except Error as err:
        print(f"Error dropping database {db_name}: {err}")
    finally:
        cursor.close()

def reset_database(host, user, password, db_name):

    conn = db_connection(host, user, password,db_name)
    if conn:
        try:
            # Show databases before dropping
            print("Databases before dropping:")
            show_databases(conn)

            # Confirm before dropping the database
            response = input(f"Are you sure you want to drop the database {db_name}? Type 'yes' to confirm: ")
            if response.lower() == 'yes':
                drop_database(conn, db_name)
                print("Databases after dropping:")
                show_databases(conn)
            else:
                print("Operation canceled.")
        finally:
            close_connection(conn)

if __name__ == "__main__":
    host = "34.121.116.155"  # Add here your host IP address from the GCP
    user = "root"
    password = 'Z"#JrsP*;3@]Bhgz'  # Add here your password
    database_name = "mininet_db"

    reset_database(host, user, password, database_name)
