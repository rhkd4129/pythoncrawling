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





