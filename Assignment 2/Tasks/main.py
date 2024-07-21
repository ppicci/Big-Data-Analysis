from dbConnection import *
from dbOperations import *


if __name__ == "__main__":
    host = "34.121.116.155"  # Add here your host IP address from the GCP
    user = "root"
    password = 'Z"#JrsP*;3@]Bhgz'  # Add here your password
    database_name = "mininet_db"

    check_for_and_create_database(host, user, password, database_name)

    check_database_connection(host, user, password, database_name)

    create_and_display_tables(host, user, password, database_name)

    insert_and_display_tables(host, user, password, database_name)

    query_and_display_results(host, user, password, database_name)