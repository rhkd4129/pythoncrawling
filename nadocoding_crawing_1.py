import requests
from bs4 import BeautifulSoup

#나도코딩님의 강의 내용

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) #첫번째 a
#print(soup.a.attrs) #첫번째 a 의  속성정보 출력
#print(soup.a["href"]) a 의 href 속성 값 출력

#print(soup.find("a",attrs={"class":"Nbtn_upload"}))    #해당하는 첫번째 엘리먼트
#print(soup.find("div",attrs={"class":"Nbtn_upload"}))


#print(soup.find("li",attrs = {"class":"rank01"}))
#rank1 =soup.find("li",attrs = {"class":"rank01"})
#print(rank1.a.get_text())
#print(rank1.next_sibling.next_sibling())  #next_silbling 다음 형제태그로 넘어감 
                                          #햇는데 안나오면 개행이 있을수도잇음 그래서 한번더쓰기
#rank2=rank1.next_sibling.next_sibling
#rank3=rank2.next_sibling.next_sibling
#rank3=rank2.next_sibling.next_siblings  s를 붙이면 하나만찾는 것이 아닌 모두 찾는다
#print(rank3.a.get_text())


#rank2 = rank3.previous_sibling.previous_sibling #뒤에 형제 태그
#print(rank2.a.get_text())

#print(rank1.parent)  #부모태그
#rank1.find_next_sibling("li")  # 다음 태그중에 조건에 해당하는 

#print(soup.prettify())


#webtoon = soup.find("a",text="독립일기 -11화") #a태그와 text내용의 해당하는 것을 찾아라