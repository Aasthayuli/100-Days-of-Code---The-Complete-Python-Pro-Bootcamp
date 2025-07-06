import smtplib

my_email = "aasthayuli2000@gmail.com"
my_password= "xpgaaxssxlayqkbu"
recipient_email = "divyasah9821@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as connection: # ✅ Correct port
    connection.starttls() # makes the connection secure(enables encryption)
    connection.login(user= my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=recipient_email,
                        msg="subject:Heeeelllllooo....\n\nbody of the mail")



import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2020:
    print("Wear a mask!")
print(type(year))
month = now.month
print(month)
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2002, month=5, day=24, hour=3)
print(date_of_birth)