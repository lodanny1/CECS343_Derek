"""
Module: auth
This module handles user authentication including login and logout.
"""

from user import User

# Simulated user database for demonstration purposes.
USER_DB = {
    "faculty1": {"password": "secret1", "email": "faculty1@university.edu", "role": "Faculty"},
    "student1": {"password": "secret2", "email": "student1@university.edu", "role": "Student"},
    "visitor1": {"password": "secret3", "email": "visitor1@example.com", "role": "Visitor"},
}

def login(username: str, password: str) -> User:
    """
    Authenticates the user with the provided credentials.

    Flow of Control:
        - The user navigates to the login page.
        - The user enters username and password.
        - The system verifies the credentials.
        - If valid, the system returns a User instance.

    Args:
        username (str): The username entered by the user.
        password (str): The password entered by the user.

    Returns:
        User: The authenticated user object.

    Raises:
        ValueError: If credentials are invalid.
    """
    if username in USER_DB and USER_DB[username]["password"] == password:
        user_info = USER_DB[username]
        return User(username=username, email=user_info["email"], is_active=True)
    else:
        raise ValueError("Invalid username or password.")

def logout(user: User) -> bool:
    """
    Logs out the given user by terminating their session.

    Flow of Control:
        - The user selects the logout option.
        - The system terminates the session and returns to the login screen.

    Args:
        user (User): The user to be logged out.

    Returns:
        bool: True if logout is successful.
    """
    # In a real application, session termination logic would go here.
    return True
