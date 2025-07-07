#Write a Program to input 2 numbers & print their sum.
a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a+b)

#WAP to input 2 floating point numbers & print their average.
c=float(input("Enter first number"))
d=float(input("Enter second number"))
t=c+d/2
print(t)

# Take principal, rate, and time from the user and calculate simple interest (SI = P × R × T / 100).
prin=int(input("ENter principal vlaue: "))
rate=int(input("Enter rate value: "))
time=int(input("Enter the time: "))
total=prin*rate*time/100
print(total)

# Temperature Converter
# Convert a temperature from Celsius to Fahrenheit.(32°F − 32) × 5/9 = 0°C
temp=int(input("Enter your temperature"))
conveter= temp*(5/9)+32
print(conveter)





## string(concatenation,indexing,slicing,len) and Conditional statement(if,elif,else)

#Wapto input user’s first name & print its length.
name=input("Enter your name")
print(f"the lenght of your name: {name}",len(name))
#find the occurrence of ‘$’ in a String.
sting="$hello $ there haha $"
print(sting.count("$"))
#wap check if a number entered by the user is odd or even.\
num=int(input("ENter a number"))
if num%2==0:
    print("even")
else:
    print("odd")
#wap to find the greatest of 3 numbers entered by the user.
num1=int(input("ENter first number"))
num2=int(input("ENter second number"))
num3=int(input("ENter thid number"))
if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")
# Write a Python program that asks the user to enter a number.
# Then check and print:
# If the number is even and divisible by 5, print "Even and divisible by 5"
# If it’s just even, print "Even but not divisible by 5"
# If it’s odd, print "Odd"
a=int(input("Write a number:"))
print(a)
if a%2==0:
    if a%5==0:
        print("Even and divisible by 5")
    else:
      print("Even but not divisible by 5")
else:
    print("Odd")
    
    
    
# ##List/string/tuple/
#WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
user1=input("Enter your first fav movie name")

user2=input("Enter your first fav movie name")
user3=input("Enter your first fav movie name")
lis=[]
lis.insert(0,user1)
lis.insert(1,user2)
lis.insert(2,user3)
print(lis)
#WAP to count the number of students with the “A” grade in the following tuple.
# [”C”“D”“A”A”“B”b,a,a,a]
students=("C","D","A","A","B","B")
print(students.count("A"))

