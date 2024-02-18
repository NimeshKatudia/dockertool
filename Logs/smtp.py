import smtplib
from email.message import EmailMessage

# Define the sender and recipient email addresses
sender_email = 'your_email@gmail.com'
recipient_email = 'recipient_email@example.com'

# Create a message object
message = EmailMessage()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Hello from Python!'
message.set_content('This is a test email sent from a Python script.')

# Connect to the SMTP server (in this case, Gmail's SMTP server)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('your_email@gmail.com', 'your_password')
    smtp.send_message(message)

print('Email sent successfully!')