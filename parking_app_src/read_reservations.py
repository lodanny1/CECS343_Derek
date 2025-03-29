from connect_mongo import get_mongo_collections

_, reservations_collection = get_mongo_collections()

def read_reservations():
    """
    Fetches and displays all reservations from the 'reservations' collection.
    """
    try:
        reservations = list(reservations_collection.find())

        if not reservations:
            print("No reservations found.")
            return []

        print("Reservations list:\n")
        for res in reservations:
            print(
                f"ID: {res.get('_id')}\n"
                f"User: {res.get('user_id')}\n"
                f"Spot: {res.get('parking_spot')}\n"
                f"Start: {res.get('reservation_time')}\n"
                f"Duration: {res.get('duration_minutes')} minutes\n"
                f"Payment ID: {res.get('payment_id')}\n"
                f"Status: {res.get('status')}\n"
                f"Created at: {res.get('created_at')}\n"
                "--------------------------------------------"
            )
        return reservations

    except Exception as e:
        print("Error while reading reservations:", e)
        return []

# Test rapide
if __name__ == "__main__":
    read_reservations()
