from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

the_dictionary = {}

try:
    time.sleep(5)
    for i in range(1,6):
        the_list = driver.find_element(By.XPATH,value=f"//*[@id='content']/div/section/div[2]/div[2]/div/ul/li[{i}]")
        time = the_list.find_element(By.CSS_SELECTOR, value="time")
        event = the_list.find_element(By.CSS_SELECTOR, value="a")
        the_dict = {"time":f"{time.text}", "name" : f"{event.text}"}
        the_dictionary[i-1] = the_dict
    print(the_dictionary)
except Exception:
    print("Error!" + str(Exception))


driver.quit()