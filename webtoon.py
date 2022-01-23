import requests
from bs4 import BeautifulSoup

#나도코딩님의 강의 내용
#value = key 
#https://comic.naver.com/webtoon/list?titleId=683496&weekday=tue&page=26


def webton_title_extract(page_number):
    for page in range(1,page_number):
        url = f"https://comic.naver.com/webtoon/list?titleId=683496&weekday=tue&page={page}" 
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text,'lxml')
        title_lst = soup.find_all("td",attrs={"class":"title"})
        for x in title_lst:
            print(x.a.get_text())

webton_title_extract(5)












#webtoon_title_lst = soup.find_all("td",attrs={"class":"title"})
#link = webtoon_title_lst[0].a["href"]

#만화제목 
#print(webtoon_title_lst[0].a.get_text())
#print("https://comic.naver.com"+link)
#for webtoon in webtoon_title_lst:
#    print(webtoon.a.get_text(),end='',sep='url')
#    print("https://comic.naver.com"+webtoon.a["href"])


#평점
#total_rates =0
#webtons = soup.find_all("div",attrs={"class":"rating_type"})

#print(webtons[0].get_text())

#for webton in webtons:
#        rate = webton.find("strong").get_text()
#        print(rate)
#        total_rates = float(rate)+float(total_rates)
#print(total_rates)
#print(total_rates/len(total_rates))
