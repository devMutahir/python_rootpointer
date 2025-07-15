import random

store = ["rock", "paper", "scissor"]
print("Choices:", store)

user = input("Pick your weapon: ").lower()
computer = random.choice(store)

print("Computer choice:", computer)

if user == computer:
    print("It's a draw!")
elif (user == "rock" and computer == "scissor") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissor" and computer == "paper"):
    print("You win!")
elif user in store:
    print("Computer wins!")
else:
    print("Invalid input.")
