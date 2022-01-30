import requests
from bs4 import BeautifulSoup
import re

url="https://maple.inven.co.kr/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

titles = soup.find_all("li",attrs={"class":"b2299"})
for title  in titles:

    print(title.get_text()[2:-7],end="  link -->>")
    print(title.a['href'])
    