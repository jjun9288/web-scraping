import requests
from bs4 import BeautifulSoup
URL = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
#print(URL.text)   #We got all the information about this website. But we are going to take out the page numbers from here.

indeed_soup = BeautifulSoup(URL.text,"html.parser")
#print(indeed_soup)

#Let's use soup.find()  (We can see what we can use in the documentation)
#<div class="pagination" onmousedown="pclk(event);"> == $0
pagination = indeed_soup.find("div",{"class":"pagination"})
#print(pagination)

#Its still complicated code, but we got closer. I can see numbers(1,2,3,...) between the codes and that might be the page numbers.

pages = pagination.find_all('a') 
#print(pages)
spans = []
#Lset get span inside the achors
for page in pages:
    spans.append(page.find("span"))
#print(spans)
#We succesfully extracted the pages now :)

#Also there was a function which only extracts the number of the pages and nothing else, which is .string
page_num = []
for page in pages[:-1]:
    page_num.append(page.string)
print(page_num)

max_page = pages[-1]

#In indeed.py, I made a function which can bring me the last page of the website with the codes up here.
from indeed import extract_indeed_jobs
from indeed import extract_indeed_url
max_indeed_page = extract_indeed_url()
print(max_indeed_page)
#Found out that the last page is 20

last_indeed_page = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_page)
print(indeed_jobs)