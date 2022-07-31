from selenium import webdriver
from time import sleep



from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--window-size=1920,1080')
options.add_argument("--headless")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# options.add_argument("--start-fullscreen")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# The place we will direct our WebDriver to


# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome(chrome_options=options)

# Directing the driver to the defined url
# driver.get('https://www.sps-software.net/')
driver.get('https://www.shareasale.com/r.cfm?b=421982&u=3161018&m=43951')

sleep(10)



######################################################STSRT##########################################
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[1]/input").send_keys("edwardjohnson19539i@gmail.com")
#####################################################
sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/form/div[2]/div[2]/a") \
    .click()


sleep(4)

elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/h1")

source_code = elem.get_attribute("outerHTML")
print(source_code)
sleep(3)
###########################################################END##########################################################################


driver.quit()
