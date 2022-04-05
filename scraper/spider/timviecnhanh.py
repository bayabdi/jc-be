from msilib.schema import tables
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import db
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True
browser = webdriver.Firefox(
    options=options,
    executable_path=GeckoDriverManager().install()
)

link = 'https://timviecnhanh.com'

def getJobInfo(jobLink, f):
    print('Link   --->  ' + jobLink)
    
    browser.get(jobLink)
    
    soup = BeautifulSoup(browser.page_source, features="html.parser")

    title = ''
    
    if len(soup.select('span.title')) > 0:
        title = soup.select('span.title')[0].get_text(strip=True)
        
    #print('Title ---> ' + title)
    
    description = ''
    requirement = ''
    
    table = soup.select('tbody')
    
    if len(table) > 0:
        cell = table[0].select('td')
        if len(cell) > 1:
            description = cell[1].get_text(strip=True)
        if len(cell) > 3:
            requirement = cell[3].get_text(strip=True)

    #print('Description -->  ', description)
    #print('Requirement -->  ', requirement)
    
    company_name = ''
    if len(soup.select('div.title-employer')) > 0:
        company_name = soup.select('div.title-employer')[0].get_text(strip=True)
    #print('Company name -->  ' + company_name)
    
    company_description = ''
    
    location = ''
    if len(soup.select('div.company-job-address')) > 0:
        location = soup.select('div.company-job-address')[0].get_text(strip=True)
    #print('Location --> ' + location)
    
    company_size = ''
    
    company_logo = ''
    if len(soup.select('img.lazyloaded')) > 0:
        company_logo = soup.select('img.lazyloaded')[0]['src']
    #print('Company Logo -->  ' + company_logo)
    
    salary = ''
    if len(soup.select('article')) > 0 and len(soup.select('article')[0].select('li')) and len(soup.select('article')[0].select('li')[0]):
        salary = soup.select('article')[0].select('li')[0].get_text(strip=True).split(':')[1]
    #print('Salary --> ' + salary)
    
    post_date = ''
    if len(soup.select('article')) > 0 and len(soup.select('article')[0].select('div')) > 0:
        post_date = soup.select('article')[0].select('div')[0].get_text(strip=True)
        post_date = post_date.split('|')[0].split(': ')[1]
    #print('Post date --> ' + post_date)
    
    language = ''
    
    db.insert(
        title,
        jobLink,
        description,
        '',
        requirement,
        company_name,
        company_description,
        location,
        company_size,
        company_logo,
        salary,
        post_date,
        language
    )
    
def getJobList(pageN):
    URL = link + '/vieclam/timkiem?action=search&page=' + str(pageN)
    browser.get(URL)
    soup = BeautifulSoup(browser.page_source, features="html.parser")

    table = soup.find('tbody')
    job_elements = table.find_all('a', class_="title-job", href=True)
    
    with open('timvievnhanh.txt', 'w', encoding='utf-8') as f:
        for job_element in job_elements:
            jobLink = link + job_element['href']
            getJobInfo(jobLink, f)
            time.sleep(2)
    
def run():
    for page in range(1, 21):
        getJobList(page)
        time.sleep(3)
    
    browser.quit()