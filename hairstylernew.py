import time, os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import names
from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import urllib
import pydub
import speech_recognition as sr
import re
import sys


print("INIT")
options = Options()

# options = webdriver.ChromeOptions()
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

    # bot.get('https://www.thehairstyler.com/signup')

    # time.sleep(8)

    

    # bot.execute_script("document.body.style.zoom='-80%'")

    bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

    bot.get("https://email-fake.com/")

    time.sleep(3)

    emaill = bot.find_element(By.CSS_SELECTOR, '#email_ch_text')

    email = emaill.text

    print(email)


    bot.execute_script("window.open('https://www.google.com');")

    bot.switch_to.window(bot.window_handles[1])

    time.sleep(2)



    bot.get('https://www.shareasale.com/r.cfm?b=15440&u=3669348&m=4421')

    time.sleep(3)

    bot.get('https://www.thehairstyler.com/signup')

    time.sleep(8)

    try:

        bot.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[1]').click()
    except:
        pass

    fname = names.get_first_name(gender='male')


    bot.find_element(By.XPATH, '//*[@id="user_first_name"]').send_keys(fname)

    lastname = names.get_last_name()

    time.sleep(1)

    bot.find_element(By.XPATH, '//*[@id="user_last_name"]').send_keys(lastname)

    time.sleep(1)

    bot.find_element(By.XPATH, '//*[@id="user_email"]').send_keys(email)

    time.sleep(1)

    bot.find_element(By.XPATH, '//*[@id="user_password"]').send_keys("Jatin@123")

    time.sleep(1)

    bot.find_element(By.XPATH, '//*[@id="user_password_confirmation"]').send_keys("Jatin@123")

    # '//*[@id="last_name"]'

    # '//*[@id="email"]'

    # WebDriverWait(bot, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title^='reCAPTCHA']")))

    # # WebDriverWait(bot, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='google_esf'][src^='https://googleads.g.doubleclick.net/pagead/html/r20230308/r20190131/zrt_lookup.html']")))
    # WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

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
        if not (recaptcha_control_frame and recaptcha_challenge_frame):
            print("[ERR] Unable to find recaptcha. Abort solver.")
            sys.exit()
        # switch to recaptcha frame
        time.sleep(5)
        frames = bot.find_elements(By.TAG_NAME, "iframe")
        bot.switch_to.frame(recaptcha_control_frame)
        # click on checkbox to activate recaptcha
        bot.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

        # switch to recaptcha audio control frame
        time.sleep(5)
        bot.switch_to.default_content()
        frames = bot.find_elements(By.TAG_NAME, "iframe")
        bot.switch_to.frame(recaptcha_challenge_frame)

        # click on audio challenge
        time.sleep(4)
        bot.find_element(By.ID, "recaptcha-audio-button").click()

        # switch to recaptcha audio challenge frame
        bot.switch_to.default_content()
        frames = bot.find_elements(By.TAG_NAME, "iframe")
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
    try:
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = sr.AudioFile(path_to_wav)
    except Exception:
        pass
        # sys.exit(
        #     "[ERR] Please run program as administrator or download ffmpeg manually, "
        #     "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
        # )

    # translate audio to text with google voice recognition
    try:
        time.sleep(5)
        r = sr.Recognizer()
        with sample_audio as source:
            audio = r.record(source)
        key = r.recognize_google(audio,language='en-IN')
        print(f"[INFO] Recaptcha Passcode: {key}")

        # key in results and submit
        time.sleep(5)
        bot.find_element(By.ID, "audio-response").send_keys(key.lower())
        bot.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
    except:
        pass
    # time.sleep(5)
    # bot.switch_to.default_content()
    # time.sleep(5)
    # bot.find_element(By.ID, "recaptcha-demo-submit").click()
    # time.sleep(300)
    # if (tor_process):
    #     tor_process.kill()


    time.sleep(5)


    bot.switch_to.default_content()


    time.sleep(1)

    bot.find_element(By.XPATH, '//*[@id="submitBtn"]').click()

    time.sleep(5)

    aa = bot.find_element(By.CSS_SELECTOR, 'body > div.container > div:nth-child(4) > div > h1')

    print(aa.text)


    time.sleep(1)

    bot.switch_to.window(bot.window_handles[0])


    time.sleep(1)



    bot.get("https://email-fake.com/")


    time.sleep(5)

    # bot.execute_script("document.body.style.zoom='45%'")

    html = bot.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)

    time.sleep(10)

    bot.find_element(By.CSS_SELECTOR, 'div.fem.mess_bodiyy > p + p + p > a').click()
    time.sleep(5)
    bot.switch_to.window(bot.window_handles[1])
    get_url = bot.current_url

    print("The current url is:"+str(get_url))
    time.sleep(2)
    bot.switch_to.window(bot.window_handles[2])
    get_url = bot.current_url

    print("The current url is:"+str(get_url))



# 'Welcome to TheHairStyler.com. You can confirm your account email through the link below:'







    time.sleep(1)
    print('done')
    bot.quit()


if __name__ == "__main__":
    RunScript()
