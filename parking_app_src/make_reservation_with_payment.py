from datetime import datetime
from insert_payment import insert_payment
from insert_reservations import insert_reservation
from check_availability import is_spot_available
from pricing import calculate_price

# TEMPORARY user_id placeholder (to be replaced later with real user system)
user_id = "user_test_001"

def make_reservation_with_payment(parking_spot, reservation_time, duration_minutes, amount, method):
    """
    Handles payment + reservation in a single flow.
    Only inserts the reservation if the payment is successful.
    """
    try:
        # Check spot availability
        if not is_spot_available(parking_spot, reservation_time, duration_minutes):
            print(f"Spot {parking_spot} is already reserved at the selected time.")
            return None

        # Insert payment first
        amount = calculate_price(duration_minutes)
        payment_id = insert_payment(user_id, amount, method, status="completed")

        if not payment_id:
            print("Payment failed. Reservation cancelled.")
            return None

        # Insert reservation only if payment is successful
        reservation_id = insert_reservation(
            user_id=user_id,
            parking_spot=parking_spot,
            reservation_time=reservation_time,
            duration_minutes=duration_minutes,
            payment_id=payment_id,
            status="active"
        )

        return reservation_id

    except Exception as e:
        print("Error during reservation with payment:", e)
        return None

# Example test
if __name__ == "__main__":
    make_reservation_with_payment(
        parking_spot="A1",
        reservation_time=datetime(2025, 3, 26, 10, 0),
        duration_minutes=45,
        amount=3.5,
        method="credit_card"
    )