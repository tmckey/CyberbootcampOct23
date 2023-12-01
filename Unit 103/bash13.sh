#!/bin/bash
# Bob is back at it again! Now he needs us to script something that if user inserts between 2 to 5, it will print out “Valid Number” and “your number is ___”.
# And if the user input is not between 2 and 5, it will print out “not valid!”
 
#Main
# -eq = equal
# -ne = are not equal
# -gt = greater than
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)

#!/bin/bash

echo "Enter a number between 2 and 5: "
read user_input

# Check if the input is a number
if [[ $user_input =~ ^[0-9]+$ ]]; then
    # Check if the number is between 2 and 5 (inclusive)
    if ((user_input >= 2 && user_input <= 5)); then
        echo "Valid Number"
        echo "Your number is $user_input"
    else
        echo "Not valid!"
    fi
else
    echo "Invalid input. Please enter a valid number."
fi