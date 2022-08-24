import random
answer = ["rock", "paper", "scisors"]
computer_answer = random.choice(answer)
user_answer = ""
print(computer_answer)
while user_answer not in answer:
    user_answer = input("rock, paper or scisors?: ")
if computer_answer == user_answer:
    print("You both chose same thing")
elif computer_answer == "rock" and user_answer == "paper" or computer_answer == "paper" and user_answer == "scisors" or computer_answer == "scisors" and user_answer == "rock":
    print("User won")
else:
    print("computer won")
