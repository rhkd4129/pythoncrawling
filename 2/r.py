
from c import w_baseball,w_football
import numpy as np
import pandas as pd



base  = w_baseball('https://sports.news.naver.com/wbaseball/index')
foot  = w_football('https://sports.news.naver.com/wfootball/index')
base_news = pd.Series(base.keys())
base_link = pd.Series(base.values())
foot_news = pd.Series(foot.keys())
foot_link = pd.Series(foot.values())
a = pd.DataFrame({
    '기사':base_news,
    '링크':base_link                
})
print(a)
