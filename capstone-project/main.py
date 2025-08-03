import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://appbrewery.github.io/Zillow-Clone/"
header = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
price= soup.find_all("span",class_="PropertyCardWrapper__StyledPriceLine")
# price_list = [price.get_text() for price in price]
price_list2 = [price.get_text().replace('$', '').replace('+', '').replace('/mo', '').replace(',', '').strip() for price in price]
print(price_list2)

address_elements = soup.find_all("address", attrs={"data-test": "property-card-addr"})
address_list = [addr.get_text(strip=True) for addr in address_elements]
print(address_list)

# Find all property detail lists
detail_lists = soup.find_all("ul", class_="StyledPropertyCardHomeDetailsList")
# Extract and format details
details = []
for detail in detail_lists:
    items = detail.find_all("li")
    text_parts = []
    for item in items:
        value = item.find("b").get_text(strip=True)
        unit = item.find("abbr").get_text(strip=True)
        text_parts.append(f"{value} {unit}")
    details.append(" ".join(text_parts))

print(details)

# Get all <a> tags with the property-card-link class or data-test attribute
link_tags = soup.find_all("a", attrs={"data-test": "property-card-link"})
# Extract the href from each tag
property_links = [tag["href"] for tag in link_tags if tag.get("href")]
print(property_links)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for n in range(len(property_links)):
    driver.get("https://forms.gle/N982A3jyrCJbEyUj7")
    sleep(5)
    address_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(address_list[n])

    price_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price_list2[n])

    link_field = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(property_links[n])

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()

    sleep(5)



driver.quit()

