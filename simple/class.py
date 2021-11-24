### 클래스 ###
# Java                         클래스 위주로 프로그래밍        객체지향
#                                 클래스 하나로 파일 하나 구성
# Python                    모듈 위주로 프로그래밍            모듈지향?
#                                 전역변수 일반함수 클래스 파일 구성
from pickle import NONE
from simple.squences import name, age
from _ast import Name

# this -> self           멤버는 무조건 명시해야 한다. 멤버함수에서 self 첫번째 인자로 명시

## 캡슐화 ##
# 접근제한자 #
# private                    _ 또는 __ 
__a = 10            # 일반변수        private X
def getA():         # 일반함수
    return __a
print(getA())

class P :           # 클래스                             새로운 자료형 설계한 설계도
    __a = 100                       # private
    b = 200                             # default
    def getA(self):
        return self.__a
    def getB(self):
        return self.b
    def setA(self , a):
        self.__a = a
    def setB(self ,b):
        self.b = b
p = P()
#print('a : ' , p.__a)    #private 이기 때문에 접근이 막혀있다
#print("b : ",p.b)
print('a : ',p.getA())
print('b : ',p.getB())
p.setA(10)
p.setB(20)
print('a : ',p.getA())
print('b : ',p.getB())
print("a: ",p._P__a)        # private 접근 가능. 캡슐화가 완벽하지 않다.

# 캡슐화 적용

class Person:
    __name = None
    __age = 0
    __tel = None
    def getName(self):
        return self._name
    def getAge(self):
        return self._age
    def getTel(self):
        return self._tel
    def setName(self,name):
        if len(name) >10:
            print("10글자 이내로 입력하세요")
        else:
            self._name = name
    def setAge(self, age):
        if age > 150 or age<1:
            print("1~150살 만 임력하세요")
        else:
            self._age = age
    def setTel(self,tel):
        if len(tel) >15:
            print("15글자 이내로 입력하세요")
        else:
            self._tel = tel
       

kim = Person()
kim.setName("김유신")          # 10 글자 이하만
kim.setAge(20)                      # 1 ~ 150
kim.setTel('1111-2222')         # 15 글자 이하만
print("이름 : " , kim.getName())
print("나이 : " , kim.getAge())
print("전화번호 : " , kim.getTel())


lee = Person()
lee.setName("ㄱㄴㄷㄻㅄㅇㅈㅊㅋㅌㅍㅅㅎ")          # 10 글자 이내로 입력하세요
lee.setAge(170)                      # 1~ 150살 만 입력하세
lee.setTel('1111-2222-3333-4444')             # 15 글자 이하로 입력하세요

# 생성자 / 소멸자 #
# __ init__        객체 생성시 자동호출 , 객체 초기화 함수
# __ del__        객체 소멸시 자동호출. 객체 메모리 정리 함수

class User:
    __name = NONE
    __age = 0
    def __init__(self,name=None, age=0):
        print("생성자 실행중")
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def __del__(self) :
        print("소멸자")

kim = User()
print("이름 : " ,kim.getName())
print('나이 :' ,kim.getAge()) 
del kim

lee = User("이순신")
print("이름 : " ,lee.getName())
print('나이 :' ,lee.getAge()) 

hong = User("홍길동",30)
print("이름 : " ,hong.getName())
print('나이 :' ,hong.getAge()) 
       
## static ##
# Static 멤버
# 모든 객체가 공유
# 인터프리터 언어라서 명시할 필요가 없다. 사용할 때 static 으로 사용

# 멤버                  객체.멤버
# static 멤버        클래스명.멤버
print("="*30)
class Member:
    name = NONE
    age = 0
    def setName(self,name):
        self.name = name
    def setAge(self,age):
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def dispName(self):
        return "이름 : "+ Member.name
    def dispAge(self):
        return "나이: " + str(Member.age)
    
    
Member.name = "홍길동" # static 영역에 저장
Member.age = 30

kim = Member()
print("이름: ",kim.getName())
print("나이 : ",kim.getAge())

lee = Member()
print("이름 : ",lee.getName())
print("나이 : ",lee.getAge())

kang = Member()
kang.setName("강감찬")
kang.setAge(20)
print("이름 : ",kang.getName())   # 멤버 , stack 영역 변수
print("나이 : ",kang.getAge())
print(" 이름: ", kang.dispName()) # static 멤버, static 영역 변수
print("나이 : ", kang.dispAge()) # static 변수를 출력, 공유변수도 사용할 수 있다

print("="*50)
## 상속 ##
'''
class Animal :
    def __init__(self , name=""):
        self.name = name
    def getName(self):
        return self.name;
class Dog(Animal):
    NONE
class Cat (Animal):
    NONE
dog = Dog()
print("이름 :" , dog.getName())
dog = Dog("멍멍이")
'''
# 상속시 생성자 호출 순서
class Animal :
    def __init__(self , name=""):
        self.name = name
    def getName(self):
        return self.name;
class Dog(Animal):
    def __init__(self, name=""):
        Animal.__init__(self,name)              # super()         부모생성자 호출. 생략가능
        print("Dog 생성자")
class Cat (Animal):
    def __init__(self, name=""):
        Animal.__init__(self,name)
        print("Cat 생성자")
dog = Dog()
print("이름 :" , dog.getName())
dog = Dog("멍멍이")
print("이름 :",dog.getName())
cat = Cat("나비")
print("이름 :",cat.getName())

# 다중상속 #
# C             다중상속가능. 사용불가능
# Java         다중상속 불가능. 인터페이스는 다중상속 가능
# Python    다중상속 가능. 사용가능
print("="*50)
class Car :
    
    def __init__(self , name=""):
        self.name = name
    def getName(self):
        return self.name;
    
class Seat:                                                 # 인승 관리
    def __init__(self,num=0):
        self.num = num
    def getNum(self):
        return self.num
 
class Bus(Car, Seat):
    def __init__(self, name = "", num=0):
        Car.__init__(self, name)
        Seat.__init__(self,num)
    
class Truck(Car):
     def __init__(self, name = "", ton=0):
        Car.__init__(self, name)
        self.ton = ton
     def getTon(self):
        return self.ton
    
class Suv(Car, Seat):
    def __init__(self, name="",num=0):
        Car.__init__(self,name)
        Seat.__init__(self,num)
        
bus = Bus("대우", 45,)
truck = Truck("현대",10)
suv = Suv("벤츠",6)

print("이름 : ", bus.getName() )     # 이름 : 대우
print("인승 : ", bus.getNum() )        # 인원 : 45인승
print("이름 : ", truck.getName() )  # 이름 : 현대
print("크기 : ", truck.getTon() )     # 용량: 10t
print("이름 : ", suv.getName() )     # 이름 : 벤츠
print("인승 : ", suv.getNum() )        # 인원 : 6인승

# 오버라이드
print("="*50)
class Pet :
    def __init__(self, kind="", name="" ) :
        self.kind = kind
        self.name = name
    def getKind(self) :
        return self.kind
    def getName(self) :
        return self.name
class Puppy( Pet ) :
    def __init__(self, kind="", name="", age=0) :
        Pet.__init__(self, kind, name)
        self.age = age
    def getAge(self) :
        return self.age   
    def getName(self) :                     # 오버라이드(재정의)
        return "우리집 " + self.name 
class Guppy( Pet ) :
    def __init__(self, kind="", name="", color=""):             
        Pet.__init__(self, kind, name)
        self.color = color
    def getColor(self) :
        return self.color    

puppy = Puppy( "치와와", "멍멍이", 3 )     # new 생략가능
print( "품종 : ", puppy.getKind() );
print( "이름 : ", puppy.getName() );
print( "나이 : ", puppy.getAge() )
guppy = Guppy( "구피", "알풀", "빨간색" )
print( "품종 : ", guppy.getKind() );
print( "이름 : ", guppy.getName() );
print( "색상 : ", guppy.getColor() );

    
puppy = Puppy("치와와","멍멍이",3)
print("품종 : ",puppy.getKind())
print("이름 :",puppy.getName())
print("나이 : ",puppy.getAge())
guppy = Guppy("구피","알풀","발간색")
print("품종 : " ,guppy.getKind())
print("이름 : ",guppy.getName())
print("색상 : ",guppy.getColor())

print("="*50)
## 다형성 ##
# 상속과 오버라이드가 된 상태

class Bread :
    def __init__(self, name="" ) :
        self.name = name
    def getName(self) :
        return "Bread : " + self.name
    def getAddr(self) :
        return id(self)   
class Cake( Bread ) :
    def getName(self) :
        return "Cake : " + self.name       
class RedBean( Bread ) :
    def getName(self) :
        return "RedBean : " + self.name
class Toast( Bread ) :
    def getName(self) :
        return "Toast : " + self.name
# 들어가는 곳은 하난데 나오는 곳이 여러 개
# 부모의 멤버 호출 -> 자식들중의 멤버 중에 선택해서 실행
# Bread bread = Cake();          참조변수의 자료형이 없어서 성립이 안됨
bread = Cake("딸기")
print(bread.getName())    

print("="*50)
## 예외처리 ##
import traceback
try :
    #a = 4 / 0
    #a = 4 / "A"
    a = 4/2
except ZeroDivisionError:
    print("0 으로 나누지 마세요")
except TypeError:
    print("숫자로만 나누세요")
else: # 에러가 없을때
    print(a)
finally :
    print("프로그램 끝")
    
# 사용자 정의 예외
class InputError (Exception) :
    def __init__(self,length):
        self.length = length
        print(length , "4~8 사이오 입력하세요")
        
class NumberException(Exception):
    def __init__(self):
        print("문자를 섞어넣어 주세요")

print("비밀번호 : ",end="")
str = input()
try :
    if len(str) < 4 or len(str) > 8:
        raise InputError(len(str))
    if str.isdigit():
        raise NumberException()
except InputError:
    #traceback.print_exc()
    print("InputError 예외 발생")
except NumberException:
    print("NumberException 예외 발생")
    

