##loops
#even and odd using for loop
for i in range(1,20):
    if i%2==0:
        print("even",i)
    elif i%2!=0:
        print("odd",i)
#sum of number 1 to 10
o=0
for i in range(1,10):
    print(i)
    o+=i
print(o)
#print the table pf multiplication
h=int(input("Enter a number to print a table of"))
for i in  range(1,11):
    print(f"{h} x {i}={h*i}")
# print the square number 
for i in range(1,10):
    print(i*i)
count=0

# voel in a sentence
vowels=input("Enter your name").lower()

for i in vowels:
    if i=="a"or i=="e" or i=="i" or  i=="o"  or i=="u":
        count+=1
        print(i)
print(count)

#print reverse of a string
word=input("Enter your word:  ")
reverse=""
for i in word:
    print(i)
    reverse=i+reverse
print(reverse)
 #check fi a number is prime
num=int(input("ENter a number"))
if num<2:
     print("not prime")
else:
    for i in range(2,num):
      if num%i==0:
       print("not prime")
       break
    else:
        print("prime")

 