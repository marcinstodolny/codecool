import string
import random
all_characters = string.ascii_lowercase
answer = ["yes", "no"]

answer_digits = input("Do you want digits in password?(Yes/No): ").lower()
while answer_digits not in answer:
    answer_digits = input("You entered wrong value, try again\nDo you want digits in password?(Yes/No): ").lower()
    
answer_uppercase = input("Do you want upercase in password?(Yes/No): ").lower()    
while answer_uppercase not in answer:
    answer_uppercase = input("You entered wrong value, try again\nDo you want upercase in password?(Yes/No): ").lower()
    
answer_special = input("Do you want special charracters in password?(Yes/No): ").lower()
while answer_special not in answer:
    answer_special = input("You entered wrong value, try again\nDo you want special charracters in password?(Yes/No): ").lower()
    
if answer_special == "yes":
    all_characters += (string.punctuation)
if answer_uppercase == "yes":
    all_characters += (string.ascii_uppercase)
if answer_digits == "yes":
    all_characters += (string.digits)
lenght = input("how long?: ")
while not lenght.isnumeric():
    lenght = input("You entered wrong value, try again\nhow long?: ")
password = [random.choice(all_characters) for _ in range(int(lenght))]
print("Your password: " + "".join(password))
