create database bank
use bank
create table dep(dep_id int identity(1,1) primary key,name varchar(60),department varchar(125),joining date)
insert into dep(name,department,joining)
values('has','acct','2040-3-22')
create table emp(id int identity(1,1) primary key,name varchar(150),age int,number int,dep_id int)
insert into emp(name,age,number,dep_id)
values('all',33,89023,4);
drop table dep
update dep set dep_id=1 where dep_id=2 
select * from emp as a
inner join dep as b
on a.dep_id=b.dep_id
select * from emp as a
outer join dep as b
on a.dep_id=b.dep_id
select * from emp
select * from dep
select * from emp as a
left join dep as b
on a.dep_id=b.dep_id
select * from emp as a
right join dep as b
on a.dep_id=b.dep_id
select * from emp as a
inner join emp as b
on a.dep_id=b.dep_id