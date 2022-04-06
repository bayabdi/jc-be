from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import os
directory = os.getcwd()

options = Options()
options.headless = True
browser = webdriver.Firefox(
    options=options,
    executable_path = directory + 'geckodriver.exe'
)

link = 'https://www.vietnamworks.com'

def getJobList():
    print('Ok')

def run():
    URL = link + '/tim-viec-lam/tat-ca-viec-lam'
    