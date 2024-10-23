from fastapi import APIRouter
from models import *
import database_connect
from mysql.connector import Error
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["Bcrypt"], deprecated="auto")

router = APIRouter()

@router.post("")
def register_user(user: UserCreate):    
    try:
        connection = database_connect.get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO user (username, is_admin, email, user_password, picture_id) VALUES (%s, 0, %s, %s, 0)",
            (user.username, user.email, pwd_context.hash(user.password))
        )
        connection.commit()
        return {"message": "User registration successful!"}
    except Error as e:
        print(f"The error' '{e}' 'occured")
        return {"error": "Error with user registration"}
    finally:
        cursor.close()
        connection.close()