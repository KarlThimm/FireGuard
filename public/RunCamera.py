import pexpect
import time

# Constants
HOST = "128.4.222.193"
USER = "karlthimm"
PASSWORD = "Shock042"
SSH_COMMAND = f"ssh -Y {USER}@{HOST}"
COMMAND = "sudo -E ircamera I2C MLX90640"

def ssh_login(host, user, password, command):
    try:
        # Start the SSH connection
        session = pexpect.spawn(SSH_COMMAND, timeout=20)
        session.expect("password:")  # Wait for the password prompt
        
        # Send the password
        session.sendline(password)
        
        # Wait for a few seconds to ensure the connection is established
        time.sleep(5)
        
        # Send the command
        session.sendline(command)
        
        # Wait for a moment to allow the command to execute
        time.sleep(2)

        # Optionally, you can handle expected outputs or further interactions
        # session.expect("some_expected_output_after_command")
        # print(session.before)  # Print the output before this expected output
        
        # Interact with the terminal (this hands control over to the user)
        session.interact()

        # Close the session after interact returns (user exits the remote shell)
        session.close()
    except pexpect.exceptions.EOF:
        print("EOF encountered, possibly connection failure.")
    except pexpect.exceptions.TIMEOUT:
        print("Timeout occurred, check network or server.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    ssh_login(HOST, USER, PASSWORD, COMMAND)

