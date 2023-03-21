import time, os 
from selenium import webdriver
from selenium.webdriver.common.by import By
# from random import randrange
import random
import names
from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io


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

    bot.get("https://email-fake.com/")

    time.sleep(3)

    emaill = bot.find_element_by_css_selector('#email_ch_text')

    email = emaill.text

    print(email)


    bot.execute_script("window.open('https://www.google.com');")

    bot.switch_to.window(bot.window_handles[1])

    time.sleep(2)

    # bot.get("https://www.shareasale.com/r.cfm?b=1261297&u=2885514&m=83604")
    # time.sleep(6)

    bot.get('https://www.shareasale.com/r.cfm?b=15440&u=2874505&m=4421')

    time.sleep(3)

    bot.get('https://www.thehairstyler.com/signup')

    time.sleep(8)

    try:

        bot.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[1]').click()
    except:
        pass

    fname = names.get_first_name(gender='male')


    bot.find_element_by_xpath('//*[@id="user_first_name"]').send_keys(fname)

    lastname = names.get_last_name()

    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="user_last_name"]').send_keys(lastname)

    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="user_email"]').send_keys(email)

    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="user_password"]').send_keys("Jatin@123")
    
    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="user_password_confirmation"]').send_keys("Jatin@123")

    # '//*[@id="last_name"]'

    # '//*[@id="email"]'

    WebDriverWait(bot, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title^='reCAPTCHA']")))

    # WebDriverWait(bot, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='google_esf'][src^='https://googleads.g.doubleclick.net/pagead/html/r20230308/r20190131/zrt_lookup.html']")))
    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()


    time.sleep(10)


    bot.switch_to.default_content()


    time.sleep(1)

    bot.find_element_by_xpath('//*[@id="submitBtn"]').click()

    time.sleep(5)

    aa = bot.find_element_by_css_selector('body > div.container > div:nth-child(4) > div > h1')

    print(aa.text)


    time.sleep(1)

    bot.switch_to.window(bot.window_handles[0])


    time.sleep(1)



    bot.get("https://email-fake.com/")


    time.sleep(5)

    # bot.execute_script("document.body.style.zoom='45%'")

    html = bot.find_element_by_tag_name('html')
    html.send_keys(Keys.END)

    time.sleep(2)

    bot.find_element_by_css_selector('div.fem.mess_bodiyy > p + p + p > a').click()


    


    # bot.find_element_by_xpath('//*[@id="email-table"]/div[2]/div[4]/div[3]/p[3]/a').click()


    # bot.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div[2]/div[4]/div[3]/p[3]/a').click()
    


    

    



    time.sleep(25)
    print(done)
    bot.quit()


if __name__ == "__main__":
    RunScript()
