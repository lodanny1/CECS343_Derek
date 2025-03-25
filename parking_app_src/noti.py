import smtplib

def send_email_notification(to_email, subject, message):
    # Email configuration (update these with your credentials)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"       # Replace with your sender email
    sender_password = "your_email_password"       # Replace with your sender email password or app-specific password

    # Construct the email message
    email_message = f"Subject: {subject}\n\n{message}"
    
    try:
        # Establish connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, email_message)
            print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

# Example usage
if __name__ == "__main__":
    recipient = "recipient@example.com"  # Replace with the recipient's email
    send_email_notification(recipient, "Test Email", "This is a test email notification.")
