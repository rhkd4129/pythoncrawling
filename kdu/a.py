from bs4 import BeautifulSoup
import urllib.request
from django import views
import pandas as pd
from urllib.parse import quote

def janhak(lastpage):
    janhak_list={}
    a,b,c=[],[],[]
    
    for page in range(1,lastpage+1):
        url = f"https://www.kduniv.ac.kr/kor/CMS/Board/Board.do?robot=Y&mCode=MN284&page={page}"
        search_url = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(search_url,'html.parser')
        titles = soup.select('.subject>p.stitle>a')
        dt = soup.select('td.date')
        views = soup.select('td.cnt')

        for t in dt:c.append(t.get_text())
        for v in views:b.append(v.get_text())
        for title in titles:
            z = title.get_text().replace("\t","").replace("\n","").replace("\r","")
            a.append(z[4:])
        a = list(range(1,5))
        for idx in range(page*len(a)):
            janhak_list[idx]= [a[idx],b[idx],c[idx]]
    return janhak_list

print(janhak(2).items())