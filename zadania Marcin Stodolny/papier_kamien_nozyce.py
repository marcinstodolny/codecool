import random
answer = ["rock", "paper", "scissors"]
computer_answer = random.choice(answer)
user_answer = ""
while user_answer not in answer:
    user_answer = input("rock, paper or scissors?: ")
if computer_answer == user_answer:
    print("You both chose same thing")
elif computer_answer == "rock" and user_answer == "paper" or computer_answer == "paper" and user_answer == "scissors" or computer_answer == "scissors" and user_answer == "rock":
    print("User won")
else:
    print("computer won")
