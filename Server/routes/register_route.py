from fastapi import APIRouter
# Importing all models from models/__init__.py
from models import *
import database_connect
from mysql.connector import Error
from auth_tools import AuthTool
from create_fake_profiles import *


# Creating a router
router = APIRouter()

# Endpoint to register a new user (POST/register)
@router.post("")
def register_user(user: UserCreate):    
    try:
        connection = database_connect.get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO user (username, is_admin, email, user_password, picture) VALUES (%s, 0, %s, %s, '../Client/public/images/NOPICTURE.png')",
            (user.username, user.email, AuthTool.pwd_context.hash(user.password))
        )
        connection.commit()
        return {"message": "User registration successful!"}
    except Error as e:
        print(f"The error' '{e}' 'occured")
        return {"error": "An error occured during registration. Username and email may already be taken."}
    finally:
        cursor.close()
        connection.close()

# route pour récupérer les fake profiles sur le front 
@router.get("/fake-users", response_model=List[UserCreate])
def get_fake_users():
    try:
        return fake_users_set1
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Failed to fetch fake users"}