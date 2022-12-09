from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import os
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

SIMILAR_ACCOUNT = "chefsteps"

#Instagram credentials:
INSTA_EMAIL = os.environ.get("insta_email")
INSTA_PASS = os.environ.get("insta_pass")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=options)
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        time.sleep(3)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(INSTA_EMAIL)
        time.sleep(3)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(INSTA_PASS)
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        time.sleep(8)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR, "._ab8w ._ac8f button")
        not_now_button.click()# works
        time.sleep(4)
        # make sure to copy the FULL XPATH or it wont work **
        notif_off = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notif_off.click()

        pass
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
    def follow(self):
        pass

bot = InstaFollower()
bot.login()
bot.find_followers()
# bot.follow()






