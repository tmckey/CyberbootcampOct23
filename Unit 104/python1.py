# Write a multi-line comment with your name, favorite food, and dream job on 3 different lines.

'''
My name is Trevor McKey
My favorite food is pizza.
My dream job is coaching college basketball.
'''

# assign 5 different data types to 5 different variables. At least one datatype must be a string.

#Integer
userage = 36 
print(userage)

#Float
userHeight = 74
print(userHeight)

#String
userName = "Trev" + "Henry" + "Tennessean"
print(userName)
print(len(userName))

#List
kidsAge = [7, 4, 1]
print (kidsAge)

userage = [33, 34, 35, 36, 37]
print(userage)

#Dictionary
kidsNameAndAge = {"Forrest":7, "Jack":4, "Luke":1}
print (kidsNameAndAge)

kidsNameAndAge = dict(Forrest = 7, Jack = 4, Luke = 1)
print (kidsNameAndAge)


# print the length of your string.

string = "Love the LORD your GOD with all your heart, with all your soul, and with all your mind"
print (string)
print(len(string))


# create a new variable called savvy, and assign it the string with this phrase "Learning Python is Awesome!"

savvy = "Learning Python is Awesome!"
print(savvy)



# Replace "Awesome" with "great" in the string

new_savvy=savvy.replace("Awesome, great")
print(new_savvy)


# Create and assign 3 more variables called name, age and length using the multi-variable naming method.

name = "Trevor"
age = 36
length = 74
print (name)
print (age)
print (length)

name, age, length = "Trevor", 36, 74

# Format a new string called 'miniBio' using variables in curly brackets to complete this phrase... "Hi my name is (name), I am (tall) and (so) old today."

name = "Trevor"
tall = "6'2\""
so = 36

miniBio = f"Hi my name is {name}, I am {tall}, and {so} old today."
print (miniBio)

    ###The miniBio string is created using an f-string (formatted string literal) where variables are placed within curly braces {}.
    ###The variables are substituted with their respective values when the string is evaluated.
    ### https://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf


# Create a list of at least 5 elements of mixed data types

mixed_list = [36, "Trevor", 74 {"Forrest":7, "Jack":4, "Luke":1}, ("Trev" + "Henry" + "Tennessean")]
    #interger, variable, variable, dictionary, string
print (mixed_list)


# replace a part of it with something else
mixed_list[1]="hi"
print (mixed_list)



# append or insert several more items to the list

mixed_list.append(33)
print (mixed_list)


# find and print the length of the list

print(len(mixed_list))

# slice a sub-section of the 1st list, and save it to a different 2nd list

userage2 = userage[1:3]


# print the 2nd list

print(userage2)

# extend your original list with the 2nd list sliced above

userage.append(38)
print(userage)


# Create a new list called "simList" containing at least 5 elements of the same data type, either string, integer, float, or Boolean.

simList=[50,45,48,47,46, 49]
print(simList)


# sort "simList", and print the list

simList.sort()
print(simList)


# copy the "simList" list to another 3rd list

simList=[50,45,48,47,46, 49]
thirdList = simList.copy()
print(thirdList)


# add the 2nd and 3rd lists together into a 4th list


mixed_list = [36, "Trevor", 74 {"Forrest":7, "Jack":4, "Luke":1}, ("Trev" + "Henry" + "Tennessean")]
userage2 = userage[1:3]
thirdList = simList.copy()

combined_list = mixed_list + userage2 + thirdList
print (combined_list)