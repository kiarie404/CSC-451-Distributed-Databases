################################################################
# import the python-to-database drivers (connectors):
################################################################
import mysql.connector as mysql_mariadb_driver          # mysql.connector driver synchs with both MariaDB and Mysql database engines.
from mysql.connector import Error as mysql_like_error   # For us to get mysql error messages. Instead of uninformative and verbose python error messages

import psycopg2                                         # The Psycopg library acts as a python-to-database driver to the PostgreSql database.
from psycopg2 import Error as postgresql_like_error     # For us to get postgresql error messages. Instead of uninformative and verbose python error messages


import predefined_sql_queries


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
try: 
    site_2_mariadb_connection = mysql_mariadb_driver.connect(host="192.168.56.101", user="remote_root", password="admin_password", database="lab_x")
    print("Successfully Connected to site 2 mariadb server")
except mysql_like_error as connection_error_message:
    print("Error: Failure in the creation of a Connection to the mariadb server found in site 2 Linux machine \n", connection_error_message)

# Site 3 connection.
try: 
    site_3_mysql_connection = mysql_mariadb_driver.connect(host="192.168.56.102", user="remote_root", password="admin_password", database="lab_x")
    print("Successfully Connected to site 3 mysql server")
except mysql_like_error as connection_error_message:
    print("Error: Failure in the creation of a Connection to the mysql server found in site 3 Linux machine \n", connection_error_message)

# def pretty_print (some_array):
#     for element in some_array :
#         print(element)


def reconstruct_job_descriptions_table():
    site_1_job_descriptions_relation = perform_union_of_job_descriptions_tables_at_site(site_1_postgre_connection)
    site_2_job_descriptions_relation = perform_union_of_job_descriptions_tables_at_site(site_2_mariadb_connection)
    site_3_job_descriptions_relation = perform_union_of_job_descriptions_tables_at_site(site_3_mysql_connection)
    unionised_job_descriptions_table = site_1_job_descriptions_relation.union(site_2_job_descriptions_relation, site_3_job_descriptions_relation)
    return unionised_job_descriptions_table

def perform_union_of_job_descriptions_tables_at_site (site_connection):
    # create database cursor to navigate the database using sql queries
    cursor = site_connection.cursor()

    # extract data from the fragments and temporarily store them in seperate lists
    get_fragment = "SELECT * FROM job_descriptions"
    cursor.execute(get_fragment)
    frag_list = cursor.fetchall()

    # convert the seperate lists into sets; so that we can do union operation
    frag_set = set(frag_list)
    return frag_set

def reconstruct_employees_table():
    site_1_employees_relation = perform_union_of_employees_tables_at_site(site_1_postgre_connection)
    site_2_employees_relation = perform_union_of_employees_tables_at_site(site_2_mariadb_connection)
    site_3_employees_relation = perform_union_of_employees_tables_at_site(site_3_mysql_connection)
    unionised_employees_table = site_1_employees_relation.union(site_2_employees_relation, site_3_employees_relation)
    return unionised_employees_table

def perform_union_of_employees_tables_at_site (site_connection):
    # create database cursor to navigate the database using sql queries
    cursor = site_connection.cursor()

    # extract data from the fragments and temporarily store them in seperate lists
    get_fragment = "SELECT * FROM employees"
    cursor.execute(get_fragment)
    frag_list = cursor.fetchall()

    # convert the seperate lists into sets; so that we can do union operation
    frag_set = set(frag_list)
    return frag_set

def reconstruct_projects_table():
    site_1_projects_relation = perform_union_of_projects_tables_at_site(site_1_postgre_connection)
    site_2_projects_relation = perform_union_of_projects_tables_at_site(site_2_mariadb_connection)
    site_3_projects_relation = perform_union_of_projects_tables_at_site(site_3_mysql_connection)
    unionised_projects_table = site_1_projects_relation.union(site_2_projects_relation, site_3_projects_relation)
    return unionised_projects_table

def perform_union_of_projects_tables_at_site (site_connection):
    # create database cursor to navigate the database using sql queries
    cursor = site_connection.cursor()

    # extract data from the fragments and temporarily store them in seperate lists
    get_fragment_1_sql = "SELECT * FROM projects_fragment_1"
    get_fragment_2_sql = "SELECT * FROM projects_fragment_2"
    cursor.execute(get_fragment_1_sql)
    frag_1_list = cursor.fetchall()
    cursor.execute(get_fragment_2_sql)
    frag_2_list = cursor.fetchall()

    # convert the seperate lists into sets; so that we can do union operation
    frag_1_set = set(frag_1_list)
    frag_2_set = set(frag_2_list)
    temporary_union = frag_1_set.union(frag_2_set)
    return temporary_union

def reconstruct_assignations_table():
    site_1_assignations_relation = perform_union_of_asgn_tables_at_site(site_1_postgre_connection)
    site_2_assignations_relation = perform_union_of_asgn_tables_at_site(site_2_mariadb_connection)
    site_3_assignations_relation = perform_union_of_asgn_tables_at_site(site_3_mysql_connection)
    unionised_assignations_table = site_1_assignations_relation.union(site_2_assignations_relation, site_3_assignations_relation)
    return unionised_assignations_table


def perform_union_of_asgn_tables_at_site (site_connection):
    # create database cursor to navigate the database using sql queries
    cursor = site_connection.cursor()

    # extract data from the fragments and temporarily store them in seperate lists
    get_fragment_1_sql = "SELECT * FROM assignations_fragment_1"
    get_fragment_2_sql = "SELECT * FROM assignations_fragment_2"
    cursor.execute(get_fragment_1_sql)
    frag_1_list = cursor.fetchall()
    cursor.execute(get_fragment_2_sql)
    frag_2_list = cursor.fetchall()

    # convert the seperate lists into sets; so that we can do union operation
    frag_1_set = set(frag_1_list)
    frag_2_set = set(frag_2_list)
    temporary_union = frag_1_set.union(frag_2_set)
    return temporary_union

def populate_reconstructed_schema (job_descriptions_union, employees_union, projects_union, assignations_union):
    populate_reconstructed_projects_table(projects_union)
    populate_reconstructed_job_descriptions_table(job_descriptions_union)
    populate_reconstructed_employees_table(employees_union)
    populate_reconstructed_assignations_table(assignations_union)

def populate_reconstructed_job_descriptions_table(some_union):
    # using prepared statements to populate the reconstruted schema
    insert_data_to_students_table_formated = """
    INSERT INTO reconstructed_job_descriptions(job_id, job_title, job_pay) 
    VALUES (%s, %s, %s)
    """

    some_list = list(some_union) #convert set into a list type

    # insert data into table using the prepared sql statement
    postgre_cursor = site_1_postgre_connection.cursor()
    for element in some_list:
        postgre_cursor.execute(insert_data_to_students_table_formated, element)
        site_1_postgre_connection.commit()


def populate_reconstructed_employees_table(some_union):
    # using prepared statements to populate the reconstruted schema
    insert_data_to_employees_table_formated = """
    INSERT INTO reconstructed_employees(employee_id, employee_name, employee_job_id) 
    VALUES (%s, %s, %s)
    """

    some_list = list(some_union) #convert set into a list type

    # insert data into table using the prepared sql statement
    postgre_cursor = site_1_postgre_connection.cursor()
    for element in some_list:
        postgre_cursor.execute(insert_data_to_employees_table_formated, element)
        site_1_postgre_connection.commit()

def populate_reconstructed_projects_table(some_union):
    # using prepared statements to populate the reconstruted schema
    insert_data_to_projects_table_formated = """
    INSERT INTO reconstructed_projects(project_id, project_name, project_budget, project_location) 
    VALUES (%s, %s, %s, %s)
    """

    some_list = list(some_union) #convert set into a list type

    # insert data into table using the prepared sql statement
    postgre_cursor = site_1_postgre_connection.cursor()
    for element in some_list:
        postgre_cursor.execute(insert_data_to_projects_table_formated, element)
        site_1_postgre_connection.commit()

def populate_reconstructed_assignations_table(some_union):
    # using prepared statements to populate the reconstruted schema
    insert_data_to_assignations_table_formated = """
    INSERT INTO reconstructed_assignations(assignation_id, employee_id, project_id, project_duration) 
    VALUES (%s, %s, %s, %s)
    """

    some_list = list(some_union) #convert set into a list type

    # insert data into table using the prepared sql statement
    postgre_cursor = site_1_postgre_connection.cursor()
    for element in some_list:
        postgre_cursor.execute(insert_data_to_assignations_table_formated, element)
        site_1_postgre_connection.commit()

def perform_reconstruction ():
    job_descriptions_union = reconstruct_job_descriptions_table()
    employees_union = reconstruct_employees_table()
    projects_union = reconstruct_projects_table()
    assignations_union = reconstruct_assignations_table()
    populate_reconstructed_schema(job_descriptions_union, employees_union, projects_union, assignations_union)
    print("successful full reconstruction")


perform_reconstruction()
