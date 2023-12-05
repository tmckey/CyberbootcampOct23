#!/bin/bash
# Create a script that you think you would use in a daily job routine No right or Wrong anwsers here
# You could ping all the devices in your network?
# Run a script to reset your ip address?
# Create a script that does some math? 


network="192.168.0"  # Replace this with your network prefix

# Iterate over all possible host addresses in the network
for ((i=1; i<=254; i++)); do
    ip="$network.$i"
    ping -c 1 -W 1 "$ip" &> /dev/null

    if [ $? -eq 0 ]; then
        echo "Device with IP $ip is reachable"
    else
        echo "Device with IP $ip is not reachable"
    fi
done

# The definitions are for the terms in the Bash script above:
## for i in {1..254}; do ... done:
# for i in {1..254} is a Bash loop that iterates through a sequence of numbers from 1 to 254.
# i is a variable that holds the current value from the sequence during each iteration of the loop.
## ip:
# In the context of the script, ip is a variable used to store the constructed IP address based on the network prefix and the iteration value i in the loop.
# For instance, if the network variable is set to 192.168.1, and during an iteration i equals 10, then ip will be 192.168.1.10.
# &>:
# In Bash, &> is a redirection operator used for redirecting both standard output (stdout) and standard error (stderr) of a command to a file or suppressing output.
# For example, ping -c 1 -W 1 "$ip" &> /dev/null redirects both output and errors generated by the ping command to /dev/null, a special device file that discards the data written to it.
# $network.$1:
# $network is a variable that holds the network prefix, like 192.168.1 in the script.
# $1 refers to the first argument passed to the script when it is executed.
# When used together like $network.$1, it concatenates the value of $network with the value of the first argument passed to the script. For instance,
# if the script is executed as ./bash14.sh 10, and $network is 192.168.1, then $network.$1 will result in 192.168.1.10.