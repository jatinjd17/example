# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time, os
# from pykeyboard import PyKeyboard
# import keyboard
import random
from selenium.webdriver.common.by import By
# from itertools import islice
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from requests import get, post
import json
import time

# Set up Firefox options for headless mode
firefox_options = Options()
# firefox_options.headless = True
firefox_options.add_argument("--headless")
firefox_options.add_argument("--window-size=1920x1080")


# Create a WebDriver instance with the specified options
bot = webdriver.Firefox(options=firefox_options)

random_number = random.randint(100, 1000000)
shopname = 'Shopy'+str(random_number)

bot.get("https://email-fake.com/")

time.sleep(3)

emaill = bot.find_element(By.CSS_SELECTOR, '#email_ch_text')

email = emaill.text

print(email)

bot.execute_script("window.open('https://www.google.com');")
time.sleep(3)

bot.switch_to.window(bot.window_handles[1])

# Example: Open a website
bot.get('https://www.shoplazza.com/pages/shareasale?utm_source=shareasale&utm_medium=affiliate&utm_campaign=shareasale_affiliate&utm_term=2176125&')
time.sleep(5)
bot.save_screenshot("screenshot.png")

# WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[2]/input'))).send_keys(email)
bot.save_screenshot('1.png')
time.sleep(2)

actions = ActionChains(bot)
# modal_dialog = bot.switch_to.active_element
for _ in range(12):
    actions.send_keys('\ue004')  # '\ue004' is the Unicode representation of the Tab key

# Press the Enter key
actions.send_keys(' ')   # '\ue007' is the Unicode representation of the Enter key

# Perform the actions
actions.perform()
# actions = ActionChains(bot)
#
# # Press the Tab key
# actions.send_keys('\ue004')  # '\ue004' is the Unicode representation of the Tab key
#
# # Press the Space key
# # actions.send_keys('\ue007')  # Space key
#
# # Perform the actions
# actions.perform()
# time.sleep(2)
# actions2 = ActionChains(bot)
#
# # Press the Tab key
# # actions2.send_keys('\ue004')  # '\ue004' is the Unicode representation of the Tab key
#
# # Press the Space key
# actions2.send_keys('\ue007')  # Space key
#
# # Perform the actions
# actions2.perform()
# WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Continue without accepting')]"))).click()
# keyboard.send('tab')
# keyboard.send('tab')
# keyboard.send('tab')
# keyboard.send('tab')
# keyboard.send('tab')

time.sleep(2)
bot.save_screenshot('12.png')
WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[2]/input'))).send_keys(email)
# keyboard.send('enter')
# bot.find_element(By.XPATH, '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[2]/input').send_keys('xxxxspb@domaain23.online')
# time.sleep(5)

# '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/div[3]/div[1]/input'


# WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/div[3]/div[1]/input'))).click()

time.sleep(5)

bot.switch_to.window(bot.window_handles[0])

time.sleep(10)

bot.get("https://email-fake.com/")


# 'div.fem.mess_bodiyy > div '

time.sleep(5)
bot.save_screenshot('01.png')

bot.get("https://email-fake.com/")

time.sleep(5)
bot.save_screenshot('02.png')
# bot.execute_script("document.body.style.zoom='45%'")

# html = bot.find_element_by_tag_name('html')
html = bot.find_element(By.XPATH, '/html')
html.send_keys(Keys.END)
bot.save_screenshot('03.png')
# time.sleep(10)
element = WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mess_bodiyy > div:nth-child(1) > p:nth-child(3)')))

inner_text = element.text

print("Inner Text:", inner_text)

bot.switch_to.window(bot.window_handles[1])
time.sleep(2)
bot.save_screenshot('2.png')
WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/div[3]/div[1]/input'))).send_keys(inner_text)
# time.sleep(3)
# '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[3]/div[1]/input'
WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/div[4]/input'))).send_keys('Jatin@123')
# time.sleep(1)
# '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[4]/input'
WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/div[5]/div/input'))).send_keys(shopname)
# time.sleep(1)
# '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[5]/div/input'
WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/div[6]/div/span[2]'))).click()
time.sleep(2)
# '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/div[6]/div/span[2]'
WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/button'))).click()
                                                                    # '/html/body/div[2]/div[4]/div/div/div/div/div/div/div[2]/div/form[1]/button'


# '//*[@id="affiliate-register-container"]/div/div/div[2]/div/form[1]/button'

time.sleep(10)
print('1111111')
WebDriverWait(bot,1000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/div/a'))).click()
time.sleep(5)
try:
    WebDriverWait(bot,10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/div/a'))).click()
except:
    pass
# bot.find_element(By.XPATH, '//*[@id="dj-smart-app"]/div[2]/div/div[3]/div/a').click()
# time.sleep(10)
print('111222')
time.sleep(10)

WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/div[2]/main/aside/div[2]/div[1]/div[3]/div/span[2]'))).click()

# bot.get(f'https://{shopname}.myshoplaza.com/admin/smart_apps/python/products')
# '//*[@id="dj-smart-app"]/div[2]/header/div[2]/button[3]'
# bot.find_element(By.XPATH, '//*[@id="rc-tabs-0-panel-14"]/div/div[1]/div/div[3]/button').click()
# WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-0-panel-13"]/div/div[1]/div/div[3]/button'))).click()
# time.sleep(10)
# WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div/div/div/div/a/span/span'))).click()
# time.sleep(10)

###import
##########################################
#     WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dj-smart-app"]/div[2]/header/div[2]/button[3]'))).click()
#     # time.sleep(5)

#
#     file_input = WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/span/div')))
#
# # Provide the path to the file you want to upload
#     file_path = r"C:\Users\jatin\OneDrive\Desktop\example\product.xlsx"
#
#     # Use send_keys to set the file path in the file input
#     file_input.send_keys(file_path)
#
#     # time.sleep(5)
#
#     WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div[2]/div/div[2]/div[3]/div/button[2]'))).click()
#
#     # time.sleep(8)
#
#     WebDriverWait(bot,100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[16]/div/div[2]/div/div[2]/div[3]/div/button'))).click()

########################################################

WebDriverWait(bot,1000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/div[2]/main/section/div[2]/div/div[2]/div[1]/div/div[2]/button'))).click()
print('222222')

###Create product
# WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dj-smart-app"]/div[2]/header/div[2]/button[5]'))).click()
time.sleep(5)
WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product.title"]'))).send_keys('Cloth')
time.sleep(3)
WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product.title"]'))).send_keys('Cloth')
print('33333')

time.sleep(2)
try:
    WebDriverWait(bot,40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/div[2]/header/header/div[2]/div[2]/button[2]'))).click()
except:
    pass
print('44444')

time.sleep(5)
# WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productimagescard"]/div[2]/div/div/div/span/div/div[1]/div'))).click()
# time.sleep(15)
modal_trigger_element = bot.find_element(By.XPATH, '/html/body/div[5]/section/div[2]/main/section/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div/span/div/div[1]/div')
modal_trigger_element.click()
print('555555')

# Switch to the active modal dialog
modal_dialog = bot.switch_to.active_element
WebDriverWait(bot,40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/div[1]/button[3]'))).click()
WebDriverWait(bot,40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[3]/div/div[2]/div[1]/div[1]'))).click()
WebDriverWait(bot,40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[12]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]'))).click()
WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product.variants[0].price"]'))).send_keys('10')
WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product.variants[0].compare_at_price"]'))).send_keys('12')
WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product.variants[0].cost_price"]'))).send_keys('8')
WebDriverWait(bot,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product.variants[0].weight"]'))).send_keys('0.6')
WebDriverWait(bot,40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/div[2]/header/header/div[2]/div[2]/button[2]'))).click()
print('6666666')

time.sleep(4)
bot.save_screenshot('4.png')
print('Done')



time.sleep(200)

time.sleep(10)
# Perform other automation tasks as needed

# Close the browser
driver.quit()
