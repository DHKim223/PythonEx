#3-1a
weight = int(input("짐의 무게는 얼마입니까? : "))
if weight >=10:
    print("수수료는 만원 입니다")
else:
    print("수수료는 없습니다")

#3-1b
weight = int(input("짐의 무게는 얼마입니까? : "))
if weight >=10:
    print("수수료는",int(weight/10)*10000,"원 입니다")
else:
    print("수수료는 없습니다")

# 3-2
import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1,10) # 1~10 사이 랜덤정수발생

while True:
    my = int(input('예상 숫자를 입력하시오 : ')) # 숫자입력
    if my>com :
        print('더 작은수를 입력하세요')
    elif my<com:
        print('더 큰 수를 입력하세요')
    else:
        print('정답입니다!')
        break

# 3-3
print('수열 : ',end = " ")
sum=0
for i in range(1,100): 
    if i%3==0 and i%2 != 0:
        print(i,end=" ")
        sum += i
print()
print('합계 : ',sum)

#3-4
multiline="""안녕하세요. 파이썬 세계로 오신걸 환영합니다. 파이썬은 비단뱀 처럼 매력적인 언어입니다."""
cnt = 0
splited = multiline.split(" ")
for i in range(0,len(splited)):
    print(splited[i])
    cnt += 1
print('단어개수 : ',cnt)
