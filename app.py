import smtplib
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))



EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

recipients = [
    "devireddymeghana268@gmail.com",
    "sonyjkh819@gmail.com",
    "bhargavi84999@gmail.com"
]

message = """Subject: Python Training Notification

Hello,

This is your trainer Uppara Kalyani.

Please do not reply to this email.

Regards,
Uppara Kalyani
upparakalyani22@gmail.com
"""

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASSWORD)

for receiver in recipients:
    server.sendmail(EMAIL_USER, receiver, message)
    print(f"Email sent successfully to {receiver}")

server.quit()
