from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
#To press enter and everything:
from selenium.webdriver.common.keys import Keys
import os
import time


options = webdriver. ChromeOptions()
options. add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://tinder.com/")

PROMISED_UP = 150
PROMISED_DOWN = 10
TWITTER_EMAIL = "AriaSmi91565684"
TWITTER_PASS = "EAm*25?^#&p=J?j"

class InternetSpeedTwitterBot:
    def __init__(self, up, down):
        pass

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass
