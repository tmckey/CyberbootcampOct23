#!/bin/bash
#Lets create a script that would work like a DDOS attack by using a while loop
#In this script we want to contiune to ping our personal pc in a infitine while loop
#Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash

while :
do
    ping 192.168.0.179
   echo "Keep running"
   sleep 3
 done

#!/bin/bash
# https://ss64.com/bash/
# https://www.neuralnine.com/code-a-ddos-script-in-python/


#Lets create a script that would work like a DDOS (Distributed Denial of Service) attack by using a while loop


#In this script we want to contiune to ping our personal pc in a infitine while loop
#Somebody that had a control of a bot net could set up this script on thousands of computer and ping sites till they are overloaded and crash




# IP = ("192.168.0.179")


# for IP in "192.168.0.179"
# do
#  echo $IP
#  ping -c 1 $IP
# done


# This bash code is a simple loop that pings an IP address. Let's break down each element of the code:


# do: This keyword starts the loop execution. It signifies the beginning of the loop block.


# echo $IP: This line outputs the value of the variable IP. It prints the IP address being processed by the loop.


# ping -c 1 $IP: This line pings the IP address using the ping command with the -c 1 option. It sends a single ICMP echo request packet to the IP address.


# done: This keyword marks the end of the loop block. It signifies the completion of the loop.


# Overall, this code iterates over a specified IP address (192.168.10.1 in this case) and prints the IP address before pinging it.
