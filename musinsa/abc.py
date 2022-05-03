from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

url="https://www.musinsa.com/category/001"
search_url = urllib.request.urlopen(url).read()
soup = BeautifulSoup(search_url,'html.parser')
subjects = soup.find_all('li',attrs={'class':'li_box'})
df = pd.DataFrame(columns=('name','가격'))

for i,subject in enumerate(subjects):
    sale = subject.find("div",attrs={"class":"icon_new"})
    title = subject.select('div.article_info > p.list_info>a')[0].get_text().replace("\t","").replace("\r","").strip()
    price = subject.find("p",attrs={"class":"price"})
    if price != None:
        price = price.get_text().replace("\t","").replace("\r","").strip()
    else:price = "null"
    df.loc[i] = [title,price]

print(df)
