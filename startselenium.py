from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# The place we will direct our WebDriver to
url = 'http://www.srcmake.com/'

# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome(chrome_options=options)

# Directing the driver to the defined url
driver.get('https://www.ipaddress.my/')
# ippp = driver.find_element_by_css_selector("span#ipv4 > a::text")
# print("HTML code of element: " + ippp.get_attribute('innerHTML'))
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/table/tbody/tr/td/div/div/ul")
source_code = elem.get_attribute("outerHTML")
print(source_code)
