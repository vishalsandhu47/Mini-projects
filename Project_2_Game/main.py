from services.game_service import stone_paper_scissors, dice_roll_game

while True:
    print("\n========== GAME MENU ==========")
    print("1. Stone Paper Scissors")
    print("2. Dice Roll Game")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        stone_paper_scissors()
    elif choice == "2":
        dice_roll_game()
    elif choice == "3":
        print("Thanks for playing.")
        break
    else:
        print("Invalid choice. Please try again.")