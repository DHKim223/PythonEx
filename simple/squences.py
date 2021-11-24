### 열거형 ###
# 멤버쉽 테스트              in, not in, is 연산
# 인덱싱 연산                 
# 슬라이스 연산

# 문자열
a = "Hello Python!!!"

#  0   1   2  3  4  5  6  7  8  9 10 1112131415
# _H_ e_ l_ l_ o_ _P_y_t_h_o_n_!_!_!_\0_
print(a)
print(a[6])             # Java X... 자바에서는 문자열은 겍체... charAt(6) 으로 썼음
print(a[0:6])
print("=" * 10)

name='홍길동'
age = 30
#  에러 print("이름 : " + name + "\t" + "나이 : " + age) 
print("이름 : " + name + "\t" + "나이 : " + str(age))
print("이름 :" , name  , "\t" , "나이 :" , age) # ,는 형변환 안해도 됨.
print("이름 : %s \t 나이 : %d" %(name,age))
print("이름 : {0} \t 나이 : {1}".format(name,age))
print("이름 : {0:10} \t 나이 : {1:10}".format(name,age)) # 10칸 쓴다... 문자는 왼족부터 숫자는 오른쪽부터
print("이름 : {name} \t 나이 : {age}".format(name="김유신",age=40))

a = 1234.5678
print("{0:f}".format(a))
print("{0:10.2f}".format(a)) # 전체자리수 10개, 소수점 이하 2번째까지

b= "hello"
print("{0:10s}".format(b))
print("{0:<10s}".format(b))
print("{0:>10s}".format(b))
print("{0:^10s}".format(b))
print("{0:=^10s}".format(b))
print("{0:-^10s}".format(b))

# 슬라이싱 연산
#  0   1   2  3  4  5  6  7  8  9 10 1112131415
# _H_ e_ l_ l_ o_ _P_y_t_h_o_n_!_!_!_\0_
a = "Hello Python!!!"

print(a) # 0번 ~ null 전까지 출력
print(a[:5]) # 0번~4번까지
print(a[:6]) # 5까지 ,, end index - 1
print(a[6:]) # 6에서 끝까지
print(a[:-2]) # 뒤에서 두개 빼고

print(len(a))
print(a.count("l"))
print(a.find("a")) # 못찾으면 -1
print(a.find("o"))
#print(a.index("a")) # 못찾으면 에러
print(a.index("o"))
print(",".join(a))

s = " a a a "
print(s)
print(s.lstrip())
print(s.rstrip())
print(s.strip())

ss = "a, b, c, d, e, f"
print(ss.split()) # white space 의미없는 여백
print(ss.split(","))

b = "123abc"
print(b.isalnum())
print(b.isnumeric())
print(b.isdigit())
print("0123".isdigit())
print("0abc".isidentifier())
print("="*50)
print("_abc".isidentifier())
print("___abc".isidentifier())
print("a&bc".isidentifier())
print("123abc".isidentifier())
print("ABC".isidentifier())
print("가나다".isidentifier()) # 하지만 한글은 쓰지 말것


# 문자열 함수

#튜플 # 객체를 여러개 담는다
#리스트와 다르게 변경이 안된다.
# 인덱싱
# () 로 묶는다
# 단순한 값의 나열 / 함수의 리턴

# tuple        list -> tuple
# list            tuple -> list
# 복사본을 만들어서 메모리 낭비가 생긴다.

zoo = ("cat","dog","snake","spider")
print(zoo)
zoo = zoo, "lion" # 튜플에 튜플이 들어간다....
print(zoo)
print(zoo[0])
print(zoo[1])
print(zoo[0][2])
print(zoo[0][1:3]) # end index - 1
print(len(zoo))
print(len(zoo[0]))

z = list(zoo)
print(type(z))

a,b,c,d = zoo[0] # 튜플로 리턴하면 하나의 함수가 여러개를 리턴하는 효과!!!!
print(a,b,c,d)


#리스트        배열과 비슷
# 순차적인 객체들의 집합
# 인덱싱 슬라이싱
# [] 로 표시
# 추가 삽입 삭제 수정 가능

fruits = ["banana", "apple","pear","grape"]
print(fruits)
print(fruits[1])
print(fruits[1:3])
print(fruits[:-1])
print(fruits[:2])
print(fruits[2:])
print(fruits[1][0]) #a
print(fruits[1][:3]) #app

print(len(fruits))
print(max(fruits))
print(min(fruits))

fruits.append("orange")
print(fruits)
print(fruits.count("apple"))

fruits.append("apple")
print(fruits.count("apple"))
print(fruits.count("apple"))
print(fruits.index("apple"))
fruits.insert(2,"watermelon")
print(fruits)

fruits.remove("watermelon")
print(fruits)
fruits.sort()
print(fruits)

fruits.sort(reverse = True)
print(fruits)

print("="*50)
# 하위 리스트
shop =["햇반","김치","계란"]
shoplist = shop, fruits
print(shoplist) # 튜플안에 리스트가 들어가는 형태
shoplist = [shop,fruits] # 리스트안에 리스트 들어가는 형태
print(shoplist)
print(shoplist[0]) # shop 리스트
print(shoplist[1]) # fruits 리스트
print(shoplist[0][1]) # 김치
print(shoplist[1][1:3]) # 'orange' ' grape'
shoplist[0].append("도시락")
print(shoplist[0])

### 맵형 ###
# 딕셔너리
# key value 한쌍으로 구성
# 순서는 상관없다
# key  단순한 객체로 구성
# {key:value, key:value......}            JSON 형식과 비슷

# 인덱싱 , 슬라이싱 X
# 반복문 X

kim = {"name":"김유신","age":30,"tel":"1111-2222","address":"서울시"}
print(kim)
print(type(kim))  # class 'dict'
print(kim["name"]) # 김유신 
print(kim.get("name"))

for key, value in kim.items() :
    print(key,value)

# 키는 중복 불가능
if 'id' not in kim.keys():
    kim["id"] = "aaa"
print (kim)

# Set 집합
# index 없다.
# 단순한 묶음
# 중복이 안된다.
# 데이터가 많으면 느리다.

country = set(["korea","japan","china","russia","taiwan"]) # 인덱스가 없어서 순서없다... 주머니에 공넣었다 빼는 ....
print(country)
print(type(country))

country.add("finland")
print(country)
country.add("korea") # 중복이 안된다
print(country)

country.remove("japan")
print(country)

nation = country.copy()
print(nation)
nation.add("japan")
nation.add("usa")
print(nation)

print(nation - country)
print(nation | country)
print(nation & country)

print("china" in nation)

# & 교집합 ,,,, | 합집합 ,,,,,,,,, - 차집합
