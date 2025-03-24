"""
Defines the User class for the parking system.
"""

class User:
    """
    Represents a user in the parking system.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        is_active (bool): Indicates whether the user's account is active.
    """

    def __init__(self, username: str, email: str, is_active: bool = True):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
            email (str): The email address of the user.
            is_active (bool, optional): Indicates if the user account is active. Defaults to True.
        """
        self.username = username
        self.email = email
        self.is_active = is_active

    def deactivate(self):
        """
        Deactivates the user account.
        """
        self.is_active = False

    def activate(self):
        """
        Activates the user account.
        """
        self.is_active = True

    def __str__(self) -> str:
        """
        Returns a string representation of the user.

        Returns:
            str: A formatted string with the user's details.
        """
        return f"User(username='{self.username}', email='{self.email}', is_active={self.is_active})"
