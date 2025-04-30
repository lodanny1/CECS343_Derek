import PySimpleGUI as sg
from pymongo.mongo_client import MongoClient
import bcrypt
import certifi

# ------ MongoDB Atlas Connection ------
# Replace <db_password> with your actual password (URL-encode special chars)
uri = (
    "mongodb+srv://Skullgame300:Skullgame300"
    "@parking.v4glm.mongodb.net/user_auth"
    "?retryWrites=true&w=majority&appName=Parking"
)

# Create client with TLS and certifi’s CA bundle
client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())

# Ping to verify connection
try:
    client.admin.command("ping")
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print(f"❌ MongoDB connection error:\n{e}")

db = client["user_auth"]
users = db["users"]

# ------ Authentication Functions ------
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

# ------ PySimpleGUI Windows ------
def register_window():
    layout = [
        [sg.Text("Create a New Account", font=("Helvetica", 14))],
        [sg.Text("Username", size=(12,1)), sg.Input(key="-R-USER-")],
        [sg.Text("Password", size=(12,1)), sg.Input(key="-R-PASS-", password_char="*")],
        [sg.Button("Submit"), sg.Button("Cancel")]
    ]
    win = sg.Window("Register", layout, modal=True)
    while True:
        event, vals = win.read()
        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break
        if event == "Submit":
            ok, msg = register_user(vals["-R-USER-"], vals["-R-PASS-"])
            sg.popup(msg)
            if ok:
                break
    win.close()

def login_window():
    layout = [
        [sg.Text("Please Log In", font=("Helvetica", 14))],
        [sg.Text("Username", size=(12,1)), sg.Input(key="-L-USER-")],
        [sg.Text("Password", size=(12,1)), sg.Input(key="-L-PASS-", password_char="*")],
        [sg.Button("Login"), sg.Button("Register"), sg.Button("Exit")]
    ]
    win = sg.Window("Login", layout)
    while True:
        event, vals = win.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            win.close()
            return None
        if event == "Register":
            register_window()
        if event == "Login":
            if validate_login(vals["-L-USER-"], vals["-L-PASS-"]):
                win.close()
                return vals["-L-USER-"]
            else:
                sg.popup("Invalid username or password", title="Error")

def dashboard_window(username):
    layout = [
        [sg.Text(f"Welcome, {username}!", font=("Helvetica", 14))],
        [sg.Button("Logout"), sg.Button("Exit")]
    ]
    win = sg.Window("Dashboard", layout)
    while True:
        event, _ = win.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            win.close()
            return False   # Exit app
        if event == "Logout":
            win.close()
            return True    # Back to login

# ------ Main Application Loop ------
if __name__ == "__main__":
    sg.theme("LightBlue")
    while True:
        user = login_window()
        if not user:
            break
        if not dashboard_window(user):
            break
    sg.popup("Goodbye!")
