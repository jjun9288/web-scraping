import requests
from bs4 import BeautifulSoup
URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_url():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("div",{"class":"pagination"})
    pages = pagination.find_all('a') 
    page_num = []
    for page in pages[:-1]:
        page_num.append(int(page.string))
    max_page = page_num[-1]
    return max_page

#Extracting name of job and company
def extract_job(html): 
    #in each "jobsearch blahblah class, theres another class with div"
    #and in each title class, theres an anchor. But theres still lots of information, but found out that title in anchor is the only
    #thing we need.
    title = html.find("h2",{"class":"title"}).find("a")["title"]
    company = html.find("span",{"class":"company"})
    company_anchor = company.find("a")
    #But I found out that some company had put on their link but some didn't.
    if company_anchor is not None:
        company = str(company_anchor.string)
    else:
        company = str(company.string)
    #Too many whitespaces between the name of companies so we are going to use strip in this case
    company = company.strip()
    return {'title':title, 'company':company}

def extract_indeed_jobs(last_page):
    jobs = []
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs