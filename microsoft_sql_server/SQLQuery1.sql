Create database college;
use college;
create Table students(id int primary Key ,
name varchar(50),
age tinyint,
subjects varchar(50) ); 
insert into students(id,name,age,subjects)
values(2,'mello',30,'sub1')
select * from students;
insert into students(id,name,age,subjects)
values(5,'mw',10,'jam')
select id,subjects from students;
select distinct age from students;
select *
from students
where age=20;
select *
from students
where name='jello'
select * from students where age>=20;
select *from students order by age;
select * from students order by id desc
select * from students order by age,id desc
select * from students where age=20 and name='mw'
select * from students where age=50 or name='jellou'
select * from students where not age=20 
select * from students where name in('mw') and age=20
select * from students where name not in('mw') 
select * from students where age between 20 and 30
select * from students where age not between 20 and 30
select * from students where name like 'm%'
select * from students where name like '__l%'
select Max(age) from students
select Max(age) as age from students 
select Min(age) as salary from students
select sum(age)as total from students
select sum(age)as total from students where age>10
select avg(age) as avgerage from students where age>10
select count(age) as name from students where age>10
select count(*) as name from students 
use college
create table studs(id int not null unique,name varchar(90) not null,age int null,fee int not null check(fee<8000),student_id int not null);
select * from studs
drop table studs
insert into studs(id,name,age,fee,student_id)
values(6,'hejpo',30,0110,1);
insert into studs(id,name,age,fee,student_id)
values(2,'hepo',null,500,4);
select * from stud order by fee asc
alter table stud drop column age
alter table stud add age int
update stud set fee=5000 where id=3
update stud set age=20 where id=1
create procedure record
as 
select * from students
go;
exec rec;
exec record;
select * into nybackup from stud;
select * from nybackup
select name,age into mybackup from students
select * from mybackup where age>=20
create index ag on students(age)
select * from students
select top 2 * from students
select top 75 percent * from  students
select top 45 percent * from students where age>=20
backup database college to disk ='D:\database\mybackup.bak';
create view w as
select age from stud
where age=30
select *from w
select * from students as a
inner join studs as b
on a.id=b.student_id;
