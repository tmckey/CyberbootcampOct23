# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b

a = 5
b = 5

if a == b:
    print("The values of 'a' and 'b' are equal")


# Not Equals: a != b
a = 5
b = 10

if a != b:
    print("The values of 'a' and 'b' are not equal.")

# Less than: a < b
a = 5
b = 10

if a < b:
    print("The value of 'a' is less than 'b'.")
else:
    print("The value of 'a' is not less than 'b'.")

# Less a than or equal to: a <= b
a = 5
b = 10

if a <= b:
    print("The value of 'a' is less than or equal to 'b'.")
else:
    print("The value of 'a' is greater than 'b'.")



# Greater than: a > b
a = 15
b = 10

if a > b:
    print("The value of 'a' is greater than 'b'.")
else:
    print("The value of 'a' is not greater than 'b'.")


# If a is Greater than or equal to: a >= b
a = 15
b = 10

if a >= b:
    print("The value of 'a' is greater than or equal to 'b'.")
else:
    print("The value of 'a' is less than 'b'.")

# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
a = 10
b = 20

if a == b:
    print("The values of 'a' and 'b' are equal.")
elif a < b:
    print("The value of 'a' is less than 'b'.")
else:
    print("The value of 'a' is greater than 'b'.")



# Create an if statement that includes both elif and else to execute when both if and elif are not met.
x = 10
y = 20


if x == y:
    print("x is equal to y.")
elif x < y:
    print("x is less than y.")
else:
    print("x is greater than y.")


# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.
x = 10
y = 20

# If both x is greater than 5 and y is less than 30
if x > 5 and y < 30:
    print("Both conditions are true.")
else:
    print("At least one of the conditions is not true.")


# Create an if statement with two conditions by using or between conditions.
x = 10
y = 20

# If either x is greater than 15 or y is less than 15
if x > 15 or y < 15:
    print("At least one of the conditions is true.")
else:
    print("Neither of the conditions is true.")


# Create a nested if statement.
x = 10
y = 20

# Outer if statement
if x > 5:
    print("x is greater than 5.")

    # Nested if statement
    if y > 15:
        print("y is greater than 15.")
    else:
        print("y is not greater than 15.")
else:
    print("x is not greater than 5.")


# Create an if statement that includes pass to avoid errors.
x = 10
y = 20

# If x is greater than y, do nothing
if x > y:
    pass
else:
    print("x is not greater than y.")