# Today in Class we are building the childhood game Rock Paper Scissors
# We are going to import the random function for our code today
# Bonus objective can you put it on a while loop to play again
# Do not just google the game and copy paste, If you would like to look at a completed version if you get stuck on a step please do so.
#Write your code below this line:


# import random

# def get_user_choice():
#     user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#     while user_choice not in ["rock", "paper", "scissors"]:
#         print("Invalid choice. Please choose Rock, Paper, or Scissors.")
#         user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
#     return user_choice

# def get_computer_choice():
#     return random.choice(["rock", "paper", "scissors"])

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def play_game():
#     while True:
#         user_choice = get_user_choice()
#         computer_choice = get_computer_choice()

#         print(f"You chose {user_choice}")
#         print(f"Computer chose {computer_choice}")

#         result = determine_winner(user_choice, computer_choice)
#         print(result)

#         play_again = input("Do you want to play again? (yes/no): ").lower()
#         if play_again != "yes":
#             print("Thanks for playing! Goodbye.")
#             break

# # Start the game
# play_game()

# import random

# while True:
#     options = ["Rock", "Paper", "Scissors"]
#     user_choice = input("Choose Rock, Paper, or Scissors: ")
#     computer_choice = random.choice(options)
#     print("You chose:", user_choice)
#     print("Computer chose:", computer_choice)
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "Rock" and computer_choice == "Scissors") or \
#          (user_choice == "Paper" and computer_choice == "Rock") or \
#          (user_choice == "Scissors" and computer_choice == "Paper"):
#         print("You win!")
#     else:
#         print("Computer wins!")
#     # While Loop
#     play_again = input("Do you want to play again? (y/n): ").lower()
#     if play_again != 'y':
#         print("Thanks for playing. Goodbye!")
#         break

import random

CHOICES = ["rock", "paper", "scissors"]

def get_user_choice():
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    while user_choice not in CHOICES:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(CHOICES)

def determine_winner(user_choice, computer_choice):
    outcomes = {("rock", "scissors"): "You win!", ("paper", "rock"): "You win!", ("scissors", "paper"): "You win!",
                ("scissors", "rock"): "You lose!", ("rock", "paper"): "You lose!", ("paper", "scissors"): "You lose!"}
    result = outcomes.get((user_choice, computer_choice), "It's a tie!")
    return result

def play_game():
    wins, losses = 0, 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}\nComputer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            wins += 1
        elif "lose" in result:
            losses += 1

        print(f"Wins: {wins}, Losses: {losses}")

        if input("Play again? (yes/no): ").lower() != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Start the game
play_game()