from ast import Not
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True
browser = webdriver.Firefox(
    options=options,
    executable_path=GeckoDriverManager().install()
)

link = 'https://www.vietnamworks.com'

def getJobList():
    print('Ok')

def run():
    URL = link + '/tim-viec-lam/tat-ca-viec-lam'
    