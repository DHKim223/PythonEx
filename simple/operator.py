a = 10
a **=2



# bit not  1의 보수 연산자
a= ~a 
a= ~a + 1 #2의 보수 연산 ,,,,, 양수 <-> 음수
print(a)

print('ABC','DEF')
print('ABC'+'DEF')
print('ABC' 'DEF')
print('{0:10s}{0:10s}'.format('ABC, DEF'))

# and , or 로 직접사용.. && || 사용불가.

# equls 대신에..
print("Hello" in "Hello World")
print("Hello" not in "Hello World")
print ("Hello" is "Hello")
print("Hello" is "hello")

a = "Hello"
b = "Hello"

print (a==b)
print(a is b)

a+="Python!!!"
b+="Python!!!"
print( a==b )  # 내용비교
print( a is b ) # 주소비교

#산술 대입연산자
a=10
a +=10; print(a)