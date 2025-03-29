"""
Processes payments for parking reservations.
"""

def process_payment(user_id: str, amount: float, payment_details: dict) -> bool:
    """
    Processes payment for a parking reservation.

    Flow of Control:
        - The user proceeds to payment after reserving a spot.
        - The user enters payment details.
        - The system processes the payment via a payment gateway.
    
    Args:
        user_id (str): The identifier of the user.
        amount (float): The payment amount.
        payment_details (dict): Payment information such as card number and CVV.

    Returns:
        bool: True if the payment is processed successfully.

    Raises:
        ValueError: If payment processing fails.
    """
    # For demonstration, check that minimal payment details exist.
    if payment_details.get("card_number") and payment_details.get("cvv"):
        # Payment is assumed successful.
        return True
    else:
        raise ValueError("Payment failed: Invalid payment details.")
