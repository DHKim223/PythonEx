# ODBC
# pip install cx_Oracle

# select
import cx_Oracle
dsn = cx_Oracle.makedsn( "localhost", "1521", "xe" )
con = cx_Oracle.connect( "joeun", "joeun", dsn )
print( "DB 연결성공" )
cursor = con.cursor()

sql = "select * from dbtest"
cursor.execute( sql )
# for row in cursor :
#     for column in row :
#         print( column, end="\t" )
#     print()
    
rows = cursor.fetchall()            # 데이터 전체를 저장
for row in rows :
    for column in row :
        print( column, end="\t")
    print()
    
sql = "select count(*) from dbtest"
cursor.execute( sql )
count = cursor.fetchone()[0]        # 데이터 하나 저장
print( "회원수 : " + str(count) )    

sql = "select * from dbtest where id='aaa'"
cursor.execute( sql )
row = cursor.fetchone()             # 한 행을 저장
print( row )                            # 튜플
con.close();

# insert
dsn = cx_Oracle.makedsn( "localhost", "1521", "xe" )
con = cx_Oracle.connect( "joeun", "joeun", dsn )
cursor = con.cursor()
sql = "insert into dbtest(id, passwd, name, tel)  values( :1, :2, :3, :4 )"
# user = ( 'fff', '111', '홍길동', '2222-1111' )
# cursor.execute( sql, user )

# users =[( 'ggg', '111', '홍길동', '2222-1111' ),
#         ( 'hhh', '111', '이순신', '2222-1111' ),
#         ( 'iii', '111', '김유신', '2222-1111' )]
# for user in users :
#     cursor.execute( sql, user )
# print( "가입성공" )
# con.commit()                            

sql = "select * from dbtest"
cursor.execute( sql )
for row in cursor :
    for column in row :
        print( column, end="\t" )
    print()

con.close()    

# delete
dsn = cx_Oracle.makedsn( "localhost", "1521", "xe" )
con = cx_Oracle.connect( "joeun", "joeun", dsn )
cursor = con.cursor()
id = "aaa"
passwd = "111"
sql = "select * from dbtest where id='"+id+"'"
cursor.execute( sql )
user = cursor.fetchone();
if user == None :
    print( "입력하신 아이디가 없습니다." )
else :
    if passwd == user[1] :
        sql = "delete from dbtest where id=:idx"
        cursor.execute( sql, idx=id )
        con.commit()        
        print( "탈퇴성공" )
    else :
        print( "입력하신 비밀번호가 다릅니다." )
con.close()



    