from traceback import print_tb
from bs4 import BeautifulSoup
import urllib.request

# res = requests.get(url,headers = headers)
# res.raise_for_status()
url = "https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?mCode=MN246"
search_url = urllib.request.urlopen(url).read()

soup = BeautifulSoup(search_url,'html.parser')
a,b,c=[],[],[]

titles = soup.select('p.stitle a')
dt = soup.select('td.date')
writers = soup.select('td.writer')

# a=list( titles[0].get_text().replace("\t","").replace("\r","").replace("\n",""))
# print(a)
for x in titles:a.append(x.get_text().replace("\t","").replace("\n",""))
for x in dt:b.append(x.get_text())
for x in writers:c.append(x.get_text().strip())
