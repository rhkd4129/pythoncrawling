import requests
from bs4 import BeautifulSoup
import pyautogui

# 스타트코딩님의 강의 내용
keyword = pyautogui.prompt("search")
lastepage = pyautogui.prompt("last page")

pageNum = 1
for i in range(1,int(lastepage)*10,10):
    print(f"{pageNum}페이지 내용======================================================================")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}")
    soup = BeautifulSoup(response.text,"html.parser")   
    links = soup.select(".news_tit")
    
    for link in links:
        title = link.text
        url = link.attrs['href']
        #url = link.select_one('herf')
        print(title)
    pageNum = pageNum+1

            #1...11...21...31


