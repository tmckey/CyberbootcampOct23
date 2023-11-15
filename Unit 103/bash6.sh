#!/bin/bash
# Install whois on your Ubuntu

# Add to your bash script a sixth option that calls a function to:

# Take a user input string. Presumably the string is a domain name such as Google.com.
# Run whois against a user input string.
# Run dig against the user input string.
# Run host against the user input string.
# Run nslookup against the user input string.
# Output the results to a single .txt file and open it with your favorite text editor.

# For this challenge you must use at least one variable and one function.

#!/bin/bash
# Install whois on your Ubuntu

# Function to perform whois, dig, host, nslookup, and save results to a file
echo "Enter a website."
read website

function gather_info() {
    whois $website >> whois.txt
    echo "----" >> whois.txt
    dig $website >> whois.txt
    echo "----" >> whois.txt
    host $website >> whois.txt
    echo "----" >> whois.txt
    aslookup $website >> whois.txt
}

gather_info