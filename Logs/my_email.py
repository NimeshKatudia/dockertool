import smtplib
import os
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Create the email message
msg = MIMEMultipart()
msg['From'] = 'krisha.rathod2023@tsecedu.org'
msg['To'] = 'nimeshkatudia9@gmail.com'
msg['Subject'] = 'Log File'

# Get the path to the log file
log_file_path = 'log.json'

# Set the body of the email
body = 'Please find attached the log file.'
msg.attach(MIMEText(body, 'plain'))

# Open the log file and attach it to the email
with open(log_file_path, 'rb') as attachment:
    mime_type, _ = mimetypes.guess_type(log_file_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    part = MIMEBase(mime_type, mime_subtype)
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(log_file_path))
    msg.attach(part)

# Send the email
smtp_server = 'smtp.microsoft.com'
smtp_port = 587
smtp_username = 'jimil.shah279@svkmmumbai.onmicrosoft.com'
smtp_password = ''

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)

print('Email sent successfully')
