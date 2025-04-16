from connect_mongo import get_mongo_collections
from datetime import timedelta, datetime
import time

# Get reservations collection
_, reservations_collection = get_mongo_collections()

def is_spot_available(parking_spot, start_time, duration_minutes):
    """
    Checks if a parking spot is available for the given time slot.
    """
    try:
        end_time = start_time + timedelta(minutes=duration_minutes)

        overlapping_reservations = list(reservations_collection.find({
            "parking_spot": parking_spot,
            "$or": [
                {
                    "reservation_time": {"$lt": end_time},
                    "end_time": {"$gt": start_time}
                }
            ],
            "status": {"$in": ["active", "upcoming"]}
        }))

        return len(overlapping_reservations) == 0

    except Exception as e:
        print("Verification error for availability:", e)
        return False

def update_expired_reservations():
    """
    Updates the status of reservations that have expired (i.e., current time is past the reservation end time).
    """
    try:
        now = datetime.now()
        result = reservations_collection.update_many(
            {
                "end_time": {"$lte": now},
                "status": {"$in": ["active", "upcoming"]}
            },
            {"$set": {"status": "expired"}}
        )
        print(f"{result.modified_count} expired reservation(s).")
    except Exception as e:
        print("Error during reservation update:", e)

def run_auto_update(interval_seconds=60):
    """
    Runs the status update process continuously every interval (in seconds).
    """
    print("Auto-update. Verifications every", interval_seconds, "secondes.")
    while True:
        update_expired_reservations()
        time.sleep(interval_seconds)
