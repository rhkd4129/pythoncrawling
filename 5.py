import requests
from bs4 import BeautifulSoup
import pyautogui


keyword = pyautogui.prompt("search")
#keyword = input("search")
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html,'html.parser')


links = soup.select(".news_tit")


for link in links:
    title = link.text
    #url = link.attrs['href']
    url = link.select_one('herf')
    print(title,url)



#for link in links.find_all('a'):
#    print(link.get('href'))

#url
#https://
#search.naver.com/
#search.naver?    path부분
#where=news&squery=삼성전자
#key   value    파라미터
# 각 파라미터는 key와 value   =로 구분  쿼리는 검색어
