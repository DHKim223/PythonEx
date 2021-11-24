#2-1
su = 5
dan = 800
total = su * dan
print("su 주소:",id(su))
print("dan 주소:",id(dan))
print("합계: ",total)

#2-2
x=2
y = 2.5*x**2+3.3*x+6
print("2차 방정식 결과  = ",y)

#2-3
print("지방의 그램을 입력하세요  :" ,end = " ")
fat = int(input())
print("탄수화물의 그램을 입력하세요  :" ,end = " ")
carb = int(input())
print("단백질의 그램을 입력하세요  :" ,end = " ")
prot = int(input())
total = fat*9 + prot*4 + carb*4
print("총칼로리 : ",total," cal")

#2-4
word1 = input('첫번째 단어 : ')
word2 = input('두번째 단어 : ')
word3 = input('세번째 단어 : ')
abbr = word1[0] +word2[0] + word3[0]
print("="*15)
print("약자 : ",abbr)