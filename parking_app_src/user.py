"""
Defines the User class for the parking system.
"""

import re

class User:
    """
    Represents a user in the parking system.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        role (str): The role of the user (Faculty, Student, Visitor).
        is_active (bool): Indicates whether the user's account is active.
    """

    def __init__(self, username: str, email: str, password: str, role: str, is_active: bool = True):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
            password (str): The user's password.
            role (str): The user's role (Faculty, Student, Visitor).
            is_active (bool, optional): Whether the user is active. Defaults to True.
        """
        self.username = username
        self.email = email
        self.password = password  # In real apps, use a hash instead
        self.role = role
        self.is_active = is_active

        if not self._validate_email(email):
            raise ValueError("Invalid email format.")

    def deactivate(self):
        """Deactivates the user account."""
        self.is_active = False

    def activate(self):
        """Activates the user account."""
        self.is_active = True

    def update_email(self, new_email: str):
        """Updates the email address after validating it."""
        if self._validate_email(new_email):
            self.email = new_email
        else:
            raise ValueError("Invalid email format.")

    def update_password(self, new_password: str):
        """Updates the user password."""
        self.password = new_password

    def _validate_email(self, email: str) -> bool:
        """Validates email format using regex."""
        pattern = r"[^@]+@[^@]+\.[^@]+"
        return re.match(pattern, email) is not None

    def __str__(self) -> str:
        """Returns a string representation of the user."""
        return (f"User(username='{self.username}', email='{self.email}', "
                f"role='{self.role}', is_active={self.is_active})")

