# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run



# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os

# Bash operations
whoami_command = "whoami"
ip_a_command = "ip a"
lshw_short_command = "lshw -short"

# Execute commands with descriptions
def execute_command(command, description):
    print(f"\nExecuting: {description}")
    os.system(command)

# Execute the commands
execute_command(whoami_command, "Displaying current user")
execute_command(ip_a_command, "Displaying network interfaces")
execute_command(lshw_short_command, "Displaying hardware information (short)")
