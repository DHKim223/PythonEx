# 네트워크
import urllib.request
# # f=urllib.request.urlopen("https://www.daum.net")
# # print( f.read(300).decode("utf-8"))
#
# req = urllib.request.Request("http://www.dau1m.net")     
# try :               #  url 잘못넣는 경우 예외처리,,, 위에있는걸 나눈것.
#     urllib.request.urlopen(req)
# except urllib.error.URLError as e:
#     #print(e.reason)
#     print("URL 을 확인하세요")

# header
# resp = urllib.request.urlopen("http://www.daum.net")
#
# print(resp.geturl())
# #print(resp.info())
# #print(resp.info()["date"])
# print(len(resp.read()))
# print(resp.read().decode("utf-8"))

# 이미지 저장
# url = "https://image.fmkorea.com/files/attach/new2/20210810/3655304/1933684287/3821931628/67a9850e94761e48296ea1c1144ff025.jpg"
# saveimg="mypic.jpg"
# urllib.request.urlretrieve(url,saveimg)
# print("저장했습니다.")

# 텍스트 저장
# url = "http://www.google.com/robots.txt"
# resp = urllib.request.urlopen(url)
# data = resp.read()
# data = data.decode("utf-8");
# #print(data)
#
# with open("robots.txt","w") as f:
#     f.write(data)
# print("저장했습니다.")

# url = "http://www.daum.net"
# resp = urllib.request.urlopen(url)
# data = resp.read(100000).decode("utf-8")
# with open("daum.txt","w") as f:
#     f.write(data)
# print("저장했습니다.")

# RSS
# 기상청 중기 예보 - 109 서울 경기
# https://www.weather.go.kr/weather/lifenindustry/sevice_rss.jsp
# url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# resp = urllib.request.urlopen( url )
# data = resp.read().decode( "utf-8" )
# # print( data )
# id = {
#     "stdId" : "109"
#     }
# import urllib.parse
# param = urllib.parse.urlencode( id )
# url = url + "?" + param
# resp = urllib.request.urlopen( url )
# data = resp.read().decode( "utf-8" )
# print( data )

# BeautifulSoup
# pip install beautifulsoup
from bs4 import BeautifulSoup as bs
html = """
    <html>
        <head>
            <title> Web Scraping </title>
        </head>
        <body>
            <h2> 웹 스크랩핑 </h2>
            <p class="point"> Hadoop </p>
            <p id="subject"><a> Spark </a></p>
            <p class="point"><b><a> Python </a></b></p>
            <p> TensorFlow </p>
        </body>
    </html>
"""

# data = bs( html, "html.parser" )
# print( "제목 : " + data.html.body.h2.string )
# print( "과목 : " + data.html.body.p.string, \
#        data.html.body.p.next_sibling.next_sibling.next_sibling.next_sibling.string )
# # find find_all
# print( "제목 : " + data.find("h2").string )
# print( "과목 : " + data.find("h2").next_sibling.next_sibling.string )
# # for c in data.body.children :
# #     print( c )
# print( "title : " + data.find("title").string )
# print( "p : " + data.find("p").string )
# print( "p : " + data.find("a").string )
# print("p : " + data.find(class_="point").string)
# print("p : " + data.find(id="subject").string)
#
# #find_all
# for p in data.find_all("p"):                    # getElementsByTagName
#     print("과목 : " + p.string)
# for p in data.find_all(class_= "point") :
#     print("과목 : " + p.string)
#
# # select_one
# print("과목 : " +  data.select_one("#subject").string)
# print("과목 : " +  data.select_one(".point").string)
# print("과목 : " +  data.select_one("h2").string)
#
# # select
# for p in data.select("p") : 
#     print("과목  : " + p.string )
# for p in data.select("p a"):                    # 후손선택자
#     print("과목  : " + p.string)
# for p in data.select("p>a"):                    # 자식선택자
#     print("과목  : " + p.string)
# for p in data.select("p#subject") :
#     print("과목 : " + p.string)
#
#
# print(data.select("p>a"))
#

# 기상청 중기 예보 - XLM / BeautifulSoup 으로 처리
from bs4 import BeautifulSoup as bs
import urllib.parse as pa
import urllib.request as req
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

id = {
    "stnId" : "109"
    }

param = pa.urlencode(id)
url = url + "?" + param
resp = req.urlopen(url)
xmldata = resp.read().decode("utf-8")
#print( xmldata )
soup = bs( xmldata, "html.parser" )
# print( soup )
title = soup.find("title").string
print( title )
locations = soup.find_all("location")
for location in locations :
    print( "<<", location.city.string, ">>" )
   
    tmef = location.find_all("tmef")
    wf = location.find_all("wf")
    tmn = location.find_all( "tmn" )
    tmx = location.find_all( "tmx" )
    for i in range( 0, len(tmef) ) :
        print( tmef[i].string, wf[i].string, tmn[i].string, tmx[i].string )
    print()    



