"""
Module: app
This module demonstrates a simple end-to-end flow of the parking system use cases.
"""

from authentication import login, logout
from parking import get_available_spots, reserve_spot
from payment import process_payment
from history import get_transaction_history
from notification import send_notification

def main():
    # Use Case 1: Login
    try:
        user = login("faculty1", "secret1")
        print(f"Logged in: {user}")
    except ValueError as e:
        print(f"Login failed: {e}")
        return

    # Use Case 2: View Available Parking Spots
    available_spots = get_available_spots()
    print("Available parking spots:", available_spots)

    # Use Case 3: Reserve a Parking Spot
    try:
        reservation = reserve_spot(spot_id=1, user_id=user.username, time_slot="2025-03-23 10:00-12:00")
        print("Reservation successful:", reservation)
    except ValueError as e:
        print(f"Reservation failed: {e}")
        return

    # Use Case 4: Pay for Parking
    try:
        payment_success = process_payment(
            user_id=user.username,
            amount=10.0,
            payment_details={"card_number": "1234567812345678", "cvv": "123"}
        )
        if payment_success:
            print("Payment processed successfully.")
    except ValueError as e:
        print(f"Payment failed: {e}")
        return

    # Use Case 5: View Transaction/Parking History
    history = get_transaction_history(user.username)
    print("Transaction history:", history)

    # Use Case 6: Send Notification
    send_notification(user.username, "Your parking reservation is confirmed for 2025-03-23 10:00-12:00.")

    # Use Case 7: Logout
    if logout(user):
        print("User logged out successfully.")

if __name__ == "__main__":
    main()
