# login imports
import time
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from profile import Profile
from selenium.webdriver.common.by import By
# txt imports
from os import listdir
from os.path import isfile, join

def login(username, password, driver):
    driver.get("https://www.linkedin.com/")
    actions = ActionChains(driver)

    # login gombra kattintás
    login = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    actions.click(login)
    actions.perform()

    time.sleep(2)

    # adatok beírása
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.clear()
    password_input.clear()
    username_input.send_keys(username)
    password_input.send_keys(password)

    time.sleep(2)

    # sing in gomb megnyomása
    sing_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    actions.click(sing_in_button)
    actions.perform()

# bejelentkezés
driver = webdriver.Chrome(service=Service("chromedriver.exe"))
driver.maximize_window()
login("xisari4995@luxiu2.com", "azsxdcfv", driver)


# lists mappának az elérési útja
PATH = "lists"

# lista a fileokkal
txt_files = [f for f in listdir(PATH) if isfile(join(PATH, f))]

# linkek beolvasása a fileokbol
for file in txt_files:
    open_file = open(PATH + "\\" + file, 'r', encoding='utf-8')

    linkedIn_links = [line.strip().split() for line in open_file]

    for link in linkedIn_links:
        driver.get(link[0])
        time.sleep(2)

        # INFOK KIGYŰJTÉSE
        try:
            p = Profile()
            p.name = driver.find_element(By.CLASS_NAME, "text-heading-xlarge").text
            target_uni = driver.find_element(By.CLASS_NAME, "pv-entity__school-name").text
            target_edu = driver.find_elements(By.CLASS_NAME, "pv-entity__comma-item")
            target_level = target_edu[0].text
            target_major = target_edu[1].text

            print("{0:>35}".format(p.name) + "\t\t\t" + "{0:>10}".format(target_uni) + "\t\t\t" + "{0:>10}".format(target_major) + "\t\t\t" + "{0:>10}".format(target_level) + "\n")
        except:
            print("HIBA")

    open_file.close()






