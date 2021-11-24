## 정규 표현식 ## Regular Expersssion ##
import re
p = re.compile("[a-z]+")        # 소문자. 글자수는 상관 없다.

#match
print(p.match("abc"))           # abc
print(p.match("pyTHon"))    # py
print(p.match("ABC"))         # None
print(p.match("Python"))    # None

#search
print(p.search("abc"))           # abc
print(p.search("pyTHon"))    # py
print(p.search("ABC"))         # None
print(p.search("Python"))    # ython
print(p.search(" ")) # None
print(p.search(" abc ")) #abc
print(p.search("abc  ")) #abc

# group()         매치된 문자열을 리턴한다
# start()             매치된 문자열의 시작 위치를 리턴한다.
# end()              매치된 문자열의 끝 위치를 리턴한다.
# span()              매치된 문자열의 (시작,끝 ) 에 해당하는 튜플을 리턴한다.
print("="*50)
result = p.search("Python!!!")
print(result)
print(result.group())
print(result.start())
print(result.end())
print(result.span())

#findall()
print("="*50)
msg = "Life is too short!!!"
print(p.findall(msg))           #list    
print(p.finditer(msg))          #iterater 객체

for m in p.findall(msg) :
    print(m)
for i in p.finditer(msg) :
    print(i.group())

# Dot             DOTALL /S
print("="*50)
p = re.compile("a.b")
print(p.search("abc")) # None
print(p.search("acb")) # acb
print(p.search("aacb")) # acb
print(p.search("accb")) # None ... 한글자만 들어가야하는데 두글자가 들어가서 none
print(p.search("a1b")) # a1b

msg = """
abc acb abbb a 
ab  a.b a2b 
"""
print(p.findall(msg))               # ['acb','abb','a.b','a2b']     \n 때문에 두번째줄은 안찾는데,,,버전바뀜?
p = re.compile("a.b",re.DOTALL)
print(p.findall(msg))                # ['acb','abb','a.b','a2b']
p = re.compile("a.b",re.S)
print(p.findall(msg))                # ['acb','abb','a.b','a2b']

# IGNORECASE / I 대소문자 무시
# p = re.compile('[a-zA-Z]')
p = re.compile('[a-z],re.I')
print(p.match("python"))    
print(p.match("ABC"))
print(p.match(" abc"))
print(p.match(" Abc"))

# MULTILINE / M  ... 라인 하나하나를 다른 데이터로 취급
# ^ 처음 $ 마지막
p = re.compile("^python\s\w+",re.M) # python으로 시작. 여백이 한자리. 숫자나 문자가 1~무한대
data = """python one 
python  two
Python three
you need python
python
one python
1python
python1
python\none
"""
print(p.findall(data))

p = re.compile("\section")              # \s 는 화이트 스페이스
print(p.match(" ection"))           # ection 만 잡는다 ... s 까지 데이터 취급하려면?

p = re.compile("\\\\section")       # \를 데이터로 취급하려면 3~4개 써야함.
print(p.match("\section"))

print("="*50)
emails = """
aaa@aaa.com
aaa@a.com
AAA@AAA.com
1aa@1aa.com
&&&@&&&.com
@aaa.com
aaa@aaa@com
aaa@@aaa.com
aaaaaaaaaaaaaaaaaa@a.com
aa1@aaa.com
aaa@aaa.7com
aaa@aaa.co.kr
"""

p = re.compile( "^[a-z][a-z0-9]{2,15}@[a-z0-9]{2,}\.[a-z]{2,}$", re.M )
print( p.findall( emails ) )
p = re.compile( "^[a-z0-9]{2,15}@[a-z0-9]{2,}\.[a-z]{2,}\.[a-z]{2,}$", re.M )
print( p.findall( emails ) )


