from datetime import datetime
from connect_mongo import reservations_collection

def insert_reservation(user_id, parking_spot, reservation_time, duration_minutes, payment_id=None, status="active"):
    """
    Inserts a reservation into the 'reservations' collection.

    Parameters:
    - user_id (str): ID of the user making the reservation (e.g., 'student_001')
    - parking_spot (str): Parking spot number or identifier (e.g., 'A12')
    - reservation_time (datetime): Date and time of the reservation start
    - duration_minutes (int): Duration of the reservation in minutes
    - payment_id (str | None): Related payment ID, if available
    - status (str): Reservation status ("active", "completed", etc.)

    Returns:
    - The ObjectId of the inserted reservation, or None if an error occurred
    """
    try:
        reservation = {
            "user_id": user_id,
            "parking_spot": parking_spot,
            "reservation_time": reservation_time,
            "duration_minutes": duration_minutes,
            "payment_id": payment_id,
            "status": status,
            "created_at": datetime.now()
        }

        result = reservations_collection.insert_one(reservation)
        print(f"Reservation inserted successfully. ID: {result.inserted_id}")
        return result.inserted_id

    except Exception as e:
        print("Error inserting reservation:", e)
        return None


# Quick test
if __name__ == "__main__":
    insert_reservation(
        user_id="student_001",
        parking_spot="B21",
        reservation_time=datetime(2025, 3, 25, 14, 30),
        duration_minutes=120,
        payment_id=None,
        status="active"
    )
