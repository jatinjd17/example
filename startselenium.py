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
driver.get('https://youtube.com')
print(driver.title)
