# Write a program that works out whether if a given number is an 
# odd or even 2
#Write your code below this line 👇

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))

# Check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Use Modulus Operator ( % ) to check if the remainder obtained after dividing the given number N by 2 is 0 or 1.
# If the remainder is 0, print “Even”
# If the remainder is 1, print “Odd” 
# The input() function is used to take user input, and int() is used to convert the input to an integer since we want to check a number.
# The program then uses an if statement to check if the number is even or odd.
# The % (modulo) operator is used to find the remainder when the number is divided by 2. If the remainder is 0, the number is even; otherwise, it's odd.
# The program prints the result accordingly.



  # 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

# Constants
total_years = 90

# Calculate remaining time
years_left = total_years - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

# Print the result using f-strings
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")    

# Explanation:

# The program takes the user's current age as input.
# It calculates the remaining years, weeks, and months until the age of 90.
# The calculated values are then printed using f-strings in the specified format