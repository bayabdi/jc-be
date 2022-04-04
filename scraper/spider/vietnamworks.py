from ast import Not
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.firefox.options import Options

options = Options()
#options.headless = True
browser = webdriver.Firefox(
    options=options,
    executable_path='D:\geckodriver\geckodriver.exe'
)

link = 'https://www.vietnamworks.com'

def getJobList():
    print('Ok')

def run():
    URL = link + '/tim-viec-lam/tat-ca-viec-lam'
    