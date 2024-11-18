from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# Importing all the routes from routes/__init__.py
from register_route import register_router
from message_route import message_router
from tag_route import tag_router
from login_route import login_router
from token_route import token_router 
from user_route import user_router


app = FastAPI()

# Configuration de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(register_router, prefix="/register", tags=["Register"])
app.include_router(message_router, prefix="/messages", tags=["Messages"])
app.include_router(tag_router, prefix="/tags")
app.include_router(login_router, prefix="/login", tags=["Logins"])
app.include_router(token_router, prefix="/token")
app.include_router(user_router, prefix="/user", tags=["Users"])

app.mount("/Server/profilePictures", StaticFiles(directory="profilePictures"), name="static") # to upload local files


