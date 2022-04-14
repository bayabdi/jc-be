from bs4 import BeautifulSoup
import time
import db

def getJobInfo(job_link, browser):
    browser.get(job_link)
    soup = BeautifulSoup(browser.page_source, features="html.parser")
    
    print(job_link)
    
    title = ''
    if len(soup.select('h1.MuiTypography-h1')) > 0:
        title = soup.select('h1.MuiTypography-h1')[0].get_text(strip = True)
    
    print('Title >>>>>> ' + title)
     
    description = ''
    requirement = ''
    
    content = soup.get_text(strip = True)
    salary = ''
    if len(content.split('LƯƠNG')) > 1 and len(content.split('LƯƠNG')[1].split('date_range')) > 0:
        salary = content.split('LƯƠNG')[1].split('date_range')[0].strip()
    
    print('SALARY >>> ' + salary)
    
    deadline = ''
    if len(content.split('Hết hạn: ')) > 1:
        deadline = content.split('Hết hạn: ')[1][0:10]
    print('Deadline >>>', deadline)
    
    locaction = ''
    if len(content.split('ĐỊA ĐIỂM')) > 1 and len(content.split('ĐỊA ĐIỂM')[1].split('access_time')) > 0:
        locaction = content.split('ĐỊA ĐIỂM')[1].split('access_time')[0].strip()
    print('Location >>>', locaction)
    
    company_name = ''
    company_description = ''
    company_size = ''
    
    company_logo = ''
    if len(soup.find_all('img', alt='Logo')) > 0:
        company_logo = soup.find_all('img', alt='Logo')[0]['src']
    print('Company logo >>>', company_logo)
    
    """
    if len(soup.select('div.MuiPaper-rounded')) > 1:
        content = soup.select('div.MuiPaper-rounded')[1]
        if len(content.select('ol')) > 0:
            description = content.select('ol')[0].get_text(strip = True)
        elif len(content.select('div.public-DraftStyleDefault-ltr')) > 0:
            description = content.select('div.public-DraftStyleDefault-ltr')[0].get_text(strip = True)
        if len(content.select('ul')) > 0:
            requirement = content.select('ul')[0].get_text(strip = True)
        elif len(content.select('div.public-DraftStyleDefault-ltr')) > 1:
            description = content.select('div.public-DraftStyleDefault-ltr')[1].get_text(strip = True)

    print('Description >>>>> ' + description)
    print('Requirement >>>>> ' + requirement)

    salary = ''
    
    if len(content.select('div.MuiTypography-body2')) > 0:
        salary = content.select('div.MuiTypography-body2')[0].get_text(strip = True)
    
    print('SALARY >>>> ' + salary)
    
    company_name = ''
    company_description = ''
    company_size = ''
    company_logo = ''
    
    if len(soup.select('div.box-company')) > 0:
        company_box = soup.select('div.box-company')[0]

        if len(company_box.select('img')) > 0:
            company_logo = company_box.select('img')[0]['src']
        if len(company_box.select('h2.name')) > 0:
            company_name = company_box.select('h2.name')[0].get_text(strip = True)  
    
    salary = ''
    deadline = ''
    language = ''
    post_date = ''
    location = ''
    
    if len(soup.select('div.params')) > 0:
        for item in soup.select('div.params')[0].select('div.item'):
            if len(item.select('.param')) > 0:
                item = item.select('.param')[0]
            else:
                continue
            
            label = ''
            if len(item.select('span.param-label')) > 0:
                label = item.select('span.param-label')[0].get_text(strip = True)
            value = ''
            if len(item.select('.value')) > 0:
                value = item.select('.value')[0].get_text(strip = True)
            elif len(item.select('span')) > 1:
                value = item.select('span')[-1].get_text(strip = True)
            
            if label == 'Mức lương':
                salary = value
                
            if label == 'Địa điểm':
                location = value
            
            if label == 'Hạn nộp hồ sơ':
                deadline = value           
    
    db.insert(
        title,
        job_link,
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
        deadline,
        language
    )
    """
def getJobList(browser):
    link = 'https://vietcv.io'
    URL = link + '/jobs/discover'
    
    browser.get(URL)
    
    for page in range(0, 5):
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    soup = BeautifulSoup(browser.page_source, features="html.parser")
    
    job_elements = soup.select('li.MuiListItem-root')
    
    for job_element in job_elements:
        job_link = link + job_element.select('a.MuiTypography-root')[0]['href']
        getJobInfo(job_link, browser)
        time.sleep(1)
        #return
        
def run(browser):
    getJobList(browser)