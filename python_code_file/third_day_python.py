##function 
#recursion
def show(n):
    if n==1000:
        return
    print(n)
    show(n+1)
show(5)
#list comprhension
##if even then append or add number in the list
g=[i for i in range(10) if i%2==0]
print(g)
h=[]
for i in range(10):
   
     h.append(i)
#find the missing value in the list from one to 10
sum=0
w=0
lis=[1,3,4,5,6,7,8,9,10]
for i in lis:
    sum+=i
print(sum) 

for h in range(1,11):
    w+=h
print(w)
print(w-sum)

## oop classe
#student subjetc score sum
class student:
    def __init__(self,names,marks):
        self.name=names
        self.mark=marks 
    
    def welcome(self):
        print("Welcome to our school: ",self.name)
a=input("Enter your name")
b=int(input("ENter your score"))
s=student(a,b)
s.welcome()
print(s.mark,s.name)
class student:
    def __init__(self,name,s1,s2,s3):
        self.name=name
        
        self.sub=s1
        self.sub2=s2
        self.sub3=s3
    
    def avg(self):
        sum=self.sub +self.sub2+self.sub3
        print(sum)
        
nam=input("Enter name")
ma=int(input("Enter first sub score"))
a=int(input("Enter second sub score"))
am=int(input("Enter third sub score"))
s=student(nam,ma,a,am)
s.avg()
# fibonaci
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def autosum(self):
        total = sum(self.marks)
        print(total / len(self.marks))
        
    def fibo(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibo(n - 1) + self.fibo(n - 2)


s = Student("n", [1, 2, 3])
s.autosum()             
print(s.fibo(6))    
##  banking example 
class Account:
    balance=0
    account_num=0
    
    
    def debit(self,b):
        print("Welcome to the bank app")
        a=input("Enter your account number")
        print(f"your balance aganist your {a}account number is ",b)
import random
s=Account()
r=random.randrange(0,1000000)
s.debit(r)
# Ask the user to enter a number (e.g., 458926) and count how many digits in it are even (0, 2, 4, 6, 8).
o=0
num=int(input("Enter some numbers"))
for i in range(num):
    if i%2==0:
        o=o+1
        print(i)
print(o)
o=0
num=[1,2,3,4,5,7,9,9]
for i in num:
    if i%2==0:
        o=o+1
        print(i)
print(o)
## You are given a list of numbers (e.g., [123, 45, 6, 7890]).
# Count the total number of digits across all numbers.
num=[12,3,456,78,9,10]
count=0
for i in num:
    count+=len(str(i))
print(count)
# Ask the user to enter a number (e.g., 95861).
# Your task is to find the largest digit in that number.
user=input("Enter some numbers")
max=0
for i in user:
    temp=int(i)
    if temp >max:
        max=temp
print(max)    
## fake headline generator
import random

Subject=[
    "Amir Khan",
    "Salman Khan",
    "Sharukh Khan",
    "Azad chaye wala",
    "Ptcl company",
    "cocola comapny"   
]
action=[
    " dances ",
    " car accident ",
    " launched a rocket ",
    " gave a kid a cat ",
    " ate many mangoes and died ",
    " lost the most expensive watch "
]
placeofthings=[
    " In lahore ",
    " in a park ",
    " went to a zoo ",
    " at his own house ",
    " on london brigde ",
    " near a well which hold a news station "
]
letsgo=True
while letsgo==True:
    sub=random.choice(Subject)
    act=random.choice(action)
    place=random.choice(placeofthings)
    headline=f"Breakin news: {sub}{act}{place}"
    print(headline)
    i=input("if you want to genrate another headline Press (Yes/No)").strip().lower()
    i.lower()
    if i=='yes':
        letsgo=True
    elif i=="no":
        letsgo=False
    else:
        letsgo=False
        print("You choose somthing else")
