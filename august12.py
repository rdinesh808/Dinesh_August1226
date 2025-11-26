import smtplib
import calendar
from datetime import date
from email.message import EmailMessage

APP_PASSWORD = "rgnd aasp wzyx fnhj"
sender_email = "rdinesh808@gmail.com"
receiver_email = "rdinesh808@gmail.com"

start_date = date.today()
end_date = date(2026, 8, 12)
total_days = (end_date - start_date).days
month_counts = {}
current_date = start_date
while current_date <= end_date:
    next_month_year = current_date.year + (1 if current_date.month == 12 else 0)
    next_month = 1 if current_date.month == 12 else current_date.month + 1
    first_day_next_month = date(next_month_year, next_month, 1)
    if first_day_next_month <= end_date:
        days_in_month = (first_day_next_month - current_date).days
    else:
        days_in_month = (end_date - current_date).days + 1
    month_name = calendar.month_name[current_date.month] + " " + str(current_date.year)
    month_counts[month_name] = days_in_month
    current_date = first_day_next_month
print(f"Total remaining days from {start_date} to {end_date}: {total_days}\n")
year_month_details = ""
for month, days in month_counts.items():
    year = month.split()[1]
    curr_month = month.split()[0]
    count_days = days
    year_month_details += f"{month}: {days} days\n"
subject = f"12-August-2026 is coming in {total_days} days"
body = f"""Hi Dinesh,\n\nTotal remaining days from {start_date} to {end_date}: {total_days}\n{year_month_details}\nThanks"""

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