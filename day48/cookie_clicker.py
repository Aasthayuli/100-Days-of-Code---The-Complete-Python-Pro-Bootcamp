# Automated Game Player

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(5) # wait for the page to load


cookie = driver.find_element(By.ID, value="bigCookie")
start_time = time.time()
while time.time() - start_time < 10:
    cookie.click()

try:
    cookies_text = driver.find_element(By.ID, "cookies").text
    cookies_count_str = cookies_text.split()[0].replace(",", "")
    cookies_count = int(cookies_count_str)
    if cookies_count >= 1100:
        farm = driver.find_element(By.ID, "productName2").text
        print("Unlocked product:", farm)
        farm_element = driver.find_element(By.ID, "product2")
        farm_element.click()
    if cookies_count >= 100:
        grandma = driver.find_element(By.ID, "productName1").text
        print("Unlocked product:", grandma)
        grandma_element = driver.find_element(By.ID, "product1")
        grandma_element.click()
    if cookies_count >= 20:
        cursor = driver.find_element(By.ID, "productName0").text
        print("Unlocked product:", cursor)  # Output: Farm
        cursor_element = driver.find_element(By.ID, "product0")
        cursor_element.click()
    if cookies_count >= 12000:
        next_reward = driver.find_element(By.ID, "productName3").text
        print("Unlocked Product: ", next_reward)
        next_reward_element = driver.find_element(By.ID, "product3")
        next_reward_element.click()

    cookies_per_sec = driver.find_element(By.ID, value="cookiesPerSecond")
    print(f"Cookies {cookies_per_sec.text}")
    time.sleep(5)
except Exception as e:
    print("Error:", e)
finally:
    driver.quit()