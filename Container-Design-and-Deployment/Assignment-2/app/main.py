import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from database import get_database_connection
from mysql.connector.errors import InternalError
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

@app.get("/")
def read_root():
    #connection = get_database_connection()
    #print(connection)
    return {"DB_HOST": os.getenv('DB_HOST'),
            "DB_USER": os.getenv('DB_USER'),
            "MYSQL_ROOT_PASSWORD": os.getenv('MYSQL_ROOT_PASSWORD'),
            "DB_DATABASE": os.getenv('DB_DATABASE'),
            }

@app.get("/databases")
async def show_databases():
    connection = get_database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT 1")
        connection.commit()
    except InternalError as ex:
        print(ex)
    connection.close()


# os.getenv('DB_DATABASE')

class User(BaseModel):
    name: str
    email: str


@app.post("/users")
async def create_user(user: User):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = (user.name, user.email)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "User created successfully"}

@app.get("/users")
async def read_users():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    connection.close()
    return users


# uvicorn main:app --reload --port=8080 --host=0.0.0.0



# env['variablename']