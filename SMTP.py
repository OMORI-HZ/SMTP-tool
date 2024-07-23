import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

# Usage example
smtp_server = 'smtp.example.com'
port = 587
sender_email = 'your_email@example.com'
sender_password = 'your_password'
recipient_email = 'recipient_email@example.com'
subject = 'Test Email'
body = 'This is a test email.'

send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body)
