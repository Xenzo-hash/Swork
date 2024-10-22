import argparse
import subprocess
import socket
import os
import platform
import re

def print_banner():
    banner = """
    ________  ___       __   ________  ________  ___  __       
    |\   ____\|\  \     |\  \|\   __  \|\   __  \|\  \|\  \     
    \ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \/  /|_   
     \ \_____  \ \  \  __\ \  \ \  \\\  \ \   _  _\ \   ___  \  
      \|____|\  \ \  \|\__\_\  \ \  \\\  \ \  \\  \\ \  \\ \  \ 
        ____\_\  \ \____________\ \_______\ \__\\ _\\ \__\\ \__\
       |\_________\|____________|\|_______|\|__|\|__|\|__| \|__|
       \|_________|                                             
    """
    print(banner)

def display_commands():
    # Command descriptions
    commands = [
        ("--aggressivescan", "Aggressive scan, bypassing firewalls (root needed)", True),
        ("--tcpconnectscan", "TCP connect scan", False),
        ("--udpconnectscan", "UDP scan", False),
        ("--versiondetect", "Service version detection (root needed)", True),
        ("--osidentify", "Operating system detection (root needed)", True),
        ("--synscan", "SYN scan (root needed)", True),
        ("--pingscan", "Ping scan", False),
        ("--fragmentedscan", "Fragmented scan (root needed)", True),
        ("--customportrange", "Custom port range scan", False),
        ("--dnslookup", "Reverse DNS lookup", False),
        ("--traceroute", "Traceroute to target", False),
        ("--whois", "WHOIS lookup", False),
        ("--interfaceinfo", "Show local network interface info (root needed)", True),
        ("--wifiscans", "Scan for open Wi-Fi networks", False),
        ("--bannergrab", "Grab the service banner from a specified IP and port", False),
    ]
    
    print("\nAvailable Commands:\n")
    for command, description, needs_root in commands:
        if needs_root:
            print(f"\033[91m{command}\033[0m - {description}")  # Red text for root needed
        else:
            print(f"\033[94m{command}\033[0m - {description}")  # Blue text for no root needed

def check_root():
    if os.geteuid() != 0:
        print("\033[91mYou need root access to use this command.\033[0m")
        return False
    return True

def ping_scan(target):
    print(f"Pinging {target}...")
    response = subprocess.call(['ping', '-c', '4', target])
    if response == 0:
        print(f"{target} is reachable.")
    else:
        print(f"{target} is not reachable.")

def tcp_connect_scan(target):
    print(f"Starting TCP connect scan on {target}...")
    ports = [22, 80, 443]  # Example ports to scan
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open.")
        else:
            print(f"Port {port} is closed.")
        sock.close()

def aggressive_scan(target):
    print(f"Performing aggressive scan on {target}...")
    # Placeholder: Add your aggressive scan logic here
    # This could involve multiple scan types, service detection, etc.
    tcp_connect_scan(target)  # For demonstration, running a TCP connect scan

def dns_lookup(target):
    print(f"Performing reverse DNS lookup for {target}...")
    try:
        ip = socket.gethostbyname(target)
        print(f"IP address for {target} is {ip}.")
    except socket.gaierror:
        print(f"Could not resolve {target}.")

def whois_lookup(target):
    print(f"Performing WHOIS lookup for {target}...")
    # Placeholder for WHOIS implementation
    # You might want to use a library like `whois` to implement this.

def main():
    print_banner()
    display_commands()
    
    # Argument parsing
    parser = argparse.ArgumentParser(description='Swork - A Lightweight Network Scanner')

    # Adding command arguments
    parser.add_argument('--aggressivescan', help='Aggressive scan, bypassing firewalls', action='store_true')
    parser.add_argument('--tcpconnectscan', help='TCP connect scan', action='store_true')
    parser.add_argument('--udpconnectscan', help='UDP scan', action='store_true')
    parser.add_argument('--versiondetect', help='Service version detection', action='store_true')
    parser.add_argument('--osidentify', help='Operating system detection', action='store_true')
    parser.add_argument('--synscan', help='SYN scan', action='store_true')
    parser.add_argument('--pingscan', help='Ping scan', action='store_true')
    parser.add_argument('--fragmentedscan', help='Fragmented scan', action='store_true')
    parser.add_argument('--customportrange', help='Custom port range scan', nargs=2, metavar=('START_PORT', 'END_PORT'))
    parser.add_argument('--dnslookup', help='Reverse DNS lookup', action='store_true')
    parser.add_argument('--traceroute', help='Traceroute to target', action='store_true')
    parser.add_argument('--whois', help='WHOIS lookup', action='store_true')
    parser.add_argument('--interfaceinfo', help='Show local network interface info', action='store_true')
    parser.add_argument('--wifiscans', help='Scan for open Wi-Fi networks', action='store_true')
    parser.add_argument('--bannergrab', help='Grab the service banner from an IP and port', nargs=2, metavar=('IP', 'PORT'))

    args = parser.parse_args()

    target = input("Enter target IP or domain: ")

    if args.aggressivescan:
        if check_root():
            aggressive_scan(target)

    if args.tcpconnectscan:
        tcp_connect_scan(target)

    if args.pingscan:
        ping_scan(target)

    if args.dnslookup:
        dns_lookup(target)

    if args.whois:
        whois_lookup(target)

if __name__ == "__main__":
    main()
