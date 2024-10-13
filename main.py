import random

item_list=["rock","paper","scissor"]


user_choice=input("Enter your choice(rock,paper,scissor) :")
comp_choice=random.choice(item_list)

print(f"Your choice is {user_choice} and computer's choice is {comp_choice}")

if user_choice==comp_choice:
    print("Both choosed same => Match tie!!!")
elif user_choice=="rock":
    if comp_choice=="paper":
        print("paper covers rock => computer win")
    else:
        print("rock smashes scissor => You win")
elif user_choice=="paper":
    if comp_choice=="rock":
        print("paper covers rock => you win")
    else:
        print("scissor cuts paper => computer win")
elif user_choice=="scissor":
    if comp_choice=="rock":
        print("rock smashes scissor => computer win")
    else:
        print("scissor cuts paper => you win")