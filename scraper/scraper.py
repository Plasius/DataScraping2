# login imports
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# txt imports
from os import listdir
from os.path import isfile, join

def login(username, password, driver):
    driver.get("https://www.linkedin.com/")
    actions = ActionChains(driver)

    # login gombra kattintás
    login = driver.find_element_by_class_name("nav__button-secondary")
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

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
login("bcebitclub@gmail.com", "AsD1AsD2?", driver)

# lists mappának az elérési útja
PATH = "lists"

# lista a fileokkal
txt_files = [f for f in listdir(PATH) if isfile(join(PATH, f))]

# linkek beolvasása a fileokbol
for file in txt_files:
    open_file = open(PATH + "\\" + file, 'r', encoding='utf-8')

    # feldolgozás alatt álló linkek
    linkedIn_links = [line.strip().split() for line in open_file]

    for link in linkedIn_links:
        driver.get(link[0])



    open_file.close()






