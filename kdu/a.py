from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from urllib.parse import quote

def janhak():
    janhak_list={}
    a,b,c=[],[],[]
    page= 1
    # for page in range(1,lastpage+1):
    url = f"https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN284&page={page}"
    search_url = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(search_url,'html.parser')

    titles = soup.select('.subject>p.stitle>a')
    dt = soup.select('td.date')
    views = soup.select('td.cnt')
    # a = list(range(1,5))



    for t in dt:c.append(t.get_text())
    for v in views:b.append(v.get_text())
    for title in titles:
        z = title.get_text().replace("\t","").replace("\n","").replace("\r","")
        a.append(z[4:])

        
    for idx in range(1,len(a)):
        janhak_list[idx]= [a[idx],c[idx]]
        # ,,c[idx]
    return janhak_list


df = pd.DataFrame(janhak())
# s = pd.Series([1,3,4])
print(df)