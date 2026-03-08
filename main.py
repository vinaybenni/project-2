import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server
smtp_server = 'smtp.example.com'
port = 587  # For starttls
username = 'user@example.com'
password = 'your_password'

# Define the function for sending email

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add in the email body
    msg.attach(MIMEText(body, 'plain'))

    # Create the SMTP session for sending the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(username, password)
        server.send_message(msg)

# Example usage
if __name__ == '__main__':
    subject = 'Test Email'
    body = 'This is a test email from the email automation tool.'
    to_email = 'recipient@example.com'
    send_email(subject, body, to_email)
    print('Email sent!')