import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# webdriver: Used to launch and control the browser (like Chrome).
# By: Helps to locate elements using various methods (like class name, ID, tag name, etc.).
# Service: (optional here, used when you want to manage the ChromeDriver service manually).
# WebDriverWait: Used to wait for elements to load properly.
# expected_conditions (EC): Used with WebDriverWait to wait for specific conditions (like element being present).


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ChromeOptions: Lets you customize how Chrome runs.
# .add_experimental_option("detach", True): Keeps the Chrome browser window open even after the script finishes.


driver = webdriver.Chrome(options=chrome_options)
# This launches a new Chrome browser window using the options you've set.


driver.get("https://www.amazon.in/Lavie-Womens-Ushawu-Satchel-Handbag/dp/B0D2DMVH1V")
# Opens the Amazon product page for the Lavie handbag.


# try:
#     # Wait up to 10 seconds for the price element to appear
#     price_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
#     )
#     print(f"The price is ₹{price_element.text}")
# except:
#     print("Price element not found.")

# try:
#     # Wait up to 10 seconds because I gave some time to load the page
#     time.sleep(10)
#     search_bar = driver.find_element(By.NAME, value="field-keywords")
#     print(search_bar.get_attribute("placeholder"))
# except:
#     print("element not found.")

# try:
#     time.sleep(10)
#     button = driver.find_element(By.ID, value="buy-now-button")
#     print(button.size)
# except:
#     print("Button not found.")

try:
    time.sleep(10)
    product_closure_type = driver.find_element(By.XPATH, value='//*[@id="productFactsDesktopExpander"]/div[1]/div[1]/div[1]/div/div[2]/span/span')
    print(product_closure_type.text)


except:
    print("Button not found.")


# driver.close()  #closes the particular tab
driver.quit()  # closes the whole browser