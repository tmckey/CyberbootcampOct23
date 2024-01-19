# # Your challenge tonight is to write a basic adventure game using some of the  
# #code provide below and using if/elif statments

# yes_no = ["yes", "no"]
# directions = ["left", "right", "forward", "backward"]
 
# # Introduction
# name = input("What is your name, adventurer?\n")
# print("Greetings, " + name + ". Let us go on a quest!")
# print("You find yourself on the edge of a dark forest.")
# print("Can you find your way through?\n")
 
# # Start of game
# response = ""
# while response not in yes_no:
#     response = input("Would you like to step into the forest?\nyes/no\n")
#     if response == "yes":
#         print("You head into the forest. You hear crows cawwing in the distance.\n")
#     elif response == "no":
#         print("You are not ready for this quest. Goodbye, " + name + ".")
#         quit()
#     else: 
#         print("I didn't understand that.\n")
 
# # Next part of game
# response = ""

# # Use if else statment from here to take you on a journey and have fun with it

# import random

# yes_no = ["yes", "no"]
# directions = ["left", "right", "forward", "backward"]

# # Introduction
# name = input("What is your name, adventurer?\n")
# print("Greetings, " + name + ". Let us go on a quest!")
# print("You find yourself on the edge of a dark forest.")
# print("Can you find your way through?\n")

# # Start of game
# response = ""
# while response not in yes_no:
#     response = input("Would you like to step into the forest?\nyes/no\n")
#     if response == "yes":
#         print("You head into the forest. You hear crows cawing in the distance.\n")
#     elif response == "no":
#         print("You are not ready for this quest. Goodbye, " + name + ".")
#         quit()
#     else:
#         print("I didn't understand that.\n")

# # Next part of the game
# while True:
#     print("To your left, you see a witch.")
#     print("To your right, there is more forest.")
#     print("There is a rock wall directly in front of you.")
#     print("Behind you is the forest exit.\n")
    
#     response = input("What direction do you move?\nleft/right/forward/backward\n")

#     if response == "left":
#         print("You encounter a witch in a house made of candy. What do you do?")
#         fight = input("Fight the witch? (y/n)\n")
        
#         if fight.lower() == "y":
#             print("A 10-sided dice is rolled to see if you beat the witch. You need a 5 or higher.")
#             number = random.randint(1, 10)
            
#             if number >= 5:
#                 print(f"You have defeated the witch with a roll of {number} and escaped the forest with a friendly cat named Binx.")
#             else:
#                 print("You rolled less than 5. The witch throws you into the oven.")
#                 quit()
#         else:
#             print("You ran away.")
    
#     elif response == "right":
#         print("You head deeper into the forest. You find a castle in front of you.")
#         castle = input("You enter the castle. Do you go left or right?\n")
        
#         if castle == "left":
#             print("You fall through a trap door and find a hulk. You find a bow and arrows next to you.")
#             troll = input("Do you shoot the hulk or try to run? (shoot/run)\n")
            
#             if troll.lower() == "shoot":
#                 arrow = random.randint(1, 10)
#                 print("You try and shoot the hulk with 70% accuracy.")
                
#                 if arrow <= 7:
#                     print("You shoot the hulk and escape the castle.")
#                     quit()
#                 else:
#                     print("You try and shoot the hulk and miss. Then you get hulksmashed.")
#             else:
#                 print("You try and run from the hulk but he catches you and throws you in the dungeon.")
#                 quit()
#         else:
#             print("You head to the right and find a staircase. You start to ascend and get to the top, finding the princess.")
#             princess = input("Do you try and save her? (y/n)\n")
            
#             if princess.lower() == "y":
#                 print("You save the princess and escape the castle.")
#             else:
#                 print("The princess shoots you for being an asshole.")
#                 quit()

#     elif response == "forward":
#         wall = input("You find a wall you can climb. Do you climb it? (y/n)\n")
        
#         if wall.lower() == "y":
#             print("You scale the wall and find a dragon.")
#             dragon = input("Do you charm the dragon or run? (c/r)\n")
            
#             if dragon.lower() == "c":
#                 print("You charm the dragon and ride it to safety.")
#                 quit()
#             else:
#                 print("The dragon is the child of Daenerys Targaryen. She asks you to bend the knee, but you believe Tyrion should lead the seven kingdoms. So she burns you alive.")
#                 quit()
#         else:
#             print("You turn back and get lost, finding a creature guarding a ring.")
#             print("The creature calls the ring 'my precious.'")
#             ring = input("Do you take the ring from him? (y/n)\n")
            
#             if ring.lower() == "y":
#                 print("You take a chance to steal the ring.")
#                 rings = random.randint(1, 10)
                
#                 if rings >= 5:
#                     print(f"You rolled a {rings}. You take your chance to steal the ring and grab it, harnessing its power to escape.")
#                 else:
#                     print(f"You rolled a {rings}. The creature catches you and throws you into a pit to never be seen again.")
#             else:
#                 print("The creature is grateful you did not try and steal his precious and leads you to the exit.")

#         response = ""

#     elif response == "backward":
#         print("A magical door to the forest slams behind you and now you are stuck.")
#         cave = input("Do you go to the cave or the tower?\n")
        
#         if cave.lower() == "cave":
#             print("You find Tony Stark stuck in a cave building a suit and help him escape. You escape also.")
#         else:
#             print("You find the true boogeyman, John Wick. He kills all the creatures of the forest, and you become the ruler of the forest as he leaves to avenge the death of his dog.")
#     else:
#         print("I didn't understand that.\n")

#     play_again = input("Play again? (y/n): ")
#     if play_again.lower() != "y":
#         break

import random

# Intro
print("Welcome to Trevor's Basketball Game!")
player_name = input("Enter your player name:\n")

# Game variables
player_score = 0
opponent_score = 0

# Start of the game
print(f"Alright, {player_name}! Get ready for basketball.")

while True:
    print("\nCurrent Score:")
    print(f"{player_name}: {player_score} | Opponent: {opponent_score}")

    # Player's action
    action = input("\nChoose your move: shoot/dribble/defend\n").lower()

    if action == "shoot":
        shot_result = random.choice(["made", "missed"])
        if shot_result == "made":
            print(f"You made the shot! +2 points.")
            player_score += 2
            # Opponent gets a random number of points only if the player misses
            opponent_points = random.randint(0, 3)
            print(f"The opponent scores {opponent_points} points.")
            opponent_score += opponent_points
        else:
            print("You missed the shot. No points.")
            # If it's a turnover, opponent scores
            opponent_points = random.randint(1, 3)
            print(f"Opponent scores {opponent_points} points due to a turnover.")
            opponent_score += opponent_points
        
    elif action == "dribble":
        print("You dribble the ball, trying to find an opening.")
        opponent_action = random.choice(["steal", "block"])
        
        if opponent_action == "steal":
            print("Opponent steals the ball. Turnover!")
            # If it's a turnover, opponent scores
            opponent_points = random.randint(1, 3)
            print(f"Opponent scores {opponent_points} points due to a turnover.")
            opponent_score += opponent_points
        else:
            print("You successfully dribble past the opponent.")
            # Add points for successful dribble
            dribble_points = random.randint(2, 3)
            print(f"You gained {dribble_points} points for either a layup, pull up, or three!")
            player_score += dribble_points
    
    elif action == "defend":
        opponent_action = random.choice(["shoot", "dribble"])
        print(f"Opponent attempts to {opponent_action}.")
        
        if opponent_action == "shoot":
            shot_result = random.choice(["made", "missed"])
            if shot_result == "made":
                print("Opponent made the shot. +2 points for them.")
                opponent_score += 2
            else:
                print("Opponent missed the shot. Good defense!")
        else:
            print("You defend well, preventing the opponent from advancing.")

    else:
        print("Invalid move. Choose a valid move: shoot/dribble/defend")

    # Check if the game is over
    if player_score >= 10:
        print(f"Congratulations, {player_name}! You won the game with a score of {player_score}-{opponent_score}.")
        break
    elif opponent_score >= 10:
        print(f"Sorry, {player_name}. You lost the game with a score of {player_score}-{opponent_score}. Better luck next time.")
        break