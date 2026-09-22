import random
item_list = ["rock", "paper", "scissor"]

user_choice = input("Enter your move = rock, paper, scissor: ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same = MATCH TIE")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers Rock = COMPUTER WIN")
    else:
        print("Rock smashes scissor = YOU WIN")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Scissor cuts Paper = COMPUTER WIN")
    else:
        print("Paper covers Rock = YOU WIN")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("Scissor cuts Paper = YOU WIN")
    else:
        print("Rock smashes Scissor = COMPUTER WIN")