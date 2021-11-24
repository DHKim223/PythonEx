# 실행

# import 모듈명
# import 모듈명 as 모듈별칭
# from 모듈명 import 변수 or 함수        모듈 이름을 생략하고 함수 사용 가능
# from 모듈명 import  *            해당 모듈의 __ 로 시작하는 이름을 제외한 모든것
# from 모듈명 import  이름 as 별칭

import module.mymodule as md        #패키지.모듈명
# module.mymodule.hello()
# module.mymodule.bye()
md.hello()
md.bye()

from module.mymodule import hello, bye , User   # from 패키지.모듈명 import 이름
hello()
bye()
user = User("홍길동",30)
print(user.getName())
print(user.getAge())

from module.mymodule import *                           # __로 시작하는 이름을 제외한 모든것
hello()
bye()
user = User("홍길동",30)
print(user.getName())
print(user.getAge())

from module.mymodule import User as U
u = U("이순신",30)
print(u.getName())
print(u.getAge())

print("="*50)
## 자주 사용하는 모듈 ##
# os 모듈 #
import os 
for file in os.listdir("/"):
    print(file) 

print("절대경로 : " + os.path.abspath("."))

path = "c:/"
for file in os.listdir(path):
    if os.path.isdir(path+file) :
        print("폴더 :",file)
    else :
        print("파일 :",file)
    print(os.path.split(path+file))
print("절대경로 : " + os.path.abspath("."))

# sys 모듈 #
import sys
print(sys.path)             # 현재 파이썬 path 변수의 값
print(sys.version_info) # 파이썬 버전
print(type (sys.version_info))
print(sys.version_info.major)
# sys.exit(0) # 프로그램 종료

# logging 모듈#
# CRITICAL 50
# ERROR     40
# WARNING 30
# INFO            20
# DEBUG        10
# NOTSET         0

import os, platform, logging
#print(platform.platform())
if(platform.platform().startswith("Window")):
    logfile = os.path.join(os.getenv("HOMEDRIVE"),os.getenv("HOMEPATH"),"test.log")
else:
    logfile = os.path.join(os.getenv("HOME"),"test.log")
print(logfile)
    
logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s:%(levelname)s : %(message)s",
    filename = logfile,
    filemode="w"
    );
logging.debug("프로그램이  시작됐습니다.")
logging.info("정상 동작중입니다")
logging.warning("경고가 발생했습니다")
logging.error("에러가 발생했습니다")

from datetime import date, time ,datetime, timedelta
now = date.today()
print(now.year,"년",now.month,"월",now.day,"일")
print(now)

today = datetime.today()
print(today.year,"년",today.month,"월",today.day,"일",\
      today.hour,"시",today.minute,"분",today.second,'초',today.microsecond)
print(today)

#print("{0}".format(now + 30))           # date + int 라 오류
print("{0}".format(now + timedelta(30)))     # 시간 계산시 timedelta 사용

# 날짜를 문자로
print(today.strftime("%y-%m-%d %H:%M:%S")) # 형식지정

# 문자열을 날짜로
myday = "2021-09-06 12:32:13"
print(datetime.strptime(myday,"%Y-%m-%d %H:%M:%S"))

# random 모듈 #
import random
for j in range(10):
    for i in range (6) :
        print(int(random.random()*100)+1, end=" ") # 1~100
    print()
    
print("="*50)
for j in range(10):
    for i in range (6) :
        #print(int(random.random()*45)+1, end=" ") # 1~45
        pass
    lotto = random.sample(range(1,46),6) # 중복없이 범위내에서 6개
    # lotto.sort()
    # print(lotto)
    print(sorted(lotto))    # list 함수 sorted() 리턴 O, sort() 리턴 X
    print()
    
    random.shuffle(lotto)
    print(lotto)
    
# CSV (Comma Separator Values) 모듈 #
f = open("a.txt","a")           # 텍스트모드 ( 기본값 ) b (바이너리모드)
for i in range(10):
    f.write(str(i))
f.write("\n")    
f.close()

# f = open("a.txt","r")
# while True:
#     line = f.readline()
#     if not line :           # 데이터가 없으면
#         break
#     print(line, end="")
# f.close()

with open("a.txt","r") as f:                # close 를 자동으로 처리
    while True:
        line = f.readline()
        if not line:
            break
        print(line,end = "")
        
with open( "lotto.csv", "w" ) as f :
    for i in range( 10 ) :
        lotto = random.sample( range(1, 46), 6 )
        lotto.sort()
        for j in lotto :
            f.write( str(j) + "," )
        f.write( "\n" )
        
with open( "lotto.csv","r") as f:
    for line in f:
        for num in line.split(","):
            print(num, end = " ")
            
# pickle 모듈 #
# 피클링 ( 절임??? )    객체 단위 입출력
# Java            객체 단위 입출력 Object Input / Output Stream
#                    객체 직렬화가 필요 파이썬에선 X

class Member :
    def __init__(self,name="",age=0,tel=""):
        self.name = name
        self.age = age
        self.tel = tel
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getTel(self):
        return self.tel
hong = Member("홍길동",30,"1111-2222")

import pickle
with open("member.txt","wb") as f:   # binary 라 txt파일은 깨져보임... 불러오면 이상 무
    pickle.dump(hong,f)
    
with open ("member.txt","rb") as f:
    member = pickle.load(f)
    print("이름 : ",member.getName())
    print("나이 : ",member.getAge())
    print("전화번호 : ",member.getTel())
    
#Java                 컬렉션을 활용                      컬렉션과 맵이 직렬화 되어 있어서
members = [Member("kim", 20, "1111-2222"), 
           Member("hong", 30, "2222-3333"), 
           Member("lee", 25, "1111-3333")]
    
with open( "member.txt", "wb" ) as f :
    pickle.dump( members, f )
with open( "member.txt", "rb" ) as f :
    datas = pickle.load( f )
    for data in datas :
        print( data.getName(), data.getAge(), data.getTel() )  

# 유효성 검사

        
    