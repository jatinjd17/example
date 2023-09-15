import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
def RunScript():
    # bot = webdriver.Chrome(chrome_options=options)
    options = webdriver.ChromeOptions()
    # options = webdriver.FirefoxOptions()

    # options.headless = True
    # options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-popup-blocking')
    # options.add_argument('--load-extension=C:/Users/jatin/OneDrive/Desktop/Langua/Grammar')
    options.add_argument('--load-extension=/usr/local/share/ubuntuserver/Grammar')
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
    bot.get("https://languagetool.org/")
    # bot.get("https://www.shareasale.com/r.cfm?b=2285581&u=3667753&m=138470")
    # time.sleep(5)
    # WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="addon-link"]/a'))).click()
    # time.sleep(5)
    # bot.switch_to.window(bot.window_handles[1])
    # #bot.get("https://chrome.google.com/webstore/detail/grammar-checker-paraphras/oldceeleldhonbafppcapldpdifcinji?utm_source=lt-homepage")
    # #time.sleep(60)
    # #'Add to Chrome' webstore-test-button-label
    # WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Add to Chrome')]"))).click()
    #WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div/div/div/div'))).click()

    # time.sleep(5)

    # keyboard.send('left')

    # time.sleep(2)

    # keyboard.send('enter')

    # # hotkey('left', 'enter')
    # # time.sleep(4)


    # time.sleep(15)
    # bot.switch_to.window(bot.window_handles[2])

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


    #/html/body/div[3]/div[2]/div/textarea




    #html = bot.find_element(By.XPATH, '/')
    #html.send_keys(Keys.TAB)

    #class="Je-qe-zd-Ge hg S-Zb-U Pj"
    time.sleep(5)
    bot.quit()

if __name__ == "__main__":
    RunScript()
