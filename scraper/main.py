from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from spider import vn_applycv_com
from spider import vietnocv_io
import schedule
import time

options = Options()
options.headless = True
browser = webdriver.Firefox(options = options,executable_path = GeckoDriverManager().install())

schedule.every().day.at("15:00").do(vn_applycv_com.run(browser))
schedule.every().day.at("16:00").do(vietnocv_io.run(browser))

while True:
    schedule.run_pending()
    time.sleep(1)