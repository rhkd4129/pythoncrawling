import re
# 정규식 표현: 정해진 형태
#나도코딩님의 강의 내용 -------------------------

#p = re.compile("ca.e")
#def print_match(m):
#    if m:
#        print(m.group())
#    else:
#        print("매칭x")
#
#m = p.match("case")
#print_match(m)
#print(m.group())   #매치되지않으면 에러발생


# 1. p = re.compile("원하는 형태")      
# 2. m = p.match("비교할 문자열")       주어진 문자열의 처음부터 일치하는지 화인 
# 3. m = p.search("비교할문자열")       주어진 문자열 중에 일치하는게 있는지 확인
# 4. lit = p.findall("비교할 문자열 ")  일치하는 모든 것을 리스트 형태로 반환
# 원하는 형태 : 정규식

# .: (ca.e):    하나의 문자 의미    >  care,cafe             |caffe  x
# ^:  (^de):    문자열의 시작       >  dese,destination      |  fade  x 
# $:  (se$):    문자열의 끝         > case,base              | face  x
# *:  s*t:      반복(0번도됨)           
# +:  sa+t:     반복(0번이안됨)
# {}  ca{2}t    반복{m,n}a가 m이상n이하 반복되면 매치
# ?   ab?c      0이나 1번 사용되면 == {0,1}같은 표현
#-----------------------------------------------------------------------------

