import time, os 
from selenium import webdriver
from selenium.webdriver.common.by import By
# from random import randrange
import random
import names
from itertools import islice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
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
options.add_argument("--start-fullscreen")
time.sleep(2)

def RunScript():
    bot = webdriver.Chrome(chrome_options=options)

    

    # bot.execute_script("document.body.style.zoom='-80%'")

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

    bot.get('https://dlupload.com/filedetail/458502228')

    # time.sleep(4)

    #bot.execute_script("document.body.style.zoom='70%'")

    time.sleep(3)

    # bot.get('https://www.thetriviabuff.com/rachael-ray-cookware/')

    

    
    

    # time.sleep(3)

    # frame_0 = bot.find_element_by_class_name('vs_main_frame')
    # bot.switch_to.frame(frame_0)

    # bot.execute_script("document.body.style.zoom='70%'")

    # firstname = names.get_first_name()
    # lastname = names.get_last_name()
    # email = (firstname + lastname + str(random.randrange(51000,2000000)) + '@gmail.com').lower()

    
    bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div[2]/div/div[3]/div[2]/div/div').click()


    time.sleep(4)

    bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[1]/div[1]/div[2]/div').click()

    time.sleep(7)

    bot.find_element_by_xpath('//*[@id="watch_video1"]/div/div/div[1]/button/span').click()

    time.sleep(8)

    bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[1]/div[1]/div[4]').click()

    time.sleep(15)

    bot.find_element_by_xpath('//*[@id="chooseTopic"]/div/div/div[1]/button/span').click()

    time.sleep(8)

    bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[1]/div[1]/div[6]').click()

    time.sleep(4)

    bot.switch_to.window(bot.window_handles[0])

    time.sleep(10)

    bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[1]/div[1]/div[7]').click()

    time.sleep(8)

    WebDriverWait(bot, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))

    # WebDriverWait(bot, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='google_esf'][src^='https://googleads.g.doubleclick.net/pagead/html/r20230308/r20190131/zrt_lookup.html']")))
    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

    time.sleep(15)

    bot.switch_to.default_content()

    # iframe = bot.find_element_by_xpath('//*[@id="google_esf"]')

    # bot.switch_to.frame(iframe)

    time.sleep(2)

    bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[2]/div[2]').click()
    #                         'google_esf'
    # 'https://googleads.g.doubleclick.net/pagead/html/r20230308/r20190131/zrt_lookup.html'
    # '//*[@id="google_esf"]'

    time.sleep(3)


    yy = bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/h5')

    print(yy.text)

    # bot.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[5]/div[2]/div/div/div[2]/center/div/div/div[1]/a/div').send_keys(Keys.TAB)

    # actions = ActionChains(bot) 

    # actions.send_keys(Keys.TAB)

    # time.sleep(5)

    # actions.send_keys(Keys.ENTER)

    time.sleep(8)

   
    

    # # '//*[@id="last_name"]'

    # # '//*[@id="email"]'

    # bot.find_element_by_xpath('//*[@id="email"]').send_keys(email)

    # print(email)

    # time.sleep(1)
    # bot.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.ENTER)
    # # bot.find_element_by_xpath('//*[@id="entry-form"]/div[7]/a').click()

    # # time.sleep(1)

    # bot.switch_to.default_content()

    # time.sleep(3)

    # yy = bot.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/b')

    # print(yy.text)

    # # '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/b'

    # # vv = bot.find_element_by_xpath('//*[@id="entry-form"]/div[6]/span/label/p/font')

    # # print(vv)


    



    time.sleep(20)
    bot.quit()


if __name__ == "__main__":
    RunScript()
