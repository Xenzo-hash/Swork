import os
import sys
import subprocess
import whois
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Define the banner with colors
banner = f"""{Fore.WHITE}________  ___       __   ________  ________  ___  __       
|\   ____\|\  \     |\  \|\   __  \|\   __  \|\  \|\  \     
\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \/  /|_   
 \ \_____  \ \  \  __\ \  \ \  \\\  \ \   _  _\ \   ___  \  
  \|____|\  \ \  \|\__\_\  \ \  \\\  \ \  \\  \\ \  \\ \  \ 
    ____\_\  \ \____________\ \_______\ \__\\ _\\ \__\\ \__\
   |\_________\|____________|\|_______|\|__|\|__|\|__| \|__|
   \|_________|                                             
"""

# Display the banner
print(banner)

# Define commands and their descriptions with examples
commands = {
    "--scan": "Perform a basic scan on the target IP or domain. Example: `--scan example.com`.",
    "--detailed": "Run a detailed scan on the target IP or domain. Example: `--detailed example.com`.",
    "--service": "Identify services running on open ports of the target. Example: `--service example.com`.",
    "--version": "Determine the version of services on the target. Example: `--version example.com`.",
    "--traceroute": "Trace the route to the target IP or domain. Example: `--traceroute example.com`.",
    "--os-detect": "Attempt to identify the operating system of the target. Example: `--os-detect example.com`.",
    "--whois": "Perform a WHOIS lookup on the target IP or domain. Example: `--whois example.com`.",
    "--http": "Scan for HTTP related information of the target. Example: `--http example.com`.",
    "--dns": "Perform a DNS lookup for the target IP or domain. Example: `--dns example.com`.",
    "--aggressive": "Perform an aggressive scan (may bypass some firewalls) on the target. Example: `--aggressive example.com`."
}

# Check if root access is required for certain commands
root_required_commands = ["--os-detect", "--http", "--aggressive"]

def print_commands():
    print(Fore.RED + "Commands requiring root access:")
    for command in root_required_commands:
        print(f"{Fore.RED}{command}{Style.RESET_ALL} - {commands[command]}")

    print("\n" + Fore.BLUE + "Commands not requiring root access:")
    for command in commands:
        if command not in root_required_commands:
            print(f"{Fore.BLUE}{command}{Style.RESET_ALL} - {commands[command]}")

def run_command(command, target):
    if command == "--scan":
        print(f"Running basic scan on {target}...")
        # Placeholder for actual scan logic
    elif command == "--detailed":
        print(f"Running detailed scan on {target}...")
        # Placeholder for actual detailed scan logic
    elif command == "--service":
        print(f"Identifying services running on {target}...")
        # Placeholder for logic to identify services
    elif command == "--version":
        print(f"Determining versions of services on {target}...")
        # Placeholder for logic to determine versions
    elif command == "--traceroute":
        print(f"Tracing route to {target}...")
        # Placeholder for logic for traceroute
    elif command == "--os-detect":
        if os.geteuid() != 0:  # Check for root access
            print(f"{Fore.RED}You need root access to use this command.{Style.RESET_ALL}")
            return
        print(f"Attempting to detect OS of {target}...")
        # Placeholder for logic to detect OS
    elif command == "--whois":
        print(f"Performing WHOIS lookup on {target}...")
        try:
            w = whois.whois(target)
            print(w)
        except Exception as e:
            print(f"Error: {str(e)}")
    elif command == "--http":
        if os.geteuid() != 0:  # Check for root access
            print(f"{Fore.RED}You need root access to use this command.{Style.RESET_ALL}")
            return
        print(f"Scanning HTTP information of {target}...")
        # Placeholder for logic to scan HTTP
    elif command == "--dns":
        print(f"Performing DNS lookup for {target}...")
        try:
            response = subprocess.check_output(['dig', target])
            print(response.decode())
        except Exception as e:
            print(f"Error: {str(e)}")
    elif command == "--aggressive":
        if os.geteuid() != 0:  # Check for root access
            print(f"{Fore.RED}You need root access to use this command.{Style.RESET_ALL}")
            return
        print(f"Running aggressive scan on {target}...")
        # Placeholder for aggressive scan logic
    else:
        print("Unknown command.")

def main():
    print_commands()
    print("\nExamples of how to use the commands:\n")
    for command in commands:
        print(f"{Fore.WHITE}{command}{Style.RESET_ALL} - {commands[command]}")
    
    print("\nPlease enter the command followed by the target (e.g., --scan example.com):\n")
    
    while True:
        command_input = input("Enter a command (or type 'exit' to quit): ").strip()
        if command_input.lower() == "exit":
            print("Exiting SeeWork tool.")
            break
        
        # Split command and target
        parts = command_input.split()
        command = parts[0]
        target = parts[1] if len(parts) > 1 else None
        
        if command in commands:
            if target:
                run_command(command, target)
            else:
                print("Please specify a target IP or domain.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
