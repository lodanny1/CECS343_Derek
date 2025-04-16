from datetime import datetime, timedelta
from connect_mongo import get_mongo_collections

# Get reservations collection
_, reservations_collection = get_mongo_collections()

def update_expired_reservations():
    """
    Updates the status of reservations that have expired (i.e., their end_time is in the past).
    """
    now = datetime.now()

    try:
        result = reservations_collection.update_many(
            {
                "end_time": {"$lt": now},
                "status": {"$in": ["active", "upcoming"]}
            },
            {"$set": {"status": "expired"}}
        )

        print(f"Update of expired reservations : {result.modified_count}")
        return result.modified_count

    except Exception as e:
        print("Error during update reservation :", e)
        return 0

if __name__ == "__main__":
    update_expired_reservations()