from ast import Not
from selenium import webdriver
from bs4 import BeautifulSoup
import time

path=r"C:\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
link = 'https://www.vietnamworks.com'


def run():
    URL = link + '/tim-viec-lam/tat-ca-viec-lam'
    browser.get(URL)
    action = webdriver.ActionChains(browser)
    
    for i in range(100):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

        
    