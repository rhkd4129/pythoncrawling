import requests
import re
from bs4 import BeautifulSoup

#나도코딩님의 강의 내용
#value = key
url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="

headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url,headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

#ad-badge-icon
items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
print(items[0].find("div",attrs ={"class":"name"}).get_text())
for item in items:
    #광고제품 제외
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("  ㄱ광고 상품 제외")
        continue#ㅈㄴ어려웡
    name = item.find("div",attrs ={"class":"name"}).get_text()
    price = item.find("strong",attrs = {"class":"price-value"}).get_text()
    star = item.find("em",attrs = {"class":"rating"})

    if "삼성전자" in name:
        print("삼성전자 상품 제외")
        continue
    
    #평점 4.5이상되는것조회
    if star:
        star = star.get_text()
        if float(star)>= 5.0 :
            print(f"이름:{name} 가격:{price} 평점:{star}")
        else:
            print("평점 4.5 이하 상품제외")
            continue

    else:
        star="평점없음"
        continue
    
   
        

    
    