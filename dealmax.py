import time, os 
from selenium import webdriver
from selenium.webdriver.common.by import By
# from random import randrange
import random
import names
from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from scrapy.selector import Selector
from selenium.common.exceptions import NoSuchElementException
import io
from PIL import Image
import base64
from fake_useragent import UserAgent


print("INIT")
options = webdriver.ChromeOptions()
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
options.add_argument('--window-size=1920,1080')
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

    

    # bot.execute_script("document.body.style.zoom='-80%'")

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

    bot.get('https://www.shareasale.com/r.cfm?b=449385&u=3160921&m=45462')

    time.sleep(4)

    bot.get('https://www.thetriviabuff.com/rachael-ray-cookware/')

    

    
    

    time.sleep(3)

    frame_0 = bot.find_element_by_class_name('vs_main_frame')
    bot.switch_to.frame(frame_0)

    bot.execute_script("document.body.style.zoom='70%'")

    firstname = names.get_first_name()
    lastname = names.get_last_name()
    email = (firstname + lastname + str(random.randrange(51000,2000000)) + '@gmail.com').lower()

    
    bot.find_element_by_xpath('//*[@id="first_name"]').send_keys(firstname)

    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="last_name"]').send_keys(lastname)

    time.sleep(1)

    # '//*[@id="last_name"]'

    # '//*[@id="email"]'

    bot.find_element_by_xpath('//*[@id="email"]').send_keys(email)

    print(email)

    time.sleep(1)
    bot.find_element_by_xpath('//*[@id="entry-form"]/div[7]/a').click()

    # time.sleep(1)

    bot.switch_to.default_content()

    time.sleep(3)

    yy = bot.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/b')

    print(yy.text)

    # '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/b'

    # vv = bot.find_element_by_xpath('//*[@id="entry-form"]/div[6]/span/label/p/font')

    # print(vv)


    



    time.sleep(3)
    bot.quit()


if __name__ == "__main__":
    RunScript()
