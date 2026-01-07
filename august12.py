import smtplib
import calendar
from datetime import date
from email.message import EmailMessage
import os

# ---------------- CONFIG ----------------
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")  # set in environment
sender_email = "rdinesh808@gmail.com"
receiver_email = [
    "rdinesh808@gmail.com",
    "dineshrajamanickam177@gmail.com"
]

start_date = date.today()
end_date = date(2026, 8, 12)
birth_day_date = date(2026, 7, 17)

# ---------------- CALCULATIONS ----------------
total_days = (end_date - start_date).days
total_birth_day_days = (birth_day_date - start_date).days

month_counts = {}
year = start_date.year
month = start_date.month

while (year, month) <= (end_date.year, end_date.month):
    days_in_month = calendar.monthrange(year, month)[1]

    # Adjust start month
    if year == start_date.year and month == start_date.month:
        days_in_month -= start_date.day - 1

    # Adjust end month
    if year == end_date.year and month == end_date.month:
        days_in_month = end_date.day

    month_name = f"{calendar.month_name[month]} {year}"
    month_counts[month_name] = days_in_month

    month += 1
    if month == 13:
        month = 1
        year += 1

# ---------------- WISH MESSAGE ----------------
wish_days = "As usual day! Have a wonderful day ahead! 😊"

if start_date == birth_day_date:
    wish_days = "Wish you a very happy birthday Dinesh! Have a great year ahead! 🎉"
elif start_date == end_date:
    wish_days = "Happy 12-August-2026 Dinesh! You completed your goal! 🎉"

# ---------------- EMAIL BODY ----------------
year_month_details = ""
for month, days in month_counts.items():
    year_month_details += f"{month} : {days} days\n"

subject = f"12-August-2026 is coming in {total_days} days"

body = f"""Hi Dinesh,

Today Date : {start_date}

Total days for birthday from {start_date} to {birth_day_date} : {total_birth_day_days} days
Total remaining days from {start_date} to {end_date} : {total_days} days

Month-wise breakdown:
{year_month_details}

{wish_days}

Thanks
"""

# ---------------- SEND EMAIL ----------------
message = EmailMessage()
message.set_content(body)
message["Subject"] = subject
message["From"] = sender_email
message["To"] = ", ".join(receiver_email)

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(sender_email, APP_PASSWORD)
        s.send_message(message)
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check app password.")
except Exception as e:
    print(f"Error: {e}")
