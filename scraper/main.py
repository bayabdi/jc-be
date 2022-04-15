from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from spider import vn_applycv_com
from spider import vietnocv_io
import time


while (True):
    try:
        print("begin")
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(options = options,executable_path = GeckoDriverManager().install())

        try:
            vn_applycv_com.run(browser)
        finally:
            vietnocv_io.run(browser)
        print("end")
        print()
        
        time.sleep(24 * 60 * 60)
    finally:
        browser.quit()
