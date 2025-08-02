from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PROMISED_DOWN = 30
PROMISED_UP = 30

TWITTER_EMAIL = "aasthayuli2025@gmail.com"
TWITTER_PASSWORD = "@@sth@2025x"
USERNAME = "@Aasthayuli38972"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(10) # time for loading
        go = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go.click()
        sleep(40) # time for testing
        download_speed_element = self.driver.find_element(By.CLASS_NAME, value="download-speed")
        download_speed = float(download_speed_element.text)
        print(download_speed)
        upload_speed_element = self.driver.find_element(By.CLASS_NAME, value="upload-speed")
        upload_speed = float(upload_speed_element.text)
        print(upload_speed)
        return [download_speed, upload_speed]

    def tweet_at_provider(self, download, upload):
        self.driver.get("https://x.com/")
        sleep(5)
        print("Landed on login page")

        try:
            # Reliable login button click using data-testid
            signin = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="loginButton"]')
            signin.click()
            sleep(10)

            # Proceed with entering email, password, etc.
            try:
                email_input = self.driver.find_element(By.NAME, "text")
                email_input.send_keys(TWITTER_EMAIL)
                email_input.send_keys(Keys.ENTER)
            except:
                print("Error in email filling !")

            sleep(5)

            print("Email input successful !")
            try:
                username_input = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.NAME, "text"))
                )
                username_input.send_keys(USERNAME)
                username_input.send_keys(Keys.ENTER)
                print("Username input successful!")
            except:
                print("Username step skipped.")

            sleep(5)
            try:
                pass_input = self.driver.find_element(By.NAME, "password")
                pass_input.send_keys(TWITTER_PASSWORD)
            except:
                print("Error in filling Password !")

            try:
                login_button = self.driver.find_element(By.XPATH, "//span[text()='Log in']")
                login_button.click()
                print("logging in ...")
            except:
                print("Error in login button !")
            sleep(10)
            print("Twitter Home page Landed !")
            try:

                post_box = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@data-offset-key]"))
                )

                post_box.click()  # Focus on it
                post_box.send_keys(f"Hey Internet Provider, why is my internet speed {download}down/{upload}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            except:
                print("Error in post writing !")

            # Click the Post button
            try:
                post_button = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]'))
                )
                post_button.click()
                print("Tweet posted successfully!")
            except:
                print("Error in post Button clicking !")
        except :
            print("Layout may have changed !")


bot = InternetSpeedTwitterBot()

speeds = bot.get_internet_speed()
down_speed = speeds[0]
up_speed = speeds[1]

bot.tweet_at_provider(down_speed, up_speed)

