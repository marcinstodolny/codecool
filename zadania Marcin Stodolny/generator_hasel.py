import string
import random
all_characters = string.ascii_lowercase
lenght = ""
answer = ["Yes", "No"]
answer_d = ""
answer_u = ""
answer_c = ""
while answer_d not in answer:
    answer_d = input("Do you want digits in password?(Yes/No): ")
while answer_u not in answer:
    answer_u = input("Do you want upercase in password?(Yes/No): ")
while answer_c not in answer:
    answer_c = input("Do you want special charracters in password?(Yes/No): ")
if answer_c.lower() == "yes":
    all_characters += (string.punctuation)
if answer_u.lower() == "yes":
    all_characters += (string.ascii_uppercase)
if answer_d.lower() == "yes":
    all_characters += (string.digits)
while not lenght.isnumeric():
    lenght = input("how long?: ")
password = [random.choice(all_characters) for _ in range(int(lenght))]
print("".join(password))
