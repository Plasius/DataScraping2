# login imports
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
# txt imports
from os import listdir
from os.path import isfile, join
import profile

#függvények
def kinyeres(string, by):
    if by.lower() == "class":
        adat = driver.find_element_by_class_name(string).text
    elif by.lower() == "xpath":
        adat = driver.find_element_by_xpath(string).text
    elif by.lower() == "id":
        adat = driver.find_element_by_id(string).text
    
    return adat

#változók
namePath = "//section/div[2]/div[2]/div[1]/div[1]/h1"
aboutPath= "/html/body/div[7]/div[3]/div/div/div/div/div[3]/div/div/main/div/div/div[3]/section/div"

#profil loopon belül:
profilok = list()
nev = kinyeres(namePath, by="xpath")
time.sleep(2)
try:
    about = kinyeres(aboutPath, by="xpath").strip("…\nsee more").replace("\n", " ")
except:
    print("No about section on this profile")
    about = ""
time.sleep(2)
profilok.append(profile.Profile(nev, about))
