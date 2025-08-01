from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

try:
    time.sleep(5)

    f_name = driver.find_element(By.NAME, value="fName")
    f_name.send_keys("Aastha")
    m_name = driver.find_element(By.NAME, value="lName")
    m_name.send_keys("yuli")
    email = driver.find_element(By.NAME, value="email")
    email.send_keys("aasthayuli2000@gmail.com")
    sign_up = driver.find_element(By.CLASS_NAME, value="btn")
    sign_up.click()
    time.sleep(5)
except Exception:
    print("Error !")
    print(Exception)
finally:
    driver.quit()