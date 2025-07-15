/*
Section A – Core SQL CRUD & Filtering
Bulk Insert
Add five new rows into students with unique id values, ages ranging from 18 to 28, and names that all start with the letter “A.”

Conditional Update
Increase the age of every student whose current age is less than 20 by 2 years.

Safe Delete
Remove only those students whose age is greater than 60—but do it inside a transaction so you can roll back if the row count exceeds 2.


*/
select * from student_data where age>20
update student_data set age=80 where id=5 
create database uni
use uni
create table student_data(id int primary key,
st_name varchar(90),
age tinyint,
fee int
)
insert into student_data(id,st_name,age,fee)
values(1,'Aibo',18,500)
insert into student_data(id,st_name,age,fee)
values(2,'anibo',20,1500)
insert into student_data(id,st_name,age,fee)
values(3,'amibo',22,2200)
insert into student_data(id,st_name,age,fee)
values(4,'alibo',25,7400)
insert into student_data(id,st_name,age,fee)
values(10,'ahibo',129,2300)
insert into student_data(id,st_name,age,fee)
values(9,'apibo',61,58900)
insert into student_data(id,st_name,age,fee)
values(8,'ajibo',50,9000)
select * from student_data
begin transaction
delete from student_data where age>60;
rollback
commit
if @@ROWCOUNT<=2
commit;
else 
rollback;
CREATE PROCEDURE rec
AS
BEGIN
    BEGIN TRANSACTION;

    DELETE FROM student_data WHERE age > 60;

    IF @@ROWCOUNT <= 2
    BEGIN
        COMMIT;
    END
    ELSE
    BEGIN
        ROLLBACK;
    END
END
GO
exec rec
/*
Section B – Aggregations & Grouping
Average Age by First Letter
Show each first letter of name along with the average age for students whose names start with that letter.
Hint: use SUBSTRING(name,1,1).
Top‑N Query
List the three youngest students (all columns) using exactly one ORDER BY and LIMIT/TOP style clause (pick the syntax your SQL flavor supports).
HAVING Clause Challenge
Find every age value that appears at least twice in the table and list that age plus its count.
*/
