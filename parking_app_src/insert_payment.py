from connect_mongo import get_mongo_collections
from datetime import datetime
import random

payments_collection, _ = get_mongo_collections()

def simulate_payment(method):
    """
    Simulates a payment validation process for credit or debit cards.
    Returns 'completed' or 'failed'.
    """
    if method not in ["credit_card", "debit_card"]:
        print(f"Unsupported payment method: {method}")
        return "failed"
    # handle case like no more money stuff like that
    success_rate = 0.9 if method == "credit_card" else 0.85
    return "completed" if random.random() < success_rate else "failed"

def insert_payment(user_id, amount, method, status=None, reservation_id=None):
    """
    Inserts a payment into MongoDB. If no status is provided, simulates payment outcome.
    """
    try:
        if status is None:
            status = simulate_payment(method)

        payment = {
            "user_id": user_id,
            "amount": round(amount, 2),
            "method": method,
            "status": status,
            "reservation_id": reservation_id,
            "date": datetime.now()
        }
        result = payments_collection.insert_one(payment)
        print(f"Payment inserted (Status: {status}) - ID: {result.inserted_id}")
        return result.inserted_id if status == "completed" else None

    except Exception as e:
        print("Error inserting payment:", e)
        return None

#test
if __name__ == "__main__":
    insert_payment("user_test_001", 5.50, "credit_card")
