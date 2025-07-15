# Rent calculator in python 
#input from user 
#total rent,food
#ectricity total unit spent 
#charge per unit
#person living in
rent=int(input("Enter your total rent: "))
food=int(input("Enter the total food cost: "))
electricity=int(input("enter the total electricity used: "))
electricity_per_unit=int(input("enter the electricity per unit price: "))
people=int(input("Total person living and shareing expense: "))
total=electricity*electricity_per_unit
final=(total+rent+food)//people
print(final)