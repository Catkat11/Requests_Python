import requests
from bs4 import BeautifulSoup
import smtplib

# URL of the Amazon product page
URL = "https://www.amazon.pl/merci-Finest-Selection-r%C3%B3%C5%BCnorodno%C5%9B%C4%87-czekoladowe/dp/B003SG8TV0/ref=zg_mg_c_grocery_sccl_19/259-3408827-9191213?pd_rd_w=xoKXS&content-id=amzn1.sym.512e8c65-fd1a-405b-8eec-57152fc1e853&pf_rd_p=512e8c65-fd1a-405b-8eec-57152fc1e853&pf_rd_r=FKBEP49PXQE3NE6DEYX3&pd_rd_wg=Bsaed&pd_rd_r=45c16f77-b7cc-4800-b6d1-d5fb059e10be&pd_rd_i=B003SG8TV0&psc=1"

# SMTP configuration
YOUR_SMTP_ADDRESS = "your_smtp_address"
YOUR_EMAIL = "email"
YOUR_PASSWORD = "password"

# Fetching the Amazon page
response = requests.get(URL)
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, "html.parser")

# Extracting the price
price_to_split = soup.find(class_="a-offscreen").get_text()
price_after_split = price_to_split.split("zł")
price_to_replace = price_after_split[0]
price = price_to_replace.replace(",", ".")

# Extracting the title
title = soup.find(id="productTitle").get_text().strip()

# Checking if the price is below 50 zł
if float(price) < 50:
    # Composing the email message
    message = f"{title} is now {price}"

    # Sending the email alert
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon price alert!!!\n\n{message}\n{URL}".encode("utf-8")
        )
