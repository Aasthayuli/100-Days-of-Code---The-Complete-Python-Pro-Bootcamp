import smtplib
import datetime as dt
import random


MY_EMAIL = "aasthayuli2000@gmail.com"
MY_PASSWORD = "xpgaaxssxlayqkbu"
RECIPIENT_EMAIL = "Tanyatanu1300@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIPIENT_EMAIL,
                            msg=f"Subject:Thursday Motivation\n\n{quote}")

