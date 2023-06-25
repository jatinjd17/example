import speech_recognition as sr
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import sys
import urllib
import pydub

import re
# from pymongo import MongoClient
import certifi

# options = webdriver.ChromeOptions() 
# # options.headless = True
# options.add_argument('--disable-popup-blocking')
# bot = uc.Chrome(options=options)
# bot.get('https://login.live.com/login.srf')

# client = MongoClient(host="mongodb+srv://jatin:jatin123@cluster0.1zrdh.mongodb.net/outlookmail?retryWrites=true&w=majority",tlsCAFile=certifi.where(),connect=False)
# collection = client.get_database("outlookmail").get_collection("newmail2")


count = 1
# print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')



    # print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')


options = webdriver.ChromeOptions() 
# options.headless = True
options.add_argument('--headless')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-popup-blocking')
# firstname = (names.get_first_name(gender='male')).lower()
# lastname = (names.get_last_name()).lower()
# email = firstname+'_'+lastname+str(random.randrange(400,2000))+'@outlook.com'
# print(email)
bot = uc.Chrome(options=options)

bot.get('https://www.google.com/')
time.sleep(3)
bot.save_screenshot('001.png')
bot.get('https://cuty.io/I3kl1')

time.sleep(5)

try:
    bot.save_screenshot('01.png')

    element1 = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]")))
except Exception as e:
    print('yoooo')
    print(e)
    print('noooooo')

time.sleep(4)



desired_y = (element1.size['height'] / 2) + element1.location['y']
window_h = bot.execute_script('return window.innerHeight')
window_y = bot.execute_script('return window.pageYOffset')
current_y = (window_h / 2) + window_y
scroll_y_by = desired_y - current_y

bot.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

time.sleep(1)
WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).click()


# time.sleep(2)

bot.switch_to.window(bot.window_handles[0])

element2 = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I am not a robot')]")))

desired_y = (element2.size['height'] / 2) + element2.location['y']
window_h = bot.execute_script('return window.innerHeight')
window_y = bot.execute_script('return window.pageYOffset')
current_y = (window_h / 2) + window_y
scroll_y_by2 = desired_y - current_y

# print(scroll_y_by2)

bot.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by2-12)

time.sleep(3)

bot.save_screenshot('1.png')

# bot.find_element(By.XPATH, '//a').click()
# bot.execute_script("document.body.style.zoom='75%'")
time.sleep(1)

bot.save_screenshot('11.png')

WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I am not a robot')]"))).click()

bot.switch_to.window(bot.window_handles[0])
time.sleep(2)
actions = ActionChains(bot)
actions.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
actions.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
actions.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
actions.send_keys(Keys.ARROW_DOWN)

# bot.execute_script("document.body.style.zoom='75%'")
bot.save_screenshot('2.png')


# Captcha ###################################################

try:
    time.sleep(2)
    frames = bot.find_elements(By.TAG_NAME, "iframe")

    recaptcha_control_frame = None
    recaptcha_challenge_frame = None
    for index, frame in enumerate(frames):
        if re.search('reCAPTCHA', frame.get_attribute("title")):
            recaptcha_control_frame = frame
            
        if re.search('recaptcha challenge', frame.get_attribute("title")):
            recaptcha_challenge_frame = frame
    # if not (recaptcha_control_frame and recaptcha_challenge_frame):
    #     print("[ERR] Unable to find recaptcha. Abort solver.")
    #     sys.exit()
    # # switch to recaptcha frame
    # time.sleep(5)
    # frames = bot.find_elements_by_tag_name("iframe")
    # bot.switch_to.frame(recaptcha_control_frame)
    # # click on checkbox to activate recaptcha
    # bot.find_element_by_class_name("recaptcha-checkbox-border").click()

    # # switch to recaptcha audio control frame
    # time.sleep(5)
    # bot.switch_to.default_content()
    frames = bot.find_elements(By.TAG_NAME, "iframe")
    bot.switch_to.frame(recaptcha_challenge_frame)

    # click on audio challenge
    time.sleep(4)
    bot.find_element(By.ID, "recaptcha-audio-button").click()

    # switch to recaptcha audio challenge frame
    bot.switch_to.default_content()
    frames = bot.find_elements(By.TAG_NAME, "iframe")
    # for index, frame in enumerate(frames):
    #     if re.search('reCAPTCHA', frame.get_attribute("title")):
    #         recaptcha_control_frame = frame
            
    #     if re.search('recaptcha challenge', frame.get_attribute("title")):
    #         recaptcha_challenge_frame = frame
    bot.switch_to.frame(recaptcha_challenge_frame)

    # get the mp3 audio file
    time.sleep(5)
    src = bot.find_element(By.ID, "audio-source").get_attribute("src")
    print(f"[INFO] Audio src: {src}")

    path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
    path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))

    # download the mp3 audio file from the source
    urllib.request.urlretrieve(src, path_to_mp3)
    urllib.request.urlretrieve(src, path_to_wav)
except Exception as e:
    print(e)
    # if ip is blocked.. renew tor ip
    print("[INFO] IP address has been blocked for recaptcha.")
    # if activate_tor:
    #     renew_ip(CONTROL_PORT)
    #sys.exit()   
    pass 

# load downloaded mp3 audio file as .wav
print('load downloaded mp3 audio file as .wav')
try:
    sound = pydub.AudioSegment.from_mp3(path_to_mp3)
    sound.export(path_to_wav, format="wav")
    path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
    sample_audio = sr.AudioFile(path_to_wav)
except Exception as e:
    print('11111')
    print(e)
    pass
    # sys.exit(
    #     "[ERR] Please run program as administrator or download ffmpeg manually, "
    #     "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
    # )

# translate audio to text with google voice recognition
print('translate audio to text with google voice recognition')
try:
    time.sleep(5)
    r = sr.Recognizer()
    print('111')
    with sample_audio as source:
        print('1111222222')
        audio = r.record(source)
        print('222')
    key = r.recognize_google(audio,language='en-IN')
    print(f"[INFO] Recaptcha Passcode: {key}")

    # key in results and submit
    time.sleep(5)
    bot.find_element(By.ID, "audio-response").send_keys(key.lower())
    bot.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
except Exception as e:
    print(e)
    pass

######################################################

# time.sleep(100)
bot.execute_script("document.body.style.zoom='25%'")
time.sleep(2)
element3 = WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Go ->')]")))

desired_y = (element3.size['height'] / 2) + element3.location['y']
window_h = bot.execute_script('return window.innerHeight')
window_y = bot.execute_script('return window.pageYOffset')
current_y = (window_h / 2) + window_y
scroll_y_by3 = desired_y - current_y

bot.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by3)

time.sleep(3)

# bot.execute_script("document.body.style.zoom='35%'")

# time.sleep(50)

WebDriverWait(bot,100).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Go ->')]"))).click()

time.sleep(2)

get_url = bot.current_url

print("The current url is:"+str(get_url))

print('Done!!!!!!!!!')

time.sleep(2)

bot.quit()
# bot.execute_script("arguments[0].scrollIntoView();", element1)

# WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))).click()
# time.sleep(5)

# element2 = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I am not a robot')]")))
# time.sleep(5)

# bot.execute_script("arguments[0].scrollIntoView();", element2)

# WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I am not a robot')]"))).click()

        
        
# time.sleep(10000)        
        


