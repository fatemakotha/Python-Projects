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

#Instagram credentials:
INSTA_EMAIL = os.environ.get("insta_email")
INSTA_PASS = os.environ.get("insta_pass")


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=options)
    def login(self):
        pass
    def find_followers(self):
        pass
