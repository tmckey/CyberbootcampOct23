# Bob wants to create a guessing number game! 
# Rule 1: Numbers have to be between 1 and 20
# Rule 2: Program must run until the correct number is guessed
# Rule 3: When guessed right, print out how many tries to guess the 
# right number. Example: "Yes! You guessed it in ___ guesses."
# Rule 4: The program will tell you if your number needs to be HIGHER
# or LOWER 
# until the number is guessed correctly and the program ENDS.
# Remeber to import the random function
#Bonus objective can you put it into a loop to make the game end after 3 turns?

# import random

# def guessing_game():
#     correct_number = random.randint(1, 20)
#     tries = 0

#     while True:
#         guess = int(input("Guess a number between 1 and 20: "))
#         tries += 1

#         if guess == correct_number:
#             print(f"Yes! You guessed it in {tries} {'tries' if tries > 1 else 'try'}.")
#             break
#         elif guess < correct_number:
#             print("Try a HIGHER number.")
#         else:
#             print("Try a LOWER number.")

# if __name__ == "__main__":
#     for _ in range(3):  # Bonus: Allow 3 turns
#         guessing_game()


import random

def number_guessing_game():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1,20)

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 20.")

    attempts = 0
    max_attempts = 3 #variable set to 3, indicaing the maximum number of attempts allowed

    while attempts < max_attempts:  #The while loop runs as long as the attempts counter is less than max_attempts. 
        user_guess = int(input("Enter your guess: "))
        attempts += 1


        if user_guess < secret_number:
            print("Try a higher number.")
        elif user_guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Yes! You guessed it in {attempts} guesses.")
            return

    print(f"Sorry, you've reached the maximum attempts. The correct number was {secret_number}.")  

def main():
    # Call the number guessing game function
    number_guessing_game()

#Call the main function to start the game
main()  

# import random

# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# secret_number = random.choice(nums)

# print(secret_number)
# tries = 0
# max_tries = 3

# while tries < max_tries:
#     user_num = int(input('Guess the number between 1-20: '))

#     if user_num == secret_number:
#         tries += 1
#         print(f"Wow, you got it right in {tries}!")
#         break 
#     else:
#         tries += 1
#         if tries == max_tries:
#             print(f"Sorry, you've used all your tries. The secret number was {secret_number}.")
#         else:
#             print("Keep guessing")    
