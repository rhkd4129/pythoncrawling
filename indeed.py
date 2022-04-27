from pickle import NONE
from pkg_resources import ResolutionError
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL) 
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("div",{"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page



def extract_job(html):
    title = (html.find("div",{"class:":"title"}).title.find("a")["title"])
    company = html.find("span",{"class":"company"})
    company_anchor = company.find("a")
    if company_anchor is not None:
        company = str(company.find("a").string)
    else:
       company = str(company.string)
    company = company.strip()
    return {'title':title,'company':company}



def extract_indeed_jobs(last_page):
    jobs = []
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs
    