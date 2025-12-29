import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print("Chyba připojení k databázi")
        print("Zkontroluj config.py nebo běh MySQL serveru")
        print(e)
        exit(1)
