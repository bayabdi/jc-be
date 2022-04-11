from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from spider import vn_applycv_com



options = Options()
options.headless = True
browser = webdriver.Firefox(options = options,executable_path = GeckoDriverManager().install())

vn_applycv_com.run(browser)

browser.quit()
