from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from urllib.parse import quote
#클래스, 예외 파스칼
url = 'https://sports.news.naver.com/wbaseball/index'


def w_baseball(url):
    search_url = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(search_url,'html.parser')
    w_base_ball_news={}

    title = soup.select('ul.home_news_list li')
    for x in title:
        w_base_ball_news[x.a['title']] = 'https://sports.news.naver.com'+x.a['href']

    title = soup.select('ul.home_news_list division li')
    for x in title:
        w_base_ball_news[x.a['title']] = 'https://sports.news.naver.com'+x.a['href']

    # for key in news.keys():
    #     print(key, ":", news[key])
    return w_base_ball_news


def w_football(url):
    search_url = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(search_url,'html.parser')
    w_foot_ball_news={}
    title = soup.select('ul.home_news_list li')
    for x in title:
        w_foot_ball_news[x.a['title']] = 'https://sports.news.naver.com'+x.a['href']

    title = soup.select('ul.home_news_list division li')
    for x in title:
        w_foot_ball_news[x.a['title']] = 'https://sports.news.naver.com'+x.a['href']

    # for key in news.keys():
    #     print(key, ":", news[key])
    return w_foot_ball_news