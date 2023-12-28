import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_database_connection():
    return mysql.connector.connect(
        host = os.getenv('MYSQL_HOST'),
        user = os.getenv('MYSQL_USER'),
        password = os.getenv('MYSQL_ROOT_PASSWORD'),
        database = os.getenv('MYSQL_DATABASE'),
    )