import requests
from bs4 import BeautifulSoup

#beautifulsoup(html코드,html번역선생님)

# naver 서버에 대화를 시도
response = requests.get("http://naver.com")
response.raise_for_status()
a = response.text # text안에 html파일이 들어있음


soup = BeautifulSoup(a,'html.parser')
soup.select #여러개
word = soup.select_one("#NM_set_home_btn") #원하는 태그 한개  id는 #

#print(word)
print(word.text)


#find 의 목적은 원하는 태그를 찾는것 
tag = "<p class='youngone' id='junu'> Hello World! </p>" 
soup = BeautifulSoup(tag) 
# 태그 이름만 특정 soup.find('p') #
# 태그 속성만 특정 soup.find(class_='youngone') soup.find(attrs = {'class':'youngone'})
# 태그 이름과 속성 모두 특정 soup.find('p', class_='youngone')



# select는 CSS selector로 tag 객체를 찾아 반환한다. 
# 이는 CSS에서 HTML을 태깅하는 방법을 활용한 메소드다. 
# 가장 첫 번째 결과를 반환하는 select_one()은 find()에, 
# 전체 결과를 리스트로 반환하는 select()는 find_all()에 대응한다.

# 태그 이름만 특정 soup.select_one('p') # 태그 class 특정 
# soup.select_one('.youngone') # 태그 이름과 class 모두 특정 
# soup.select_one('p.youngone') # 태그 id 특정 soup.select_one('#junu') 
# 태그 이름과 id 모두 특정 soup.select_one('p#junu') 
# 태그 이름과 class, id 모두 특정 soup.select_one('p.youngone#junu')

#find soup.find('div').find('p') 
# #select soup.select_one('div > p')



# 원하는 정보가 있는 위치 찾기 

soup.select('원하는 정보')  # select('원하는 정보') -->  단 하나만 있더라도, 복수 가능한 형태로 되어있음

soup.select('태그명')
soup.select('.클래스명')
soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')    # 바로 아래의(자식) 태그를 선택시에는 > 기호를 사용
soup.select('상위태그명.클래스명 하~위태그명')              # 아래의(자손) 태그를 선택시에는   띄어쓰기 사용
soup.select('상위태그명 > 바로아래태그명 하~위태그명')     
soup.select('.클래스명')
soup.select('#아이디명')                  # 태그는 여러개에 사용 가능하나 아이디는 한번만 사용 가능함! ==> 선택하기 좋음
soup.select('태그명.클래스명)
soup.select('#아이디명 > 태그명.클래스명)
soup.select('태그명[속성1=값1]')

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