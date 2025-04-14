from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
import os
from auth_utils import hash_password, verify_password
#try test

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db():
    return psycopg2.connect(DATABASE_URL)

class UserRegister(BaseModel):
    full_name: str
    email: str
    password: str
    role: str  # should be "student", "faculty", or "admin"

@app.post("/register")
def register(user: UserRegister):
    conn = get_db()
    cur = conn.cursor()

    hashed_pw = hash_password(user.password)

    try:
        cur.execute("""
            INSERT INTO Users (full_name, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
        """, (user.full_name, user.email, hashed_pw, user.role))
        conn.commit()
    except psycopg2.Error as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail="Email already exists.")
    finally:
        cur.close()
        conn.close()

    return {"message": "User registered successfully."}
  
