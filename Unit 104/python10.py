# Create a Python script that performs the following:

# Prompt the user to type a string input as the variable for your destination URL.

# Prompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
# OPTIONS
# Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
# Add some comments of what these request are doing to your script
# Using the requests library, perform a GET request to your github.

# For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#response = requests.get()
# For the given URL, print response header information to the screen.

# from urllib import response
# import requests
# b = input("Get, Post, Put, Delete , Head, Patch, Options:")


import requests

# Prompt the user to type a string input as the variable for your destination URL.
url = input("Enter the destination URL: ")

# Prompt the user to select an HTTP Method
http_method = input("Choose an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Print the entire request about to be sent and ask for confirmation
print("\nRequest about to be sent:")
print(f"URL: {url}")
print(f"HTTP Method: {http_method}")

# Get user confirmation before proceeding
confirmation = input("\nDo you want to proceed? (yes/no): ").lower()

if confirmation != 'yes':
    print("Operation canceled.")
else:
    # Using the requests library, perform the specified HTTP request to the provided URL
    response = requests.request(http_method, url)

    # Print the response header information to the screen
    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Translate HTTP status code into plain terms
    if response.status_code == 200:
        print("Success: Request completed successfully")
    elif response.status_code == 404:
        print("Error 404: Site not found")
    elif response.status_code == 500:
        print("Error 500: Internal Server Error")
    else:
        print(f"HTTP Status Code: {response.status_code}")

#  from urllib import response
# import requests
# b = input("Get, Post, Put, Delete , Head, Patch, Options:")
# if b == "Get":
#     response = requests.get('https://github.com/Aingargiola/Learning-github-')
# elif b == "Post":
#     response = requests.post('https://github.com/Aingargiola/Learning-github-')
# elif b == "Put":
#     response = requests.put('https://github.com/Aingargiola/Learning-github-')
# elif b == "Delete":
#     response = requests.delete('https://github.com/Aingargiola/Learning-github-')
# elif b == "Head":
#     response = requests.head('https://github.com/Aingargiola/Learning-github-')
# elif b == "Patch":
#     response = requests.patch('https://github.com/Aingargiola/Learning-github-')
# elif b == "Options":
#     response = requests.options('https://github.com/Aingargiola/Learning-github-')
# else:
#     print("input error")
#     quit()
# anwser = input("Enter yes or no: ")
# if anwser == "yes":
#     print(response)
# else:
#     print("cancelling")
# if b == "Post":
#     print("Site not found")
# elif b == "Get":
#     print("Request has succedded")
# elif b == "Put":
#     print("This request is Frobidden")
# elif b == "Delete":
#     print("This request is Forbidden")
# elif b == "Head":
#     print("Request has Succedded")
# elif b == "Patch":
#     print("Request is forbidden")
# elif b == "Options":
#     print("Site not found")
# else:
#     print("Bad Request")       

