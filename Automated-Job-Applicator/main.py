from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Login
def login(your_email, your_password):
    driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account")
    time.sleep(5)
    try:
        email = driver.find_element(By.ID, value="username")
        email.send_keys(your_email)
        password = driver.find_element(By.ID, value="password")
        password.send_keys(your_password)
        login_btn = driver.find_element(By.CLASS_NAME,value="btn__primary--large")
        login_btn.click()
    except:
        print("Error while logging in !")
        print("Might be checking for some security and This Bot stucked !")
    finally:
        print("If Bot is not stucked, landing to feed....")

try:
    login("your_email", "your_password")
    time.sleep(15)
    print("login successful!")
except:
    print("Error in Loading the feed !")
    print("Can't proceed further !")
finally:
    print("If feed loading is completed, proceeding further")

search = driver.find_element(By.CLASS_NAME, value="basic-input")
search.send_keys("python developer", Keys.ENTER)
time.sleep(5)
print("Search completed and landed to the next page successfully !")

see_all = driver.find_element(By.LINK_TEXT, value="See all job results in United Kingdom")
see_all.click()
time.sleep(5)
print("Seeing all jobs...")

time.sleep(6)
apply = driver.find_element(By.ID, value="jobs-apply-button-id")
apply.click()
print("Easy apply clicked !")

try:

    phone_number = driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4278539090-22644792930-phoneNumber-nationalNumber"]')
    phone_number.send_keys("9576357966")
    print("phone number filled successfully !")
except:
    print("Error while filling phone number !")

try:
    next_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Continue to next step')]"))
    )
    driver.execute_script("arguments[0].click();", next_btn)
    driver.execute_script("arguments[0].click();", next_btn)
    print("button clicked !")
    try:
        next_btn2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Continue to next step')]"))
        )
        if next_btn2:
            back = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Back to previous step')]"))
            )
            driver.execute_script("arguments[0].click();", back)
    except:
        print("No next buton.")
except:
    print("Error !")
finally:
    print("Quitting ...")
    time.sleep(5)
    driver.quit()






