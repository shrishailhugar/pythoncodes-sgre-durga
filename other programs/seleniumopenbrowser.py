from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep,time


s_obj=Service('C:\\ChromeDriver\\chromedriver.exe')
options=ChromeOptions()
path='C:\\ChromeDriver'
prefs={
    'download.default_directory':path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
}
options.add_experimental_option('prefs',prefs)
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--start-maximized')
driver=Chrome(service=s_obj,options=options)
driver.get('https:\\youtube.com')
sleep(8)