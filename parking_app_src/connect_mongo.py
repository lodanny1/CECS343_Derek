from pymongo import MongoClient

def get_mongo_collections():
    uri = "mongodb+srv://flavienmaameri57:DCU9o2Vg0K8PvjnG@parking.v4glm.mongodb.net/?retryWrites=true&w=majority&appName=Parking"

    client = MongoClient(uri, tls=True)
    db = client["parking_db"]

    payments = db["payments"]
    reservations = db["reservations"]

    return payments, reservations
