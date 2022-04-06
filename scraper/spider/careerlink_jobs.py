from selenium import webdriver
from bs4 import BeautifulSoup
import time
import db
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
browser = webdriver.Firefox(
    options=options,
    executable_path='geckodriver'
)

link = 'https://www.careerlink.vn'

def getJobInfo (jobLink, f):
    f.write('<---begin--->\n')
    
    f.write('Link -> ' + jobLink)
    
    browser.get(jobLink + str('\n'))
    soup = BeautifulSoup(browser.page_source, features="html.parser")
    
    title = ''
    if len(soup.select('h1.job-title')) > 0:
        title = soup.select('h1.job-title')[0].get_text(strip=True)
    f.write('\nTitle -> ' + title)
    
    description = ''
    requirement = ''
    
    if len(soup.select('div.card-body')) > 0:
        if len(soup.select('div.card-body')[0].select('div.raw-content')) > 0:
            description = soup.select('div.card-body')[0].select('div.raw-content')[0].get_text(strip=True)
        if len(soup.select('div.raw-content')) > 1:
            requirement = soup.select('div.card-body')[0].select('div.raw-content')[1].get_text(strip=True)
    
    f.write('\nDescription ->' + description)
    f.write('\nRequirement ->' + requirement)
    
    company_name = ''
    if len(soup.select('p.org-name')) > 0:
        company_name = soup.select('p.org-name')[0].get_text(strip=True)
    f.write('\nCompany name ->' + company_name)
    
    company_description = ''
    if len(soup.select('div.company-profile')) > 0:
        company_description = soup.select('div.company-profile')[0].get_text(strip=True)
    f.write('\nCompany Description ->' + company_description)
    
    location = ''
    if len(soup.select('li.address')) > 0:
        location = soup.select('li.address')[0].get_text(strip=True)
    f.write('\nLocation ->' + location)
    
    company_size = ''
    company_logo = ''
    
    if len(soup.select('div.company-card')) > 0:
        if len(soup.select('div.company-card')[0].select('li.align-items-start')) > 0:
            company_size = soup.select('div.company-card')[0].select('li.align-items-start')[0].get_text(strip=True)
        if len(soup.select('div.company-card')[0].select('img')) > 0:
            company_logo = soup.select('div.company-card')[0].select('img')[0]['src']
        
    f.write('\nCompany Size ->' + company_size)
    f.write('\nCompany logo ->' + company_logo)
    
    salary = ''
    if len(soup.select('p.salary')) > 0:
        salary = soup.select('p.salary')[0].get_text(strip=True)
    f.write('\nSalary ->' + salary)
    
    post_date = ''
    if len(soup.select('div.job-expire > div.d-flex.flex-wrap.mt-2 > div.mr-5')) > 0:
        post_date = soup.select('div.job-expire > div.d-flex.flex-wrap.mt-2 > div.mr-5')[0].get_text(strip=True)
    f.write('\npost_date ->' + post_date)
    
    language = ''
    if len(soup.select('div.job-expire > p.mb-0 > strong')) > 0:
        language = soup.select('div.job-expire > p.mb-0 > strong')[0].get_text(strip=True)
    f.write('\nlanguage ->' + language)
    
    f.write('\n<---end--->\n')
    
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
    
def getJobList (pageN):
    URL = link + '/vieclam/list?page=' + str(pageN)
    browser.get(URL)
    soup = BeautifulSoup(browser.page_source)

    job_elements = soup.find_all("a", class_="job-link", href=True)
    
    with open('careerlink.txt', 'w', encoding='utf-8') as f:
        for job_element in job_elements:
            jobLink = link + job_element['href'] 
            getJobInfo(jobLink, f)
            time.sleep(2)
            
def run():
    for page in range(1, 21):
        getJobList(page)
        time.sleep(3)
    
    browser.quit()