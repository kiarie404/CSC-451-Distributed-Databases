################################################################
# import the python-to-database drivers (connectors):
################################################################
import mysql.connector as mysql_mariadb_driver          # mysql.connector driver synchs with both MariaDB and Mysql database engines.
from mysql.connector import Error as mysql_like_error   # For us to get mysql error messages. Instead of uninformative and verbose python error messages

import psycopg2                                         # The Psycopg library acts as a python-to-database driver to the PostgreSql database.
from psycopg2 import Error as postgresql_like_error     # For us to get postgresql error messages. Instead of uninformative and verbose python error messages




### Establish database connections to all sites  
### Establishing connection to Site 1 { Windows + PostgreSql + Localhost}
### Establishing connection to Site 2 { Linux Mint + MariaDB + 192.168.56.101}
### Establishing connection to Site 3 { Linux Mint + MySQL + 192.168.56.102}

# Site 1 connection.
try:
    site_1_postgre_connection = psycopg2.connect("dbname='lab_x' user='postgres' password='admin_password'")
    print("Successfully Connected to site 1 postgresql database")
except postgresql_like_error as connection_error_message:
    print("Error: Failure in the creation of a Connection to the Posgresql server found in site 1 Windows machine \n", connection_error_message)

# Site 2 connection.
# try: 
#     site_2_mariadb_connection = mysql_mariadb_driver.connect(host="192.168.56.101", user="remote_root", password="admin_password", database="lab_x")
#     print("Successfully Connected to site 2 mariadb server")
# except mysql_like_error as connection_error_message:
#     print("Error: Failure in the creation of a Connection to the mariadb server found in site 2 Linux machine \n", connection_error_message)

# Site 3 connection.
try: 
    site_3_mysql_connection = mysql_mariadb_driver.connect(host="192.168.56.102", user="remote_root", password="admin_password", database="lab_x")
    print("Successfully Connected to site 3 mysql server")
except mysql_like_error as connection_error_message:
    print("Error: Failure in the creation of a Connection to the mysql server found in site 3 Linux machine \n", connection_error_message)

