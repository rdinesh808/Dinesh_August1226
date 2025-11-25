import smtplib
from datetime import datetime
from email.message import EmailMessage

APP_PASSWORD = "rgnd aasp wzyx fnhj"
sender_email = "rdinesh808@gmail.com"
receiver_email = "rdinesh808@gmail.com"

today = datetime.strptime(datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d")
august_12 = datetime.strptime("2026-08-12", "%Y-%m-%d")
total_days = august_12 - today
day = total_days.days

subject = f"AUGUST - 12 - 2026 Total {day} days left"
body = f"""Hi Dinesh,\n\nYou still need to wait {day} days to 12-August-2026.\n\nThanks"""

message = EmailMessage()
message.set_content(body)
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(sender_email, APP_PASSWORD)
        s.send_message(message)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your email/password.")
except smtplib.SMTPException as e:
    print(f"Error: Failed to send email. {str(e)}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")