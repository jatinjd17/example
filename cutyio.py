import time, os 
from selenium import webdriver
from selenium.webdriver.common.by import By
# from random import randrange
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from scrapy.selector import Selector
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io
import base64


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
    
    bot.get('https://cuty.io/I3kl1')

    time.sleep(10)
    bot.save_screenshot('0011.png')

    



    time.sleep(25)
    print(done)
    bot.quit()


if __name__ == "__main__":
    RunScript()
