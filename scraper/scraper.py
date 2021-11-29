# login imports
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
# txt imports
from os import listdir, name, replace
from os.path import isfile, join
import profile

#ha változna a linkedin oldala, akkor csak itt kell átírni az xpatheket
namePath = '//section/div[2]/div[2]/div[1]/div[1]/h1'
positionPath1 = '//section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[2]/span[2]'
positionPath2 = '//section/div[2]/div[2]/div[1]/div[2]'
exp_namePath1 = '//section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/h3'
exp_namePath2 = '//section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/h3/span[2]' #amikor egy cégnél több állás is be van írva
exp_companyPath1 = '//section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/p[2]'
exp_companyPath2 = '//section/div[1]/section/ul/li[1]/section/div/a/div/div[2]/h3/span[2]'
exp_datePath1 = '//section/div[1]/section/ul/li[1]/section/div/div/a/div[2]/div/h4[1]/span[2]'
exp_datePath2 = '/html/body/div[7]/div[3]/div/div/div/div/div[3]/div/div/main/div/div/div[5]/span/div/section/div[1]/section/ul/li[1]/section/ul/li[1]/div/div/div/div/div/div/div/h4[1]/span[2]'
study_namePath1 = '//section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p[2]/span[2]'
study_namePath2 = '//section/div[2]/section/ul/li[1]/div/div/a/div[2]/div/p/span[2]'
study_institutionPath = '//section/ul/li[1]/div/div/a/div[2]/div/h3'
study_start_datePath = '//section/div[2]/section/ul/li[1]/div/div/a/div[2]/p/span[2]/time[1]'
study_end_datePath = '//section/div[2]/section/ul/li[1]/div/div/a/div[2]/p/span[2]/time[2]'
cert_namePath = '//section/div[3]/section/ul/li[1]/div/a/div[2]/h3'
cert_institutionPath = '//section/div[3]/section/ul/li[1]/div/a/div[2]/p[1]/span[2]'
cert_datePath = '//section/div[3]/section/ul/li[1]/div/a/div[2]/p[2]/span[2]'



def kinyeres(string, by):
    if by.lower() == "class":
        adat = driver.find_element(By.CLASS_NAME, string).text
    elif by.lower() == "xpath":
        adat = driver.find_element(By.XPATH, string).text
    elif by.lower() == "id":
        adat = driver.find_element(By.ID, string).text
    
    return adat

def login(username, password, driver):
    driver.get("https://www.linkedin.com/")
    actions = ActionChains(driver)

    # login gombra kattintás
    login = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    actions.click(login)
    actions.perform()

    time.sleep(2)

    # adatok beírása
    username_input = driver.find_element(By.ID,"username")
    password_input = driver.find_element(By.ID,"password")
    username_input.clear()
    password_input.clear()
    username_input.send_keys(username)
    password_input.send_keys(password)

    time.sleep(2)

    # sing in gomb megnyomása
    sing_in_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
    actions.click(sing_in_button)
    actions.perform()

def export(profiles, fileName, header):
    #"data.csv"
    #"Név,Pozició,Tapasztalat,Cég,Kezdés,Vég,Szak,Egyetem,Kezdés,Vég,Oklevél,Kiállító,Dátum\n"

    with open(fileName, "w", encoding="utf-8-sig") as f:
        f.write(header)
        for prof in profiles:
            f.write(str(prof)+'\n')

# bejelentkezés
driver = webdriver.Chrome(service=Service("chromedriver.exe"))
driver.maximize_window()
login("bilebe2446@terasd.com", "azsxdcfv", driver)


# lists mappának az elérési útja
PATH = "liststest"

# lista a fileokkal
txt_files = [f for f in listdir(PATH) if isfile(join(PATH, f))]



for file in txt_files:
    open_file = open(PATH + "\\" + file, 'r', encoding='utf-8')
    linkedIn_links = [line.strip() for line in open_file]

    profiles = list()

    for link in linkedIn_links:
        driver.get(link)

        time.sleep(3)
        try:
            name = kinyeres(namePath, by="xpath")
        except:
            print('Not a profile.')
            continue
        try:
            position = kinyeres(positionPath1, by="xpath")
        except:
            try:
                position = kinyeres(positionPath2, by="xpath")
            except:
                print("No position on this profile")
                position = ""
        try:
            exp_name = kinyeres(exp_namePath1, by="xpath")
        except:
            try:
                exp_name = kinyeres(exp_namePath2, by="xpath")
            except:
                print("No exp_name on this profile")
                exp_name = ""
        try:
            exp_company = kinyeres(exp_companyPath1, by="xpath")
        except:
            try:
                exp_company = kinyeres(exp_companyPath2, by="xpath")
            except:
                print("No exp_company on this profile")
                exp_company = ""
        exp_date = ""
        try:
            exp_date = kinyeres(exp_datePath1, by="xpath").split(" – ")
        except:
            try:
                exp_date = kinyeres(exp_datePath2, by="xpath").split(" – ")
            except:
                print("No exp_date on this profile")
                exp_start_date = ""
                exp_end_date = ""
        if exp_date != "":
            exp_start_date = exp_date[0]
            exp_end_date = exp_date[1]
        try:
            study_name = kinyeres(study_namePath1, by="xpath")
        except:
            try:
                study_name = kinyeres(study_namePath2, by="xpath")
            except:
                print("No study_name on this profile")
                study_name = ""
        try:
            study_institution = kinyeres(study_institutionPath, by="xpath")
        except:
            print("No study_institution on this profile")
            study_institution = ""
        try:
            study_start_date = kinyeres(study_start_datePath, by="xpath")
        except:
            print("No study_start_date on this profile")
            study_start_date = ""
        try:
            study_end_date = kinyeres(study_end_datePath, by="xpath")
        except:
            print("No study_end_date on this profile")
            study_end_date = ""
        try:
            cert_name = kinyeres(cert_namePath, by="xpath")
        except:
            print("No cert_name on this profile")
            cert_name = ""
        try:
            cert_institution = kinyeres(cert_institutionPath, by="xpath")
        except:
            print("No cert_institution on this profile")
            cert_institution = ""
        try:
            cert_date = kinyeres(cert_datePath, by="xpath")
            cert_issued = cert_date[7:15]
            if cert_date[15] == "E":
                cert_expires = cert_date[-8:]
            else:
                cert_expires = ""
        except:
            print("No cert_date on this profile")
            cert_date = "" 
            cert_issued = ""
            cert_expires = ""           
        
        time.sleep(2)
        profil = profile.Profile(name, position, exp_name, exp_company, exp_start_date, exp_end_date, study_name, study_institution, study_start_date, study_end_date, cert_name, cert_institution, cert_issued, cert_expires)
        profiles.append(profil)

    open_file.close()
    export(profiles, file[:-4]+'.csv', "name,position,exp_name,exp_company,exp_start_date,exp_end_date,study_name,study_institution,study_start_date,study_end_date,cert_name,cert_institution,cert_issued,cert_expires\n")
