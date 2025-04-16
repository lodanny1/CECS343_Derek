import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, \
    QStackedWidget, QMessageBox


class LoginScreen(QWidget):
    def __init__(self, switch_to_register_callback):
        super().__init__()
        self.setWindowTitle('Login Screen')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter username")
        layout.addWidget(self.username_input)

        # Password Input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter password")
        layout.addWidget(self.password_input)

        # Login Button
        login_button = QPushButton("Login")
        layout.addWidget(login_button)
        login_button.clicked.connect(self.login)

        # Switch to Register Button
        switch_button = QPushButton("Don't have an account? Register here")
        layout.addWidget(switch_button)
        switch_button.clicked.connect(switch_to_register_callback)

        self.setLayout(layout)

    def login(self):
        """Validate login inputs and simulate login"""
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            self.show_error_message("Please fill in both username and password.")
            return

        # Simulating login with hardcoded values (change these later for actual authentication)
        correct_username = "user1"
        correct_password = "password123"

        if username == correct_username and password == correct_password:
            print("Login Successful")
            self.show_info_message("Login Successful")
        else:
            self.show_error_message("Invalid username or password.")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def show_info_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Info")
        msg.exec_()


class RegistrationScreen(QWidget):
    def __init__(self, switch_to_login_callback):
        super().__init__()
        self.setWindowTitle('Registration Screen')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # Username Input
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter username")
        layout.addWidget(self.username_input)

        # Email Input
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter email")
        layout.addWidget(self.email_input)

        # Password Input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setPlaceholderText("Enter password")
        layout.addWidget(self.password_input)

        # Confirm Password Input
        self.confirm_password_input = QLineEdit(self)
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setPlaceholderText("Confirm password")
        layout.addWidget(self.confirm_password_input)

        # Register Button
        register_button = QPushButton("Register")
        layout.addWidget(register_button)
        register_button.clicked.connect(self.register)

        # Switch to Login Button
        switch_button = QPushButton("Already have an account? Login here")
        layout.addWidget(switch_button)
        switch_button.clicked.connect(switch_to_login_callback)

        self.setLayout(layout)

    def register(self):
        """Validate registration inputs"""
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not email or not password or not confirm_password:
            self.show_error_message("All fields must be filled out.")
            return

        if not self.is_valid_email(email):
            self.show_error_message("Please enter a valid email address.")
            return

        if password != confirm_password:
            self.show_error_message("Passwords do not match.")
            return

        print(f"Registering - Username: {username}, Email: {email}, Password: {password}")
        self.show_info_message("Registration Successful!")

    def is_valid_email(self, email):
        """Basic email validation"""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email)

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def show_info_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Info")
        msg.exec_()


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create stacked widget to switch between screens
        self.stacked_widget = QStackedWidget(self)

        # Create the screens
        self.login_screen = LoginScreen(self.show_registration_screen)
        self.registration_screen = RegistrationScreen(self.show_login_screen)

        # Add screens to stacked widget
        self.stacked_widget.addWidget(self.login_screen)
        self.stacked_widget.addWidget(self.registration_screen)

        # Layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        self.setWindowTitle('Parking App')
        self.setGeometry(100, 100, 400, 300)

        # Show login screen initially
        self.stacked_widget.setCurrentIndex(0)

    def show_registration_screen(self):
        """Switch to Registration screen"""
        self.stacked_widget.setCurrentIndex(1)

    def show_login_screen(self):
        """Switch to Login screen"""
        self.stacked_widget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication([])
    window = AppWindow()
    window.show()
    app.exec_()
