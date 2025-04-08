from datetime import datetime
from connect_mongo import get_mongo_collections

payments_collection, _ = get_mongo_collections()

def insert_payment(user_id, amount, method, status="completed", reservation_id=None):
    """
    Inserts a payment document into MongoDB.
    """
    try:
        payment = {
            "user_id": user_id,
            "amount": amount,
            "method": method,
            "status": status,
            "reservation_id": reservation_id,
            "date": datetime.now()
        }

        result = payments_collection.insert_one(payment)
        print(f"Payment saved with ID : {result.inserted_id}")
        return result.inserted_id

    except Exception as e:
        print("Error during payment insertion :", e)
        return None

# Test rapide
if __name__ == "__main__":
    insert_payment(
        user_id="test_user",
        amount=5.00,
        method="credit_card",
        status="completed",
        reservation_id=None
    )
