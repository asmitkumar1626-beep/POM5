from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    options=Options()
    options.add_argument("--guest")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    driver.maximize_window()
    return driver