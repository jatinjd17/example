import time, os
os.environ['DISPLAY'] = ':0'
from selenium import webdriver
from selenium.webdriver.common.by import By
import names
from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyautogui import hotkey
import undetected_chromedriver as uc
def RunScript():
    # bot = webdriver.Chrome(chrome_options=options)
    options = webdriver.ChromeOptions()
    # options = webdriver.FirefoxOptions()

    options.headless = True
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-popup-blocking')
    # options.add_extension('C:\Users\Momentum_v0.92.2.crx')
    # firstname = (names.get_first_name(gender='male')).lower()
    # lastname = (names.get_last_name()).lower()
    # email = firstname+'_'+lastname+str(random.randrange(400,2000))+'@outlook.com'
    # print(email)
    bot = uc.Chrome(options=options)

    # bot.get('https://www.thehairstyler.com/signup')

    # time.sleep(8)



    # bot.execute_script("document.body.style.zoom='-80%'")

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    bot.get("https://google.com/")
    bot.get("https://themeisle.com/blog/best-grammar-checker-free/")
    time.sleep(5)
    # bot.get("https://languagetool.org/")
    bot.get("https://www.shareasale.com/r.cfm?b=2285581&u=3667753&m=138470")
    time.sleep(25)
    
    bot.quit()

if __name__ == "__main__":
    RunScript()
