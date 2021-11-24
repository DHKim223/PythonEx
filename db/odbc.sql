select * from tabs;

drop table dbtest;
drop table GAME;
drop table GAME2;

create table dbtest(
id varchar2(20) primary key,
passwd varchar2(20) not null,
name varchar2(20) not null,
tel varchar2(15),
logtime date default sysdate
);

select * from dbtest;

insert into dbtest values('aaa','111','홍길동','1111-2222',sysdate);
insert into dbtest values('bbb','222','이순신','2222-2222',sysdate);
insert into dbtest values('ccc','333','김유신','1111-3333',sysdate);
insert into dbtest values('ddd','444','강감찬','3333-2222',sysdate);
insert into dbtest values('eee','111','대조영','2222-3333',sysdate);
 commit;
 
 