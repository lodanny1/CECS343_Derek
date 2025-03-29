"""
Manages notifications for parking-related events.
"""

def send_notification(user_id: str, message: str) -> bool:
    """
    Sends a notification message to the user.

    Flow of Control:
        - A trigger event (like a reservation reminder) occurs.
        - The system generates and sends a notification to the user.

    Args:
        user_id (str): The identifier of the user.
        message (str): The notification message.

    Returns:
        bool: True if the notification is sent successfully.
    """
    # In a real application, this would interface with a push notification service.
    print(f"Notification to {user_id}: {message}")
    return True
