import requests
from requests.structures import CaseInsensitiveDict

def login():
    url = 'https://api.jobcado.com/user/login'
    data = {
        "email": "string",
        "password": "string"
    }
    
    response = requests.post(url, json = data)
        
    if (response.status_code == 201):
        data = response.json()

        return data['token']
    
    return ''
    
def insert(
    title,
    link,
    description,
    category,
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
):
    token = login()
    
    headers = CaseInsensitiveDict()
    headers['Authorization'] = "Bearer " + token
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"
    
    data = {
        "title": title,
        "description": description,
        "category": category,
        "requirement": requirement,
        "company_name": company_name,
        "company_description": company_description,
        "location": location,
        "company_size": company_size,
        "company_logo": company_logo,
        "salary": salary,
        "post_date": post_date,
        "language": language
    }