from connect_mongo import get_mongo_collections
payments_collection, _ = get_mongo_collections()

def read_payments():
    """
    Reads and displays all payments from the MongoDB collection.
    """
    try:
        payments = payments_collection.find().sort("date", -1)
        print("\n--- Payment History ---")
        for payment in payments:
            print(f"ID: {payment.get('_id')} | User: {payment.get('user_id')} | Amount: {payment.get('amount')}€ | Method: {payment.get('method')} | Status: {payment.get('status')} | Reservation: {payment.get('reservation_id')} | Date: {payment.get('date')}")
    except Exception as e:
        print("Error while reading payments:", e)

# view per user (to use when user_id is known)
# def read_payments_by_user(user_id):
#     """
#     Displays only the payments made by a specific user.
#     """
#     try:
#         payments = payments_collection.find({"user_id": user_id}).sort("date", -1)
#         print(f"\n--- Payment History for User: {user_id} ---")
#         for payment in payments:
#             print(f"ID: {payment.get('_id')} | Amount: {payment.get('amount')}€ | Method: {payment.get('method')} | Status: {payment.get('status')} | Reservation: {payment.get('reservation_id')} | Date: {payment.get('date')}")
#     except Exception as e:
#         print("Error while reading user payments:", e)

if __name__ == "__main__":
    read_payments()
    # Example future usage:
    # read_payments_by_user("user_test_001")