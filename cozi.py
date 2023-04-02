import time, os 
from selenium import webdriver
from selenium.webdriver.common.by import By
# from random import randrange
import names
from random import randrange


print("INIT")
options = webdriver.ChromeOptions()
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
#options.add_argument('--window-size=1920,1080')
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled") 

 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
# # options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--log-level=3")
# options.add_argument(r"--user-data-dir=C:\Users\jatin\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument('profile-directory=Default')
# options.add_argument('--window-size=1920,1080')
options.add_argument("--headless")
time.sleep(2)



def RunScript():
    bot = webdriver.Chrome(chrome_options=options)
    gname = '@gmail.com'
    fullname = names.get_full_name()
    firstname = fullname.split(" ",1)
    email = fullname.replace(" ","")+str(randrange(40000))+gname
    print(email)

    

    # bot.execute_script("document.body.style.zoom='-80%'")

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

    bot.get('https://www.shareasale.com/r.cfm?b=2092437&u=3595269&m=128168')
    
    time.sleep(3)

    bot.get('https://my.cozi.com/signup/')

    time.sleep(4)



    ######################################################STSRT##########################################
    bot.find_element_by_xpath("//*[@id='first_name']").send_keys(firstname[0])
    #####################################################
    time.sleep(1)

    bot.find_element_by_xpath("//*[@id='email']").send_keys(email)
    #####################################################
    time.sleep(1)

    bot.find_element_by_xpath("//*[@id='password']").send_keys("Jakewill@123")
    #####################################################
    time.sleep(1)

    bot.find_element_by_xpath("//*[@id='household_name']").send_keys(firstname[0])
    #####################################################
    time.sleep(1)

    bot.find_element_by_xpath("//*[@id='app']/main/div[2]/div/div[1]/div/div[1]/div/button") \
        .click()
    
    
    


    



    time.sleep(8)
    print('Done!!!')
    time.sleep(2)
    bot.quit()


if __name__ == "__main__":
    RunScript()
