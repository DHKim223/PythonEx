# #4-1
# lst = [10,1,5,2]
# result = lst*2
# print('단계 1:' ,result)
# result.append(lst[0]*2)
# print('단계 2:', result)
#
# result2=[]
# for i in range (0,len(result)):
#     if(i%2==1):
#         result2.append(result[i])
# print('단계 3: ',result2)

# #4-2a
# import random
#
# size = int(input("vector 수 : "))
# vector=[]
# for i in range(size):
#     vector.append(random.randint(1,10))
#     print(vector[i])
# print('vector 크기 : ',len(vector))

# #4-2b
# import random
# size = int(input("vector 수 : "))
# vector=[]
# for i in range(size):
#     vector.append(random.randint(1,10))
#     print(vector[i])
# guess = int(input("찾는 수를 입력하세요: "))
# if guess in vector:
#     print("Yes")
# else:
#     print("No")
    
#4-3a
message = ['spam','ham','spam','ham','spam']
# dummy=[]
# for i in range (len(message)):
#     if(message[i] == 'spam'):
#         dummy.append(1)
#     else:
#         dummy.append(0)
# print(dummy)

# dummy=[1 if msg == 'spam' else 0 for msg in message]
# print(dummy)

# #4-3b
# spam_list = [msg for msg in message if msg =='spam']
# print(spam_list)

#4-4
position = ['과장','부장','대리','사장','대리','과장']

uni_position = list(set(position)) # position 을 set() 함수를 이용해 set 으로 변경... 중복제거... list 로 변경... index 사용가능
print("중복되지 않는 직위 : ",uni_position)

wc = {} # 빈 셋
for key in position: # 키 넘김
    wc[key] = wc.get(key,0)+1   # key = value ( value 가 없다면 0으로 초기화, 있다면 +1)
print('각 직원별 빈도수: ',wc)



