### 함수 function ###
# 사용자 정의 함수
# 반복되는 내용을 묶어서 처리
# 선언 구현 호출해야 한다
# 반드시 호출한 자리로 돌아온다
# 듀플로 리턴이 가능해 여러 값을 리턴할 수 있는 효과
# 반환값이 없으면 None 이 반환

# 기본형
# 접근제한자 반환형 함수명( 매개변수,.....) {            # Java 메서드        클래스내에서만 구현
#     실행문;
#}

# def 함수명(매개변수,...) :                     일반함수                 멤버함수 / 일반함수
#     실행문 ;

def hello():                                    # 선언
    print("Hello Python!!!")            # 구현

hello()                                             # 호출
    
# 매개변수
# def max(a,b):
#     if a>b:
#         print(a,"가 크다")
#     elif b>a:
#         print(b,"가 크다")
#     else:
#         print("같다")
#
# max(5,2)
# max(5,5)   
# max(5,8)

 #return
def min(a,b):                       # 반환형이 없다
    if a>b:
        return b                        # int
    elif b>a:
        return a                        # int
    else:
        return "같다"                 # str
    
print(min(1,2))
print(min(3,2))
print(min(2,2))

# 여러값을 리턴
def calc(a,b):
    return (a+b, a-b, a*b, a/b)
 
hap,cha,gop,mok = calc(5,2)
print(hap,cha,gop,mok) # 단 갯수를 맞춰서 리턴 받아야한다.

# 매개변수의 초기값
# 오버로드                매개변수의 개수가 다르거나 순서가 다르거나 자료형이 다르거나
# 오버로드가 안된다

# def hap(a,b,c):
#     return a+b+c
# def hap(a,b):            #파이썬에선 불가
#     return a+b
print("합*50")
def hap(a=1, b=1, c=1):     # 처음 초기값을 준 매개변수 뒤의 모든 매개변수는 초기값이 필요하다.
    return a+b+c
print(hap(2,3,7))
print(hap(2,3))
print(hap(2))
print(hap())

# VarArgs 매개변수
#  *param
def gop(*param):                # *param     튜플이 된다.
    #print(param)
    sum = 1
    for i in param:
        sum*=i
    print(sum)
gop(1,2,3,4,5)   
gop(1,2,3)
print("차"*50)
# **param                                # 키워드 인수
# 인수에 이름 부여
def cha(a,b=0,c=0): 
    return a-b-c;
print(cha(2,5,7))
print(cha(2,5))
print(cha(2))

print(cha(c=10, a=20))          # 초기값 없는 a는 반드시 포함
print(cha(10,c=20,b=30))

#키워드 인수 사전 ( dict )
def add(a,**param):                     # **param 은 dict
    print(a, end=" ")
    for key, value in param.items():
        print(key, value)

add(10,b=20,c=30)
add(10,b=20,c=30, d=40, e=50)

# VarArgs 키워드인수사전 순서
def sum(a, *args, **param):
    print('변수:',a, end=" ")                           #변수
    print()
    print('튜플:',args, end=" ")                        #튜플
    print()
    print('dict: ',end=" ")
    for key, value in param.items():        #딕셔너리
        print(key,value,end = " ")
    print()
print()
sum(10, 20, 30 ,40) # 10은 a 가 ,  2340 은 *args 가
sum(10,'A','B','C', b=20, c=30)             # (b=20, c=30) 이 키워드 인수부분
#sum(10,b=20,c=30,20,30,40) # 순서에 맞지 않아 에러난다.
print()
#지역변수/전역변수
#Java        전역변수        가장 큰 {} 안에 있는 변수. 클래스 변수(멤버변수) _____ 자바는 영역 밖에 코딩이 안된다.
#               지역변수        특정 영역안에 선언한 변수
#Python    전역변수        {} 밖에 구현하는 변수. 일반변수
#                지역변수        특정 영역안에 선언한 변수

# 전역변수
a = 10
a = 100 # 재할당

def disp():
    global a
    print(a)                #전역변수를 지역에서 사용할 때는 global 명시 해야함.
  
    a=10                    # 지역변수를 재할당하면 에러
    print(a)
    
disp()
print()
# 1
a, b =10, 20

def hap1():
    global a         # global 이라고 쓰는건 전역변수와 같은 이름의 지역변수를 쓸때.... 이런 경우는 안써도 된다.
    global b
    print(a+b)

def cha1():
    global a
    global b
    print(abs(a-b))

def gop1():
    global a
    global b
    print( a*b)

def mok1():
    global a
    global b
    print( a%b)

hap1()            #합
cha1()           #차
gop1()        #곱
mok1()               #몫
print()

# 2
def hap2(a , b):
    print(a+b)

def cha2(a , b):
    print(abs(a-b))

def gop2(a , b):
    print(a*b)
    
def mok2(a , b):
    print(a%b)
    
hap2(10, 20)
cha2(10, 20)
gop2(10, 20)
mok2(10,20)

# 내장함수
# print()
# input()
print(abs(-3))
print(all ( [1,2,3] ) ) # 0이 아니면 다 참 # True
print(all ( [1,2,3,0] ) ) # False
print(any ([0,1]))      # True    하나라도 참이면 True
print(any ([0,""]))     # False "" 는 False " " 는 True

import sys
print (dir(sys)) # sys라는 모듈에 사용할 수 있는 함수,변수 list
print (dir())                               # 현재 파일(모듈) 에서 사용할 수 있는 멤버

print( divmod( 7,3 )) #  몫 나머지 출력
print(eval("1+2"))

a = 3
print(id(a))

print( max( "python" ) ) # min  도 가능

print(pow(10,3)) # 1000 = 10**3

print(sorted([2 , 7, 8, 5, 3 ]))
print(list(zip([1,2,3],[4,5,6]))) # 14 25 36 끼리 묶어줌

## 람다함수 ##
def multiply(a,b):
    return a*b
print(multiply(10,20))

multy=(lambda a,b : a*b)
print(multy(10,20))

print((lambda a,b : a*b)(3,4))

def even(a):
    return a%2 == 0
print(even(10))
print(even(9))
print((lambda a : a%2==0)(10))
print((lambda a : a%2==0)(9))

# filter
# filter( 함수 , list )                # list 값들을 함수로 처리한 후 골라낸다
print(list(filter(even, range(1,11))))                                      # 함수형 언어, 자체 반복문
print(list(filter(lambda a:a%2==0, range(1,11))))                   

# map                                        # Hadoop 분석 맵,리듀스 분석
print(list(map(lambda a  : a%2==0 , range(1,11))))

# reduce ( 함수, list)
from functools import reduce
print(reduce ( lambda a,b:a+b, range(1,11)))

