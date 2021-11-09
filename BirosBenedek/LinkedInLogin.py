
# Profil felhasználóneve
username = "bcebitclub@gmail.com"
# Profil jelszava
password = "AsD1AsD2?"

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/")

# login gombra kattintás
login = driver.find_element_by_class_name("nav__button-secondary")
actions = ActionChains(driver)
actions.click(login)
actions.perform()

time.sleep(2)

# adatok beírása
username_input = driver.find_element_by_id("username")
password_input = driver.find_element_by_id("password")
username_input.clear()
password_input.clear()
username_input.send_keys(username)
password_input.send_keys(password)

time.sleep(2)

# sing in gomb megnyomása
sing_in_button = driver.find_element_by_class_name("btn__primary--large")
actions.click(sing_in_button)
actions.perform()

driver.get('https://hu.linkedin.com/in/izsak-attila?')

