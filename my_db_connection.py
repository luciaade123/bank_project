"""
Lucia Adeola
project 2
step 2
my_db_connection.py
"""

# step 1: import psycopg2
import psycopg2

# step 2: Define the function


def connect_to_db(vault_file):
    """
    connect to the bank databse using password and username credentials from vault file.
    parameters are vault_file (str): path to the vault txt file
    returns connection or none if connection fails.
    """
    # open the vault file
    with open(vault_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # username and password for user
    username = lines[0].strip()
    password = lines[1].strip()
    

    # connect to the bank database and return connection
    try:
        conn = psycopg2.connect(
            dbname="bank",
            user=username,
            password=password,
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.OperationalError as error:
        print("Connection failed:", error)
        return None
