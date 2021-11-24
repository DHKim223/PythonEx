# 간단한 스크래핑
import urllib.request as req
from bs4 import BeautifulSoup as bs
# url = "https://finance.naver.com/marketindex/exchangeList.nhn"
# data = req.urlopen( url ).read().decode("euc-kr")
# # req.urlretrieve( url, "exchage.txt" )
# soup = bs( data, "html.parser" )
#
# title = soup.find("caption")
# print( "<<", title.string, ">>" )
# changes = soup.select( "td.tit a" )
# prices = soup.select( "td.sale" )
# buy = soup.select("td")
# sell = soup.select("td")
#
# for i in range( 0, len(changes) ) :
#     print( changes[i].string.strip(), end=" " )
#     print( prices[i].string.strip(), end=" " )
#     print( prices[i].next_sibling.next_sibling.string, end=" ")
#     print( prices[i].next_sibling.next_sibling.next_sibling.next_sibling.string)
#
#     for child in prices[i].parent.children:
#         print(child.string.strip(), end = " ")
#     print()
#

# 주요기사 제목 / 내용
# import time
# url = "https://news.naver.com"
# data = req.urlopen(url).read().decode("euc-kr")
# req.urlretrieve(url,"news.txt")
# soup = bs(data, "html.parser")
# hdnews = soup.select("div.hdline_article_tit a")
# for hd in hdnews :
#     print("제목 : " + hd.string.strip())
#     article_url = url + hd.attrs["href"]
#     article = req.urlopen(article_url).read().decode("euc-kr")
#     article_soup = bs(article, "html.parser")
#     article_content = article_soup.select_one("div._article_body_contents");
#     # print(article_content.contents)
#     msg = ""
#     for content in article_content.contents : 
#         strdata = str(content).strip()
#         if strdata == "" : 
#             continue
#         if strdata not in [ "\n", "[[", "]]",  "<div" , "<" , ">" , "//" , "/", "<br>"] :
#             msg  += strdata
#     print(msg)
#     time.sleep(3)

# 페이지 로그인
# 한빛미디어 마일리지 확인
# import requests
# session = requests.session()
# info = {
#     "m_id" : "filmal",
#     "m_passwd" : "aaaa1111",
#     }
# url = "https://www.hanbit.co.kr/member/login_proc.php"
# try : 
#     resp = session.post(url, info)
#     resp.raise_for_status()
# except Exception as e : 
#     print(e)
# else : 
#     print("로그인 성공")
#
# mypage = "https://www.hanbit.co.kr/myhanbit/myhanbit.html"
# myresp = session.get(mypage)
# myresp.raise_for_status()
#
# soup = bs( myresp.text, "html.parser")
# title1 = soup.select_one(".mileage_section1 dt")
# mileage = soup.select_one(".mileage_section1 span")
# print(title1.string + " : " + mileage.string)
#
# title2 = soup.select_one(".mileage_section2 dt")
# ecoin = soup.select_one(".mileage_section2 span")
# print(title2.string + " : " + ecoin.string)

# requests
# import requests as req
#resp = req.get("http://www.google.com/robots.txt")
#print(resp.text)        # 텍스트 형태
#print(resp.content)     # 바이너리 형식
#
# resp = req.get("")
# with open("sunset.jpg","wb") as f:
#     f.write(resp.content)
# print("저장성공!")

#selenium                     임시 브라우저
# from selenium import webdriver
# import time
# url = "http://www.naver.com"
# chromedriver = "C:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# browser = webdriver.Chrome(chromedriver)
# browser.implicitly_wait(5)
# browser.get(url)
# time.sleep(5)
# browser.save_screenshot("naver.png")
# browser.quit()

# 구글 로그인
# import time
# url = "https://accounts.google.com/signin/v2/indentifier"
# chromedriver = "C:\Python\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
# browser = webdriver.Chrome(chromedriver)
# browser.implicitly_wait(3)
# browser.get(url)
# browser.find_element_by_id("identifierId").send_keys("instructor.set")
# time.sleep(2)
# browser.find_element_by_id("identifierNext").click()

# browser.find_element_by_id("passwd").send_keys("11111111")
# time.sleep(2)
# browser.find_element_by_id("passwdNext").click()
# 로그인상태

# 공공데이터 포털
# 아파트 실거리가 정보
# import urllib.parse as pa
# url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=11680&DEAL_YMD=202108&serviceKey=OUwSlot%2BeCADq1M9zzdj8Sh1Ni9C4Iiaj9VqSEnyvikodjynkoS1hrbUsP6mSENccvTJH%2FDe3s3y7i836Lk7ew%3D%3D"
# #url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=11680&DEAL_YMD=202108&serviceKey=SSNyuBtI0OklWp98k4%2F9FCsrKhoXcZ5Pa9JVgFZftWPHoYvxOqyq%2BPzBra2SdQ0LnO4YhJbgDcTqOzJnjjJLXg%3D%3D"
# resp = req.urlopen(url).read().decode("utf-8")
#
# resp = resp.replace("거래금액","price")
# resp = resp.replace("월","month")
# resp = resp.replace("일","day")
# resp = resp.replace("아파트","apart")
#
# with open("price.xml","wt",encoding="utf-8") as f:
#     f.write(resp)
# print("저장했습니다")
#
# soup = bs(resp,"html.parser")
# items = soup.find_all("item")
# for item in items :
#     print(item.apart.string, item.price.string, item.month.string, item.day.string)
