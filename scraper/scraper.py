# login imports
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# txt imports
from os import listdir, name
from os.path import isfile, join
import profile


def kinyeres(string, by):
    if by.lower() == "class":
        adat = driver.find_element(By.CLASS_NAME, string).text
    elif by.lower() == "xpath":
        adat = driver.find_element(By.XPATH, string).text
    elif by.lower() == "id":
        adat = driver.find_element(By.ID, string).text
    return adat

def login(username, password, driver):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # adatok beírása
    username_input = driver.find_element(By.ID,"username")
    username_input.send_keys(username)
    time.sleep(2)


    password_input = driver.find_element(By.ID,"password")
    password_input.send_keys(password)
    time.sleep(2)

    password_input.send_keys(Keys.RETURN)


def export(profiles, fileName, header):
    with open('output'+'\\'+fileName, "w", encoding="utf-8-sig") as f:
        f.write(header)
        for prof in profiles:
            f.write(str(prof)+'\n')

# bejelentkezés
driver = webdriver.Chrome(service=Service("chromedriver.exe"))
driver.maximize_window()


with open('fake_account.txt', 'r') as login_file:
    login(login_file.read(), login_file.read(), driver)


# lists mappának az elérési útja
PATH = "lists"

# lista a fileokkal
txt_files = [f for f in listdir(PATH) if isfile(join(PATH, f))]



for file in txt_files:
    organizationFile = open(PATH + "\\" + file, 'r', encoding='utf-8')
    urls = [line.strip() for line in organizationFile]

    profiles = list()

    for link in urls:
        driver.get(link)
        time.sleep(5)

        try:
            name = kinyeres('text-heading-xlarge', by='class')
        except:
            print('Not a profile:', link)
            continue

        try:
            bio = kinyeres('text-body-medium', by="class")
        except:
            print("No bio on this profile")
            bio = ""

        #EXPERIENCE
        foundExperience = False
        position = ''
        company = ''
        exp_start_date = ''
        exp_end_date = ''


        # EXP BLOCK 1
        try:
            experience_block = driver.find_element(By.CLASS_NAME, 'pv-entity__summary-info')
            position = experience_block.find_element(By.CLASS_NAME, 't-16').text

            uni_block = driver.find_element(By.CLASS_NAME, 'pv-entity__degree-info')
            university = uni_block.find_element(By.CLASS_NAME, 'pv-entity__school-name').text

            if position == university:
                experience_block = ''
                position = ''
        except:
            try:
                experience_block = driver.find_element(By.CLASS_NAME, 'pv-entity__summary-info')
            except:
                experience_block = ''

        if experience_block != '':
            foundExperience = True
            try:
                position = experience_block.find_element(By.CLASS_NAME, 't-16').text
            except:
                position = ''
            
            try:
                company =  experience_block.find_element(By.CLASS_NAME, 'pv-entity__secondary-title').text
                if company[-4:] == 'time':
                    company = ' '.join(company.split(' ')[:-1])
            except:
                company = ''

            try:
                exp_date = experience_block.find_element(By.CLASS_NAME, 'pv-entity__date-range')
                exp_date = exp_date.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text
                if(len(exp_date)>4):
                        exp_start_date = exp_date.split('–')[0]
                        exp_end_date = exp_date.split('–')[1].split(' · ')[0]
                else:
                    exp_start_date = exp_date
            except:
                exp_start_date = ''
                exp_end_date = ''
        else:
            pass

        # EXP BLOCK 2
        try:
            experience_block = driver.find_element(By.CLASS_NAME, 'pv-entity__summary-info-v2')
            position = experience_block.find_element(By.CLASS_NAME, 't-14').find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text

            uni_block = driver.find_element(By.CLASS_NAME, 'pv-entity__degree-info')
            university = uni_block.find_element(By.CLASS_NAME, 'pv-entity__school-name').text

            if position == university:
                experience_block = ''
                position = ''
        except:
            try:
                experience_block = driver.find_element(By.CLASS_NAME, 'pv-entity__summary-info-v2')
            except:
                experience_block = ''


        if experience_block != '':
            foundExperience = True
            try:
                position = experience_block.find_element(By.CLASS_NAME, 't-14').find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text
            except:
                position = ''
            
            try:
                company =  driver.find_elements(By.CLASS_NAME, 'pv-entity__company-summary-info')[0].find_elements(By.CLASS_NAME, 't-16')[0].find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text
                if company[-4:] == 'time':
                    company = ' '.join(company.split(' ')[:-1])
            except:
                company = ''
            
            try:
                exp_date = experience_block.find_element(By.CLASS_NAME, 'pv-entity__date-range')
                exp_date = exp_date.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text
                if(len(exp_date)>4):
                        exp_start_date = exp_date.split('–')[0]
                        exp_end_date = exp_date.split('–')[1].split(' · ')[0]
                else:
                    exp_start_date = exp_date
            except:
                exp_start_date = ''
                exp_end_date = ''
        else:
            pass
            
        
        if not foundExperience:
            print('nincs tapasztalat')
        
        # STUDY
        
        try:
           uni_block = driver.find_element(By.CLASS_NAME, 'pv-entity__degree-info') 
        except:
            uni_block = ''
            print('nincs tanulmany', name)


        if uni_block != '':
            try:
                university = uni_block.find_element(By.CLASS_NAME, 'pv-entity__school-name').text
            except:
                university = ''

            try:
                degree = uni_block.find_element(By.CLASS_NAME, 'pv-entity__fos').find_element(By.CSS_SELECTOR, 'span:nth-child(2)').text
            except:
                try:
                    degree = uni_block.find_element(By.CLASS_NAME, 'pv-entity__comma-item').text
                except:
                    degree = ''

            try:
                uni_block = driver.find_elements(By.CLASS_NAME, 'pv-entity__dates')[0]
                study_start_date = uni_block.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').find_element(By.CSS_SELECTOR, 'time:nth-child(1)').text
                study_end_date = uni_block.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').find_element(By.CSS_SELECTOR, 'time:nth-child(2)').text
            except:
                try:
                    study_start_date = uni_block.find_element(By.CSS_SELECTOR, 'span:nth-child(2)').find_element(By.CSS_SELECTOR, 'time:nth-child(1)').text
                    study_end_date = ''
                except:
                    study_start_date = ''
                    study_end_date = ''
        else:
            university = ''
            degree = ''
            study_start_date = ''
            study_end_date = ''
        

        profil = profile.Profile(name, bio, position, company, exp_start_date, exp_end_date, university, degree, study_start_date, study_end_date)
        profiles.append(profil)

    organizationFile.close()
    export(profiles, file[:-4]+'.csv', 'Név,Bio,Pozició,Cég,Kezdés,Vég,Szak,Egyetem,Kezdés,Vég\n')

driver.close()
