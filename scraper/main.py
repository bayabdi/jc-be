from spider import careerlink_jobs
#from spider import vietnamworks
from spider import timviecnhanh
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import os
directory = os.getcwd() + 'geckodriver'

options = Options()
options.headless = True
browser = webdriver.Firefox(
    options=options,
    executable_path = directory
)

careerlink_jobs.run(browser)
#vietnamworks.run()
timviecnhanh.run(browser)