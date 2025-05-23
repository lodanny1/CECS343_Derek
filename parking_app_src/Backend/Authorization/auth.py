import bcrypt
import certifi
from pymongo import MongoClient

# MongoDB connection
uri = (
    "mongodb+srv://Skullgame300:Skullgame300"
    "@parking.v4glm.mongodb.net/user_auth"
    "?retryWrites=true&w=majority&appName=Parking"
)
client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())
db = client["user_auth"]
users = db["users"]

def register_user(username: str, password: str):
    if not username or not password:
        return False, "Username and password cannot be empty!"
    if users.find_one({"username": username}):
        return False, "Username already exists!"
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    users.insert_one({"username": username, "password": hashed})
    return True, "Registration successful!"

def validate_login(username: str, password: str):
    user = users.find_one({"username": username})
    return bool(user and bcrypt.checkpw(password.encode("utf-8"), user["password"]))
