from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

try:
    time.sleep(5)
    # element = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
    # print(element.text)
    # element.click()

# Find Element by Link Text
#     all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#     all_portals.click()

# Find the "search" <input> by Name
    search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to selenium
    search.send_keys("Python",Keys.ENTER)

# wait to not close instantly
    time.sleep(5)
except Exception:
    print("Error !")
    print(Exception)


driver.quit()