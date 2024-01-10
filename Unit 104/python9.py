# Your program should print each number from 1 to 100 in turn.

# When the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# You will need to use a for loop to write this:


#Write your code below this row 👇

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# This code uses a for loop to iterate through numbers from 1 to 100 (inclusive) and checks the conditions for Fizz, Buzz, and FizzBuzz. If the number is divisible by both 3 and 5, it prints "FizzBuzz". If only divisible by 3, it prints "Fizz". If only divisible by 5, it prints "Buzz". Otherwise, it prints the current number.

# for fizzbuzz in range(101):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#     print(fizzbuzz)
        
for number in range(1, 101):
    output = "Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0)
    print(output or number)       

# This code leverages the fact that in Python, True is equivalent to 1 and False is equivalent to 0. The multiplication by (number % 3 == 0) and (number % 5 == 0) results in empty strings for numbers not divisible by 3 or 5, and concatenates them accordingly. The or operator is then used to print the number if the output is an empty string.