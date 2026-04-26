import random

def stone_paper_scissors():
    options = ["stone", "paper", "scissors"]

    user_choice = input("Enter stone, paper or scissors: ").lower()
    computer_choice = random.choice(options)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice not in options:
        print("Invalid choice.")
    elif user_choice == computer_choice:
        print("Result: Match Draw")
    elif (
        user_choice == "stone" and computer_choice == "scissors"
        or user_choice == "paper" and computer_choice == "stone"
        or user_choice == "scissors" and computer_choice == "paper"
    ):
        print("Result: You Win!")
    else:
        print("Result: Computer Wins!")

def dice_roll_game():
    user_number = int(input("Guess a number between 1 and 6: "))
    dice_number = random.randint(1, 6)

    print(f"Dice rolled: {dice_number}")

    if user_number < 1 or user_number > 6:
        print("Invalid number.")
    elif user_number == dice_number:
        print("Result: You Win!")
    else:
        print("Result: You Lose!")