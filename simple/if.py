#### 제어문 ####
# 조건문
# switch case 없음
# if ~ else문
if 5>2 : 
    print("크다")
else : 
    pass

a = 50
if a>= 0 and a<= 100:
    print("적정")
else :
    print( "오류")
    
# if ~ elif ~ else 문
#===============================================================================
# print("나이  :", end = "")
# age = int(input())
# if age <= 20:
#     print("어린이")
# elif age <= 40 :
#     print("청년")
# elif age <= 60:
#     print("장년")
# else:
#     print("노년")
#===============================================================================

# 반복문 
# for 
#for i in range(10): # 0 ~ 9
#for i in range(1,10): # 1~9
#for i in range(1,11,2) : # 시작값, 끝값-1 , 증감값
for i in range (10, 0, -1) :# 10~1
    print(i, end =" ")
print()

# 나열형
str = "Hello Python!!!"     # 문자열은 문자가 나열
for s in str:
    print(s,end = " ")
print()

nums = ( 10,20,30,40,50) # 튜플
for num in nums:
    print(num, end= " ")
print()

nums = [10,20,30,40,50] # list
for num in nums:
    print(num,end=" ")
print()

nums = set ([1,2,3,4,5])
for num in nums :
    print(num,end=" ")
print() 

names = {"kim":"김유신","lee":"이순신","hong":"홍길동"}
print(type (names))
for key, value in names.items(): # items() -- 맵을 튜플로
    print(key,value)

nums = [(1,2),(3,4),(5,6),(7,8),(9,10)]
print(type(nums))
print(nums[0][0])
print(nums[0])
a, b = nums[0]

nums = [(1,2,3),(4,5,6),(7,8,9)]
for a, b,c in nums :
    print(a,b,c)
    
# 리스트 축약
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)
nums = [i for i in range(0,10)]
print(nums)
nums = [i**2 for i in range(1,10)]
print(nums)

# 60점 이상이면 합격 아니면 불합격 출력


scores = {'kim':89 , 'lee':65, 'park':45,'jung':96, 'choi':55, \
          'cho':50, 'hong':44,'hwang':60, 'ki':87, 'sung':35}

for key, value in scores.items():
    if value >= 60 :
        print(key,'\t','합격')
    else :
        print(key,'\t','불합격')
        
scores = [('kim',89) , ('lee',65), ('park',45),('jung',96), ('choi',55), \
          ('cho',50), ('hong',44),('hwang',60), ('ki',87), ('sung',35)]

for name, score in scores:
    if score >=60:
        print(name,"합격")
    else :
        print(name, "불합격")
    
for i in range (0,len(scores)):
    if(scores[i][1] >= 60) :
        print(scores[i][0],'\t','합격')
    else:
        print(scores[i][0],'\t','불합격')
        
# while
# while ~ else
for i in range(1,11):       # 시작값 끝값 증감값
    print(i,end =' ')
print()

i=0 # 시작값
while i < 10 :
    i += 1
    print(i,end=" ")
else : 
    print("끝")
print()

i=0
while(True) : 
    i += 1
    print(i,end=" ")
    if i==10:
        break
print()

i=0
while(True) : 
    i += 1
    if i%2 ==1:
        continue
    print(i,end=" ")
    if i==10:
        break
print()

#enumerate() 반복을 못돌리는애 반복을 돌릴 수 있게 만든다..?
s = set(["kim",'lee','park','jung','hong'])
for i, name in enumerate(s,100):
        print(i,name)
              
# 다중 반복문
# 구구단 가로로 출력
i=1
while(True):
    i += 1
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end = '\t')
    print()
    if i ==9:
        break
    

for i in range(1,10):# 곱해지는 수
    for j in range(2,10): #단
        print(j,"*",i,"=",i*j,end="\t")
    print()
print()