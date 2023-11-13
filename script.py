import subprocess

def execute_command(command):
    try:
        # Run the command in the terminal
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)

        # Print the output
        print("Command Output:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        # If the command fails, print the error message
        print("Error:", e)

if __name__ == "__main__":
    # Example command: print the current directory
    command_to_execute = "sudo sh -c 'echo 1 >  /proc/sys/vm/drop_caches'"
    command_to_execute = "free -h"
    command_to_execute = "sudo sh -c 'echo 2 >  /proc/sys/vm/drop_caches'"
    commmand_to_execute = 'free -h'
    command_to_execute = "sudo sh -c 'echo 3 >  /proc/sys/vm/drop_caches'"  
    command_to_execute = 'free -h'


    # Execute the command
    execute_command(command_to_execute)

