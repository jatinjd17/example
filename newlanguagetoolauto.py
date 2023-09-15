import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests import get, post
import json
import undetected_chromedriver as uc


ipp = get('https://api.ipify.org').content.decode('utf8')
print(ipp)
url = 'https://languagetoolserververcel.vercel.app/verifyip'
myobj = {'ip': ipp}
headers = {'content-type': 'application/json'}

x = post(url, data=json.dumps(myobj), headers=headers)

ipisusedornot = x.text


istrigger = get('https://languagetoolserververcel.vercel.app/').content.decode('utf8')
print(istrigger)

def firstthing():
    print('1stttttt')
    options = webdriver.ChromeOptions()
    # options.headless = True
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-popup-blocking')
    # options.add_argument('--load-extension=C:/Users/jatin/OneDrive/Desktop/Langua/Grammar')
    options.add_argument('--load-extension=/usr/local/share/ubuntuserver/Grammar')
    bot = uc.Chrome(version_main=116,options=options)
    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    bot.get("https://google.com/")
    bot.get("https://themeisle.com/blog/best-grammar-checker-free/")
    time.sleep(5)
    # bot.get("https://languagetool.org/")
    bot.get("https://www.shareasale.com/r.cfm?b=2285581&u=3667753&m=138470")
    time.sleep(15)
    bot.switch_to.window(bot.window_handles[1])
    time.sleep(2)
    try:
        WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Okay, got it')]"))).click()
    except:
        pass
    time.sleep(2)
    try:
        WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start using LanguageTool')]"))).click()
    except:
        pass
    time.sleep(2)
    try:    
        WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).click()
    except:
        pass
    time.sleep(3)
    get_url = bot.current_url
    print("The current url is33333:"+str(get_url))
    time.sleep(8)
    WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/textarea"))).send_keys('Show me the best Food')
    time.sleep(5)
    bot.quit()

def secondthing():
    print('2ndddddddddd')
    options = webdriver.ChromeOptions()
    # options.headless = True
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-popup-blocking')
    bot = uc.Chrome(version_main=116, options=options)
    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    bot.get("https://google.com/")
    bot.get("https://themeisle.com/blog/best-grammar-checker-free/")
    time.sleep(5)
    # bot.get("https://languagetool.org/")
    bot.get("https://www.shareasale.com/r.cfm?b=2285581&u=3667753&m=138470")
    time.sleep(25)
    bot.quit()

if istrigger == 'nolinktrigger' and ipisusedornot == 'ip-never-used':    
    secondthing()
elif istrigger == 'trigger' and ipisusedornot == 'ip-never-used':
    firstthing()   
else:
    print('IP already used. Soo not triggering any def')
