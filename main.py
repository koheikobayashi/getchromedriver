import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service as fs
import pandas as pd
from get_chrome_driver import GetChromeDriver

get_driver = GetChromeDriver()
get_driver.install()
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : os.getcwd()}
options.add_experimental_option('prefs', prefs)
# options.add_argument('--headless')
# options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)
driver.get("https://admin.thebase.in/users/login")
driver.set_window_size(1449, 1050)
  