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

    titles = soup.select('ul.home_news_list li')
    for title in titles:
        w_base_ball_news[title.a['title']] = 'https://sports.news.naver.com'+title.a['href']

    links = soup.select('ul.home_news_list division li')
    for link in links:
        w_base_ball_news[link.a['title']] = 'https://sports.news.naver.com'+link.a['href']

    # for key in news.keys():
    #     print(key, ":", news[key])
    return w_base_ball_news


def w_football(url):
    search_url = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(search_url,'html.parser')
    w_foot_ball_news={}
    titles = soup.select('ul.home_news_list li')
    links = soup.select('ul.home_news_list division li')
    for title in titles:
        w_foot_ball_news[title.a['title']] = 'https://sports.news.naver.com'+title.a['href']

    for link in links:
        w_foot_ball_news[link.a['title']] = 'https://sports.news.naver.com'+link.a['href']

    return w_foot_ball_news