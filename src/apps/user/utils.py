import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Send the email
def sendEmail(correo, code):
# Set up the SMTP server
  username = os.getenv('EMAIL')
  password = os.getenv('EMAIL_PASSWORD')

  # Create the email content
  msg = MIMEMultipart()
  msg['From'] = username
  msg['To'] = correo
  msg['Subject'] = 'Codigo de inicio de session'

  # Add the email body
  body = code
  msg.attach(MIMEText(body, 'plain'))
  try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(username, password)
        smtp_server.sendmail(username, correo, msg.as_string())
        return 'Email sent successfully!'
  except Exception as e:
      raise Exception(f'Failed to send email: {e}')


