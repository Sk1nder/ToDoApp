import smtplib
from config import MY_EMAIL, MY_PASSWORD



def send_email(from_address, name, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=from_address,
            to_addrs=MY_EMAIL,
            msg=f"Subject: New Message from {name}\n\n{from_address},\n{body}")

