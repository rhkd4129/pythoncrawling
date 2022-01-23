import bs4
from bs4 import BeautifulSoup 
import requests
import re



url ="http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=beautifulsoup&queryText=&iStartCount=0&iGroupView=5&icate=all&colName=re_a_kor&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=search&isFDetailSearch=N&sflag=1&searchQuery=beautifulsoup&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=beautifulsoup&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn="
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

search_number= soup.find("span",attrs={"class":"num"}).get_text()

title =soup.select('div.cont > p.title')

print(f"{title}건의 검색결과")
for x in title:
    print(x.get_text())
    print("http://www.riss.kr"+x.a["href"])