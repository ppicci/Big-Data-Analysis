from dbConnection import *
from dbTables import dbTables
from dbInserts import dbInserts
from dbQueries import dbQueries
import decimal
import datetime

def create_database(connection, db_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        cursor.close()


def show_databases(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SHOW DATABASES")
        print("Available Databases:")
        for (database,) in cursor:
            print(database.decode("utf-8"))
    finally:
        cursor.close()


def check_for_and_create_database(host, user, password, database_name):
    server_conn = server_connection(host, user, password)
    if server_conn:
        create_database(server_conn, database_name)
        server_conn.close()


def check_database_connection(host, user, password, database_name):
    db_conn = db_connection(host, user, password, database_name)
    if db_conn:
        show_databases(db_conn)
        db_conn.close()

def print_results(cursor):
    """ Helper function to print results with column headers and formatted data. """
    columns = [desc[0] for desc in cursor.description]
    print(", ".join(columns))  # Print column headers

    for row in cursor.fetchall():
        formatted_row = []
        for item in row:
            if isinstance(item, decimal.Decimal):
                # Format decimal as a float
                formatted_row.append(f"{float(item):.2f}")
            elif isinstance(item, datetime.date):
                # Format date as a string
                formatted_row.append(item.strftime('%Y-%m-%d'))
            else:
                formatted_row.append(str(item))
        print(", ".join(formatted_row))

def create_and_display_tables(host, user, password, database_name):
    conn = db_connection(host, user, password, database_name)
    if conn:
        cursor = conn.cursor()
        for table_name, create_command in dbTables.items():
            try:
                cursor.execute(create_command)
                conn.commit()
                print(f"Table {table_name} created successfully.")

                cursor.execute(f"SELECT * FROM {table_name};")
                print(f"Contents of {table_name}:")
                print_results(cursor)  # Use the helper function
                print()

            except Error as err:
                print(f"Error creating/displaying table {table_name}: {err}")
        cursor.close()
        close_connection(conn)

def insert_and_display_tables(host, user, password, database_name):
    conn = db_connection(host, user, password, database_name)
    if conn:
        cursor = conn.cursor()
        for table_name, insert_command in dbInserts.items():
            try:
                cursor.execute(insert_command)
                conn.commit()
                print(f"Table {table_name} insertion successful.")

                cursor.execute(f"SELECT * FROM {table_name};")
                print(f"New contents of {table_name}:")
                print_results(cursor)  # Use the helper function
                print()

            except Error as err:
                print(f"Error inserting into/displaying table {table_name}: {err}")
        cursor.close()
        close_connection(conn)

def query_and_display_results(host, user, password, database_name):
    conn = db_connection(host, user, password, database_name)
    if conn:
        cursor = conn.cursor()
        for query_name, query_command in dbQueries.items():
            try:
                cursor.execute(query_command)
                print(f"{query_name} Result:")
                print_results(cursor)  # Use the helper function
                print()

            except Error as err:
                print(f"Error with {query_name}: {err}")
        cursor.close()
        close_connection(conn)