from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

ACCOUNT = "chefsteps"
USERNAME ="python20257"
PASSWORD = "inst@1289"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(PASSWORD)
        login_button = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[.//div[text()='Log in']]"))
        )
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", login_button)
        login_button.click()
        sleep(10)
        not_now_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']"))
        )
        not_now_button.click()
        sleep(5)
        # Step 1: Click search icon
        # safer XPath for Search icon (div around SVG or button)
        search_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[name()='svg' and @aria-label='Search']"))
        )

        search_icon.click()
        # Step 2: Enter "chefsteps" and press Enter
        search_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' or @aria-label='Search']"))
        )
        search_input.send_keys("chefsteps")
        search_input.send_keys(Keys.ENTER)

        sleep(5)
        chefsteps_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/chefsteps')]"))
        )
        sleep(5)  # wait before clicking
        chefsteps_link.click()
        sleep(5)  # wait after clicking before next action


    def find_followers(self):
        followers = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'followers')]"))
        )
        followers.click()

    def follow(self):
        sleep(5)
        follow_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button'))
        )
        follow_btn.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()