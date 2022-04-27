from urllib import request
from xml.sax.handler import property_interning_dict
from bs4 import BeautifulSoup 
import requests
import re


year = "2020"


for year in range(2015,2020):
    url =f"https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    images = soup.select("img.thumb_img ")

    for idx,image in enumerate(images):
        image_url = image["src"]
        image_res = requests.get(image_url)
        #image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year,idx+1),"wb") as f:
            f.write(image_res.content)
        if idx >=4: #상위 5개까지만
            break



#if url.startsith("//")
    # url중에 //로 시작하면 ~