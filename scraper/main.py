from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from spider import vn_applycv_com
from spider import vietnocv_io
import time


while (True):
    print("begin")
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options = options,executable_path = GeckoDriverManager().install())

    vn_applycv_com.run(browser)
    vietnocv_io.run(browser)
    browser.quit()
    print("end")
    print()
    
    time.sleep(24 * 60 * 60)
