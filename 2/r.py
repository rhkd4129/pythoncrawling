from c import w_baseball,w_football


base  = w_baseball('https://sports.news.naver.com/wbaseball/index')
foot  = w_football('https://sports.news.naver.com/wfootball/index')

for key in base.keys():
    print(key+":"+base[key])

print("--"*10)
for key in foot.keys():
    print(key+":"+foot[key])