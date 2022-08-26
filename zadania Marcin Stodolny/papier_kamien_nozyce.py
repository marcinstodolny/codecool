import random

answer = ["rock", "paper", "scissors"]
computer_answer = random.choice(answer)
user_answer = input("rock, paper or scissors?: ").lower()
while user_answer not in answer:
    print("You entered wrong value, try again")
    user_answer = input("rock, paper or scissors?: ").lower()
if computer_answer == user_answer:
    print("You both chose same thing - it's a draw")
elif computer_answer == "rock" and user_answer == "paper" or computer_answer == "paper" and user_answer == "scissors" or computer_answer == "scissors" and user_answer == "rock":
    print("User won")
else:
    print("computer won")
