import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
price= soup.find("span", class_ = "a-size-base")
product = soup.find("span", id="productTitle")
product_name = product.get_text()
current_price = int(price.getText().split("$")[1])

HOST = os.getenv("SMTP_ADDRESS")
FROM = os.getenv("MY_EMAIL")
TO = os.getenv("MY_EMAIL")
PASS = os.getenv("MY_PASSWORD")
PORT = os.getenv("PORT")

if current_price <= 99:
    with smtplib.SMTP(HOST, int(PORT)) as connection:
        connection.starttls()
        connection.login(FROM, PASS)
        msg = EmailMessage()
        msg["Subject"] = "Amazon Price Alert"
        msg["From"] = FROM
        msg["To"] = TO
        msg.set_content(f"{product_name} is now ${current_price}\n{url}", charset="utf-8")

        connection.send_message(msg)

