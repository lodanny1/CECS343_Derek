from pymongo import MongoClient

uri = "mongodb+srv://flavienmaameri57:PQJ2bKWCg3TnbPVq@parking.v4glm.mongodb.net/?retryWrites=true&w=majority&appName=Parking"

try:
    client = MongoClient(uri, tls=True)
    db = client["parking_db"]
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
