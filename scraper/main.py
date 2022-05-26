from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from spider import vn_applycv_com
from spider import vietnocv_io
import schedule
import time

options = Options()
options.headless = True
browser = webdriver.Firefox(options = options,
    executable_path = GeckoDriverManager().install())

while True:
    try:
         vn_applycv_com.run(browser)
    finally:
        try:
            vietnocv_io.run(browser)
        finally:
            time.sleep(24 * 60 * 60)