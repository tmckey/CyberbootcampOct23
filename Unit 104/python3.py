# Scenario
# Using one of the comparison operators in Python, write a simple program that takes the parameter n as input,
#  which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

#Chat GPT's Code10
# def check_greater_than_or_equal_to_100(n):
#     result = n >= 100
#     print(result)

# # Taking user input for n
# n = int(input("Enter an integer value for n: "))

# # Checking and printing the result
# check_greater_than_or_equal_to_100(n)


#Josh' Code
# integer = int(input("Enter a Number: "))
# print("Integer is: " + str(integer))  # Printing the integer entered by the user

# # If statement with a logical conditional and elif
# if integer > 100:
#     print("True")
# elif integer < 100:
#     print("False")


#Victor's Code
n = int(input("Enter a number:"))
m = 100
if n >= m:
    print("True")
else: print ("False")