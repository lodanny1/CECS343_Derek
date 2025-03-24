"""
Handles retrieval of a user's transaction and parking history.
"""

# Simulated transaction history database.
TRANSACTION_HISTORY = {
    "faculty1": [
        {"transaction_id": 101, "amount": 10.0, "date": "2025-03-22", "spot": 1}
    ],
    "student1": [],
    "visitor1": [],
}

def get_transaction_history(user_id: str):
    """
    Retrieves the transaction and parking history for the specified user.

    Flow of Control:
        - The user navigates to the history page.
        - The system retrieves and displays the user's history.

    Args:
        user_id (str): The identifier of the user.

    Returns:
        list: A list of transaction records.
    """
    return TRANSACTION_HISTORY.get(user_id, [])
