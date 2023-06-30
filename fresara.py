from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import names
import undetected_chromedriver as uc

cities = ["Aberdeen","Abilene","Akron","Albany","Albuquerque","Alexandria","Allentown","New York",
    "Buffalo",
    "Rochester",
    "Yonkers",
    "Syracuse",
    "Albany",
    "New Rochelle",
    "Mount Vernon",
    "Schenectady",
    "Utica",
    "White Plains",
    "Hempstead",
    "Troy",
    "Niagara Falls",
    "Binghamton",
    "Freeport",
    "Valley Stream",
    "Los Angeles",
    "San Diego",
    "San Jose",
    "San Francisco",
    "Fresno",
    "Sacramento",
    "Long Beach",
    "Oakland",
    "Bakersfield",
    "Anaheim",
    "Santa Ana",
    "Riverside",
    "Stockton",
    "Chula Vista",
    "Irvine",
    "Fremont",
    "San Bernardino",
    "Modesto",
    "Fontana",
    "Oxnard",
    "Moreno Valley",
    "Huntington Beach",
    "Glendale",
    "Santa Clarita",
    "Garden Grove",
    "Oceanside",
    "Rancho Cucamonga",
    "Santa Rosa",
    "Ontario",
    "Lancaster",
    "Elk Grove",
    "Corona",
    "Palmdale",
    "Salinas",
    "Pomona",
    "Hayward",
    "Escondido",
    "Torrance",
    "Sunnyvale",
    "Orange",
    "Fullerton",
    "Pasadena",
    "Thousand Oaks",
    "Visalia",
    "Simi Valley",
    "Concord",
    "Roseville",
    "Victorville",
    "Santa Clara",
    "Vallejo",
    "Berkeley",
    "El Monte",
    "Downey",
    "Costa Mesa",
    "Inglewood",
    "Carlsbad",
    "San Buenaventura (Ventura)",
    "Fairfield",
    "West Covina",
    "Murrieta",
    "Richmond",
    "Norwalk",
    "Antioch",
    "Temecula",
    "Burbank",
    "Daly City",
    "Rialto",
    "Santa Maria",
    "El Cajon",
    "San Mateo",
    "Clovis",
    "Compton",
    "Jurupa Valley",
    "Vista",
    "South Gate",
    "Mission Viejo",
    "Vacaville",
    "Carson",
    "Hesperia",
    "Santa Monica",
    "Westminster",
    "Redding",
    "Santa Barbara",
    "Chico",
    "Newport Beach",
    "San Leandro",
    "San Marcos",
    "Whittier",
    "Hawthorne",
    "Citrus Heights",
    "Tracy",
    "Alhambra",
    "Livermore",
    "Buena Park",
    "Menifee",
    "Hemet",
    "Lakewood",
    "Merced",
    "Chino",
    "Indio",
    "Redwood City",
    "Lake Forest",
    "Napa",
    "Tustin",
    "Bellflower",
    "Mountain View",
    "Chino Hills",
    "Baldwin Park",
    "Alameda",
    "Upland",
    "San Ramon",
    "Folsom",
    "Pleasanton",
    "Union City",
    "Perris",
    "Manteca",
    "Lynwood",
    "Apple Valley",
    "Redlands",
    "Turlock",
    "Milpitas",
    "Redondo Beach",
    "Rancho Cordova",
    "Yorba Linda",
    "Palo Alto",
    "Davis",
    "Camarillo",
    "Walnut Creek",
    "Pittsburg",
    "South San Francisco",
    "Yuba City",
    "San Clemente",
    "Laguna Niguel",
    "Pico Rivera",
    "Montebello",
    "Lodi",
    "Madera",
    "Santa Cruz",
    "La Habra",
    "Encinitas",
    "Monterey Park",
    "Tulare",
    "Cupertino",
    "Gardena",
    "National City",
    "Rocklin",
    "Petaluma",
    "Huntington Park",
    "San Rafael",
    "La Mesa",
    "Arcadia",
    "Fountain Valley",
    "Diamond Bar",
    "Woodland",
    "Santee",
    "Lake Elsinore",
    "Porterville",
    "Paramount",
    "Eastvale",
    "Rosemead",
    "Hanford",
    "Highland",
    "Brentwood",
    "Novato",
    "Colton",
    "Cathedral City",
    "Delano",
    "Yucaipa",
    "Watsonville",
    "Placentia",
    "Glendora",
    "Gilroy",
    "Palm Desert",
    "Cerritos",
    "West Sacramento",
    "Aliso Viejo",
    "Poway",
    "La Mirada",
    "Rancho Santa Margarita",
    "Cypress",
    "Dublin",
    "Covina",
    "Azusa",
    "Palm Springs",
    "San Luis Obispo",
    "Ceres",
    "San Jacinto",
    "Lincoln",
    "Newark",
    "Lompoc",
    "El Centro",
    "Danville",
    "Bell Gardens",
    "Coachella",
    "Rancho Palos Verdes",
    "San Bruno",
    "Rohnert Park",
    "Brea",
    "La Puente",
    "Campbell",
    "San Gabriel",
    "Beaumont",
    "Morgan Hill",
    "Culver City",
    "Calexico",
    "Stanton",
    "La Quinta",
    "Pacifica",
    "Montclair",
    "Oakley",
    "Monrovia",
    "Los Banos",
    "Martinez"
    ]


class InstAut:
    def __init__(self):
        options = webdriver.ChromeOptions() 
        # options = webdriver.FirefoxOptions() 

        # options.headless = True
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-popup-blocking')
        # firstname = (names.get_first_name(gender='male')).lower()
        # lastname = (names.get_last_name()).lower()
        # email = firstname+'_'+lastname+str(random.randrange(400,2000))+'@outlook.com'
        # print(email)
        bot = uc.Chrome(options=options)

        # bot.get('https://www.thehairstyler.com/signup')

        # time.sleep(8)

        

        # bot.execute_script("document.body.style.zoom='-80%'")

        bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

        bot.get("https://email-fake.com/")

        time.sleep(3)

        emaill = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#email_ch_text')))

        email = emaill.text

        print(email)


        bot.execute_script("window.open('https://www.google.com');")

        bot.switch_to.window(bot.window_handles[1])

        time.sleep(2)






        # PROXY = "103.10.235.231:80"
        # webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
        #     "httpProxy": PROXY,
        #     "ftpProxy": PROXY,
        #     "sslProxy": PROXY,
        #     "proxyType": "MANUAL",
        #
        # }


        # bot = webdriver.Chrome("C:\Selenium\Chrome WebDriver\chromedriver.exe", options=chrome_options)
        #
        #

        # bot = webdriver.Firefox()

        # bot = webdriver.Chrome()
        #
        #
        # bot.get("https://www.google.com/")
        # sleep(40)

        bot.get("https://www.shareasale.com/r.cfm?b=5304&u=3668960&m=1837")
        time.sleep(2)

        ###################################################################

        #
        # WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")\
        #     .send_keys(emai)
        # sleep(1)
        #
        # name = names.get_full_name(gender='male')
        # print(name)
        #
        #
        # WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/div/label/input")\
        #     .send_keys(name)
        # sleep(1)
        #
        # # 190347
        #
        #
        # WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[5]/div/label/input")\
        #     .send_keys(name.split(' ', 1)[0] + str(random.randint(0, 10000000000)))
        # sleep(1)
        #
        #
        # WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[6]/div/label/input")\
        #     .send_keys("Password@123")
        # sleep(4)
        #
        #
        # WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[7]/div/button")\
        #     .click()
        #
        #
        #
        # sleep(12)

############################################################################################################


        


        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/button[1]")))\
            .click()
        time.sleep(2)


        element2 = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[4]/div/div/div[2]/select")))
        desired_y = (element2.size['height'] / 2) + element2.location['y']
        window_h = bot.execute_script('return window.innerHeight')
        window_y = bot.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by2 = desired_y - current_y

        # print(scroll_y_by2)

        bot.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by2)


        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[1]/div/select")))\
            .click()
        time.sleep(0.4)

        # actions = ActionChains(bot)
        # actions.send_keys(Keys.DOWN)
        # time.sleep(0.5)
        # actions.send_keys(Keys.DOWN)
        # time.sleep(0.5)
        # actions.send_keys(Keys.DOWN)
        # time.sleep(0.5)
        # actions.send_keys(Keys.DOWN)

        # bot.execute_script("document.body.style.zoom='25%'")

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[1]/div/select/option[2]")))\
            .click()
        time.sleep(0.4)

        name = names.get_first_name(gender='male')
        print(name)


        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[2]/div/input")))\
            .send_keys(name)
        time.sleep(0.4)

        lastname = names.get_last_name()

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[3]/div/input")))\
            .send_keys(lastname)
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[4]/div/div/div[1]/select")))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[4]/div/div/div[1]/select/option[222]")))\
            .click()
        time.sleep(0.4)



        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[4]/div/div/div[2]/select")))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[4]/div/div/div[2]/select/option[{}]".format(random.randint(4,50)))))\
            .click()
        time.sleep(0.4)


        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[5]/div/input"))) \
            .send_keys(email)
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[6]/div/div/div[1]/select"))) \
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[6]/div/div/div[1]/select/option[{}]".format(random.randint(2, 9)))))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[6]/div/div/div[2]/select")))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[6]/div/div/div[2]/select/option[{}]".format(random.randint(2,28)))))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[6]/div/div/div[3]/select")))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[6]/div/div/div[3]/select/option[28]".format(random.randint(15,35)))))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[7]/div/div/div[1]/div/div/select")))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[7]/div/div/div[1]/div/div/select/option[17]".format(random.randint(4,23)))))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[7]/div/div/div[2]/div/div/select")))\
            .click()
        time.sleep(0.4)


        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[7]/div/div/div[2]/div/div/select/option[39]".format(random.randint(4,57)))))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[2]/div/div[2]/div[1]/label/input")))\
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[8]/div/input"))) \
            .send_keys("{}".format(cities[random.randint(2, 180)]))
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[1]/div/div[9]/div/input"))) \
            .send_keys("USA")
        time.sleep(0.4)

        element2 = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/div[2]/ul/li[5]/input")))

        desired_y = (element2.size['height'] / 2) + element2.location['y']
        window_h = bot.execute_script('return window.innerHeight')
        window_y = bot.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by2 = desired_y - current_y

        # print(scroll_y_by2)

        bot.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by2)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/div[2]/ul/li[5]/input"))) \
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[5]/div/div[1]/label/input"))) \
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[1]/div[5]/div/div[2]/label/input"))) \
            .click()
        time.sleep(0.4)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/form/div[2]/div[1]/button")))\
            .click()
        time.sleep(5)






        bot.switch_to.window(bot.window_handles[0])

        time.sleep(2)



        bot.get("https://email-fake.com/")

        time.sleep(3)

        bot.get("https://email-fake.com/")


        time.sleep(5)
        # elem = self.driver1.find_element(By.XPATH, "/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]")
        # time.sleep(4)
        # pro = elem.get_attribute('innerHTML')
        # time.sleep(3)
        # print(pro)
        # time.sleep(7)

        element2 = WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[2]/div[4]/div[3]/table/tbody/tr/td/center/table[2]/tbody/tr[2]/td/a/strong")))

        desired_y = (element2.size['height'] / 2) + element2.location['y']
        window_h = bot.execute_script('return window.innerHeight')
        window_y = bot.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by2 = desired_y - current_y

        # print(scroll_y_by2)

        bot.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by2)

        WebDriverWait(bot,20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[2]/div[4]/div[3]/table/tbody/tr/td/center/table[2]/tbody/tr[2]/td/a/strong"))) \
            .click()
        

        time.sleep(5)
        bot.switch_to.window(bot.window_handles[2])
        time.sleep(1)
        get_url = bot.current_url

        print("The current url is:"+str(get_url))

        time.sleep(10)


        bot.close()



InstAut()
